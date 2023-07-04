from typing import TYPE_CHECKING

from pyfactories.value_generators.constrained_number import (
    generate_constrained_number,
    get_constrained_number_range,
)
from pyfactories.value_generators.primitives import create_random_integer

if TYPE_CHECKING:
    from pydantic.v1 import ConstrainedInt


def handle_constrained_int(field: "ConstrainedInt") -> int:
    """Handles 'ConstrainedInt' instances."""
    multiple_of = field.multiple_of

    minimum, maximum = get_constrained_number_range(
        gt=field.gt, ge=field.ge, lt=field.lt, le=field.le, t_type=int, multiple_of=multiple_of
    )
    return generate_constrained_number(
        minimum=minimum, maximum=maximum, multiple_of=multiple_of, method=create_random_integer
    )
