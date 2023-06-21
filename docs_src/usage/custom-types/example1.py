from typing import Any

from pyfactories import ModelFactory


class CustomFactory(ModelFactory[Any]):
    """Tweak the ModelFactory to add our custom mocks."""

    @classmethod
    def get_mock_value(cls, field_type: Any) -> Any:
        """Add our custom mock value."""
        if str(field_type) == "my_super_rare_datetime_field":
            return cls.get_faker().date_time_between()

        return super().get_mock_value(field_type)
