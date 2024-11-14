from dataclasses import dataclass, asdict
from typing import Any
from utils.constants import getMovieCredit


@dataclass
class MovieDownload:
    url: list[str]
    size: str

    def toDict(self)->dict[str, Any]:
        return asdict(self)
    


@dataclass
class Movie:
    image_url: str
    title: str
    quality_type: str
    movie_page_url: str

    def __post_init__(self):
        self.__credits__ = getMovieCredit(self.movie_page_url)
    
    def toDict(self)->dict[str, Any]:
        return asdict(self)


@dataclass
class MovieInfo:
    image_url: str
    title: str
    quality_type: str
    movie_category: str
    casts: list[str]
    description: str
    genres: list[str]
    release_date: str
    duration: str
    download: MovieDownload
    movie_page_url: str = ""

    def __post_init__(self):
        self.__credits__ = getMovieCredit(self.movie_page_url)
    
    def toDict(self)->dict[str, Any]:
        return asdict(self)
