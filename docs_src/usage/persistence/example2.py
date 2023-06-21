from typing import List, TypeVar

from pydantic import BaseModel

from pyfactories import AsyncPersistenceProtocol, ModelFactory, SyncPersistenceProtocol

T = TypeVar("T", bound=BaseModel)


class SyncPersistenceHandler(SyncPersistenceProtocol[T]):
    def save(self, data: T) -> T:
        ...  # do stuff

    def save_many(self, data: List[T]) -> List[T]:
        ...  # do stuff


class AsyncPersistenceHandler(AsyncPersistenceProtocol[T]):
    async def save(self, data: T) -> T:
        ...  # do stuff

    async def save_many(self, data: List[T]) -> List[T]:
        ...  # do stuff


class BaseModelFactory(ModelFactory):
    __sync_persistence__ = SyncPersistenceHandler
    __async_persistence__ = AsyncPersistenceHandler


class PersonFactory(BaseModelFactory):
    ...
