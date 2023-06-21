import dataclasses
from typing import Dict, List

import pydantic

from pyfactories import ModelFactory


@pydantic.dataclasses.dataclass
class MyPydanticDataClass:
    name: str


class MyFirstModel(pydantic.BaseModel):
    dataclass: MyPydanticDataClass


@dataclasses.dataclass()
class MyPythonDataClass:
    id: str
    complex_type: Dict[str, Dict[int, List[MyFirstModel]]]


class MySecondModel(pydantic.BaseModel):
    dataclasses: List[MyPythonDataClass]


class MyFactory(ModelFactory):
    __model__ = MySecondModel


result = MyFactory.build()
