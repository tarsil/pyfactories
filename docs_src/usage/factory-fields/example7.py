from uuid import UUID

from pydantic import BaseModel

from pyfactories import ModelFactory, Require


class ArticleProxy(BaseModel):
    article_id: UUID
    ...


class ArticleProxyFactory(ModelFactory):
    __model__ = ArticleProxy

    article_id = Require()
