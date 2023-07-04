import random
from typing import TYPE_CHECKING, Any, Type, Union, cast

from pyfactories.exceptions import ParameterError
from pyfactories.utils import unwrap_new_type_if_needed
from pyfactories.value_generators.complex_types import handle_complex_type

if TYPE_CHECKING:  # pragma: no cover
    from pydantic.v1 import ConstrainedList, ConstrainedSet
    from pydantic.v1.fields import ModelField

    from pyfactories.factory import ModelFactory


def handle_constrained_collection(
    collection_type: Union[Type[list], Type[set]],
    model_factory: Type["ModelFactory"],
    model_field: "ModelField",
) -> Union[list, set]:
    """Generate a constrained list or set."""
    constrained_field = cast(
        "Union[ConstrainedList, ConstrainedSet]",
        unwrap_new_type_if_needed(model_field.outer_type_),
    )  # pragma: no cover
    min_items = constrained_field.min_items or 0
    max_items = (
        constrained_field.max_items if constrained_field.max_items is not None else min_items + 1
    )
    unique_items = getattr(constrained_field, "unique_items", False)

    if max_items < min_items:
        raise ParameterError("max_items must be longer or equal to min_items")

    if model_field.sub_fields:
        handler = lambda: handle_complex_type(  # noqa: E731
            model_field=random.choice(model_field.sub_fields),
            model_factory=model_factory,  # pyright: ignore
        )
    else:
        t_type = constrained_field.item_type if constrained_field.item_type is not Any else str
        handler = lambda: model_factory.get_mock_value(t_type)  # noqa: E731

    collection: Union[list, set] = collection_type()
    try:
        while len(collection) < random.randint(min_items, max_items):
            value = handler()  # type: ignore
            if isinstance(collection, set):
                collection.add(value)
            else:
                if unique_items and value in collection:
                    continue
                collection.append(value)
        return collection
    except TypeError as e:
        raise ParameterError(
            f"cannot generate a constrained collection of type: {constrained_field.item_type}"
        ) from e
