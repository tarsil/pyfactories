from typing import TypeVar

from pydantic import BaseModel

from pyfactories.factory import ModelFactory
from pyfactories.fields import Ignore

try:
    from odmantic import EmbeddedModel, Model
except ImportError:
    Model = BaseModel
    EmbeddedModel = BaseModel


T = TypeVar("T", Model, EmbeddedModel)


class OdmanticModelFactory(ModelFactory[T]):
    id = Ignore()
