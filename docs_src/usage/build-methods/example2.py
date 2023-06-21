from pydantic import BaseModel

from pyfactories import ModelFactory


class Person(BaseModel):
    ...


class PersonFactory(ModelFactory):
    __model__ = Person


PersonFactory.build(id=5)  # Raises a validation error

result = PersonFactory.build(factory_use_construct=True, id=5)  # Build a Person with invalid id
