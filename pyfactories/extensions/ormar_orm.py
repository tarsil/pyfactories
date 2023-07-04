import random
from typing import TYPE_CHECKING, Any, Union

from pydantic.v1 import BaseModel
from pydantic.v1.utils import smart_deepcopy

from pyfactories.factory import ModelFactory
from pyfactories.utils import is_pydantic_model, is_union

try:
    from ormar import Model
except ImportError:
    Model = BaseModel

if TYPE_CHECKING:
    from pydantic.v1.fields import ModelField


class OrmarModelFactory(ModelFactory[Model]):  # pragma: no cover
    @classmethod
    def get_field_value(
        cls, model_field: "ModelField", field_parameters: Union[dict, list, None] = None
    ) -> Any:
        """We need to handle here both choices and the fact that ormar sets values to be optional."""
        if not model_field.required:
            model_field = smart_deepcopy(model_field)
            model_field.required = True

        # check if this is a RelationShip field
        if (
            is_union(model_field=model_field)
            and model_field.sub_fields
            and any("PkOnly" in sf.name for sf in model_field.sub_fields)
        ):
            return cls.get_field_value(
                model_field=[
                    sf for sf in model_field.sub_fields if is_pydantic_model(sf.outer_type_)
                ][0],
                field_parameters=field_parameters,
            )
        if getattr(model_field.field_info, "choices", False):
            return random.choice(list(model_field.field_info.choices))  # type: ignore
        return super().get_field_value(model_field=model_field, field_parameters=field_parameters)
