from datetime import date, datetime
from enum import Enum
from random import choice
from typing import Any, Dict, List, Union

from pydantic import UUID4, BaseModel

from pyfactories import ModelFactory


class Species(str, Enum):
    CAT = "Cat"
    DOG = "Dog"


class Pet(BaseModel):
    name: str
    species: Species


class Person(BaseModel):
    id: UUID4
    name: str
    hobbies: List[str]
    age: Union[float, int]
    birthday: Union[datetime, date]
    pets: List[Pet]
    assets: List[Dict[str, Dict[str, Any]]]


class PetFactory(ModelFactory):
    __model__ = Pet
    __auto_register__ = True

    name = lambda: choice(["Ralph", "Roxy"])  # noqa: E731
    species = Species.DOG


class PersonFactory(ModelFactory):
    __model__ = Person
