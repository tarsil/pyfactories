import random
from collections import defaultdict, deque
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, Union, cast

from pydantic.v1.fields import (
    SHAPE_DEFAULTDICT,
    SHAPE_DEQUE,
    SHAPE_DICT,
    SHAPE_FROZENSET,
    SHAPE_ITERABLE,
    SHAPE_LIST,
    SHAPE_MAPPING,
    SHAPE_SEQUENCE,
    SHAPE_SET,
    SHAPE_TUPLE,
    SHAPE_TUPLE_ELLIPSIS,
    ModelField,
)

from pyfactories.utils import is_any, is_union
from pyfactories.value_generators.primitives import create_random_string

if TYPE_CHECKING:  # pragma: no cover
    from pyfactories.factory import ModelFactory

type_mapping = {
    "Dict": dict,
    "Sequence": list,
    "List": list,
    "Set": set,
    "Deque": deque,
    "Mapping": dict,
    "Tuple": tuple,
    "DefaultDict": defaultdict,
    "FrozenSet": frozenset,
    "Iterable": list,
}

shape_mapping = {
    SHAPE_LIST: list,
    SHAPE_SET: set,
    SHAPE_MAPPING: dict,
    SHAPE_TUPLE: tuple,
    SHAPE_TUPLE_ELLIPSIS: tuple,
    SHAPE_SEQUENCE: list,
    SHAPE_FROZENSET: frozenset,
    SHAPE_ITERABLE: list,
    SHAPE_DEQUE: deque,
    SHAPE_DICT: dict,
    SHAPE_DEFAULTDICT: defaultdict,
}


def handle_container_type(
    model_field: ModelField,
    container_type: Type[Any],
    model_factory: Type["ModelFactory"],
    field_parameters: Optional[Union[Dict[Any, Any], List[Any]]] = None,
) -> Any:
    """Handles generation of container types, e.g. dict, list etc.

    recursively
    """
    is_frozen_set = container_type is frozenset
    container = container_type() if not is_frozen_set else set()
    if isinstance(container, dict) and field_parameters and isinstance(field_parameters, dict):
        key, value = list(field_parameters.items())[0]
        container[key] = value
        return container
    value = None
    if value is not None:
        if isinstance(container, (list, deque)):
            container.append(value)
        else:
            container.add(value)
            if is_frozen_set:
                return cast("set", frozenset(*container))
    return container
