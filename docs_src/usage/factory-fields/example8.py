from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import UUID4, BaseModel

from pyfactories import Fixture, ModelFactory
from pyfactories.plugins.pytest_plugin import register_fixture


class Person(BaseModel):
    id: UUID4
    name: str
    hobbies: Optional[List[str]]
    nicks: List[str]
    age: Union[float, int]
    birthday: Union[datetime, date]


class ClassRoom(BaseModel):
    teacher: Person
    pupils: List[Person]


@register_fixture(name="my_fixture")
class PersonFactory(ModelFactory):
    __model__ = Person


class ClassRoomFactory(ModelFactory):
    teacher = Fixture(PersonFactory, name="Jenny Osterman")
    pupils = Fixture(PersonFactory, size=20)
