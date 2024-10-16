from typing import Optional
from pydantic import BaseModel
from utils.types import MovieType


class MovieModel(BaseModel):
    title: str
    url: str
    image_url: str
    films:list[str]
    movie_type: Optional[MovieType] = None