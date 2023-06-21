from datetime import datetime, timedelta
from random import randint

from pydantic import BaseModel

from pyfactories import ModelFactory, PostGenerated


def add_timedelta(name: str, values: dict, *args, **kwds):
    delta = timedelta(days=randint(0, 12), seconds=randint(13, 13000))
    return values["from_dt"] + delta


class MyModel(BaseModel):
    from_dt: datetime
    to_dt: datetime


class MyFactory(ModelFactory):
    __model__ = MyModel

    to_dt = PostGenerated(add_timedelta)
