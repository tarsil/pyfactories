from app.models import Person
from faker import Faker

from pyfactories import ModelFactory

from .persistence import AsyncPersistenceHandler, SyncPersistenceHandler

Faker.seed(5)
my_faker = Faker("en-EN")


class PersonFactory(ModelFactory):
    __model__ = Person
    __faker__ = my_faker
    __sync_persistence__ = SyncPersistenceHandler
    __async_persistence__ = AsyncPersistenceHandler
    __allow_none_optionals__ = False
    ...
