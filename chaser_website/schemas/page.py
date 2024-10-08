from typing import Generic, TypeVar

from pydantic import BaseModel

from chaser_website.schemas.project import ProjectOut

T = TypeVar('T')


class Page(Generic[T], BaseModel):
    items: list[T]
    limit: int
    offset: int
    total: int