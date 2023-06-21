from typing import TypeVar

from odmantic import EmbeddedModel, Model

from pyfactories import Ignore, ModelFactory

T = TypeVar("T", Model, EmbeddedModel)


class OdmanticModelFactory(ModelFactory[T]):
    id = Ignore()
