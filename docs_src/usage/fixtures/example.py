from datetime import date, datetime
from typing import List, Union

from pydantic import UUID4, BaseModel

from pyfactories import ModelFactory
from pyfactories.plugins.pytest_plugin import register_fixture


class Person(BaseModel):
    id: UUID4
    name: str
    hobbies: List[str]
    age: Union[float, int]
    birthday: Union[datetime, date]


@register_fixture
class PersonFactory(ModelFactory):
    """A person factory"""

    __model__ = Person


@register_fixture(scope="session", autouse=True, name="cool_guy_factory")
class AnotherPersonFactory(ModelFactory):
    """A cool guy factory"""

    __model__ = Person


def test_person_factory(person_factory: PersonFactory) -> None:
    person = person_factory.build()
    assert isinstance(person, Person)


def test_cool_guy_factory(cool_guy_factory: AnotherPersonFactory) -> None:
    cool_guy = cool_guy_factory.build()
    assert isinstance(cool_guy, Person)
