from enum import Enum
from random import choice

from pydantic import BaseModel

from pyfactories import ModelFactory


class Species(str, Enum):
    CAT = "Cat"
    DOG = "Dog"


class Pet(BaseModel):
    name: str
    species: Species


class PetFactory(ModelFactory):
    __model__ = Pet

    name = lambda: choice(["Ralph", "Roxy"])  # noqa: E731
    species = lambda: choice(list(Species))  # noqa: E731
