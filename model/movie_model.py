from dataclasses import dataclass

from utils.constants import getMovieCredit

@dataclass
class MoviesPageModel:
    time_ago:str
    movie_id: str
    image_url:str
    title: str
    description: str
    movie_url: str
    download_url: list[dict]
    movie_info:list[dict]
    
    def __post_init__(self):
        self.__credits__ = getMovieCredit(self.movie_url)


@dataclass
class MovieModel:
    time_ago:str
    movie_id: str
    image_url:str
    title: str
    description: str
    movie_url: str

    def __post_init__(self):
        self.__credits__ = getMovieCredit(self.movie_url)
