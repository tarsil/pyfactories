from pydantic import BaseModel

from pyfactories import ModelFactory


class Pet(BaseModel):
    name: str
    age: int


class Person(BaseModel):
    name: str
    pets: list[Pet]
    age: int


class PersonFactory(ModelFactory[Person]):
    __model__ = Person


data = {
    "name": "John",
    "pets": [
        {"name": "dog"},
        {"name": "cat"},
    ],
}

person = PersonFactory.build(**data)

print(person.json(indent=2))
