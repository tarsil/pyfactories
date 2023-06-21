from datetime import date, datetime
from enum import Enum
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union

from pydantic import UUID4, BaseModel

from pyfactories import ModelFactory


class Species(str, Enum):
    CAT = "Cat"
    DOG = "Dog"


class PetBase(BaseModel):
    name: str
    species: Species


class Pet(PetBase):
    id: UUID4


class PetCreate(PetBase):
    pass


class PetUpdate(PetBase):
    pass


class PersonBase(BaseModel):
    name: str
    hobbies: List[str]
    age: Union[float, int]
    birthday: Union[datetime, date]
    pets: List[Pet]
    assets: List[Dict[str, Dict[str, Any]]]


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    id: UUID4


class PersonUpdate(PersonBase):
    pass


def test_factory():
    class PersonFactory(ModelFactory):
        __model__ = Person

    person = PersonFactory.build()

    assert person.pets != []


ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BUILDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(
        self,
        model: ModelType = None,
        create_schema: Optional[CreateSchemaType] = None,
        update_schema: Optional[UpdateSchemaType] = None,
    ):
        self.model = model
        self.create_model = create_schema
        self.update_model = update_schema

    def build_object(self) -> ModelType:
        object_Factory = ModelFactory.create_factory(self.model)
        return object_Factory.build()

    def build_create_object(self) -> CreateSchemaType:
        object_Factory = ModelFactory.create_factory(self.create_model)
        return object_Factory.build()

    def build_update_object(self) -> UpdateSchemaType:
        object_Factory = ModelFactory.create_factory(self.update_model)
        return object_Factory.build()


class BUILDPet(BUILDBase[Pet, PetCreate, PetUpdate]):
    def build_object(self) -> Pet:
        object_Factory = ModelFactory.create_factory(self.model, name="Fido")
        return object_Factory.build()

    def build_create_object(self) -> PetCreate:
        object_Factory = ModelFactory.create_factory(self.create_model, name="Rover")
        return object_Factory.build()

    def build_update_object(self) -> PetUpdate:
        object_Factory = ModelFactory.create_factory(self.update_model, name="Spot")
        return object_Factory.build()


def test_factory_create():
    person_factory = BUILDBase(Person, PersonCreate, PersonUpdate)

    pet_factory = BUILDPet(Pet, PetCreate, PetUpdate)

    create_person = person_factory.build_create_object()
    update_person = person_factory.build_update_object()

    pet = pet_factory.build_object()
    create_pet = pet_factory.build_create_object()
    update_pet = pet_factory.build_update_object()

    assert create_person is not None
    assert update_person is not None

    assert pet.name == "Fido"
    assert create_pet.name == "Rover"
    assert update_pet.name == "Spot"
