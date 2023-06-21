from datetime import date, datetime
from enum import Enum
from typing import Any, Dict, List, Union

from pydantic import UUID4, BaseModel

from pyfactories import ModelFactory


class Species(str, Enum):
    CAT = "Cat"
    DOG = "Dog"
    PIG = "Pig"
    MONKEY = "Monkey"


class Pet(BaseModel):
    name: str
    sound: str
    species: Species


class Person(BaseModel):
    id: UUID4
    name: str
    hobbies: List[str]
    age: Union[float, int]
    birthday: Union[datetime, date]
    pets: List[Pet]
    assets: List[Dict[str, Dict[str, Any]]]


class PersonFactory(ModelFactory):
    __model__ = Person


result = PersonFactory.build()
