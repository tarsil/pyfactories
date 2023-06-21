from pydantic import BaseModel

from pyfactories import ModelFactory


class Person(BaseModel):
    ...


class PersonFactory(ModelFactory):
    __model__ = Person


single_result = PersonFactory.build()  # a single Person instance

batch_result = PersonFactory.batch(size=5)  # list[Person, Person, Person, Person, Person]
