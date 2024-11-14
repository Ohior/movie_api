from pprint import pprint
from random import randrange
from core.soup_manager import soupManager
from model.movie_model_v1 import Movie, MovieDownload, MovieInfo
from utils.tools import displayInFile

_COOLMOVIES_HOLLYWOOD = "https://www.coolmoviez.int.in/movielist/13/Hollywood_movies/default/2.html"


def _movieListPageUrl(page_num: int) -> str:
    return f"https://www.coolmoviez.int.in/movielist/13/Hollywood_movies/default/{page_num}.html"


async def _getDownload(download_url: str) -> MovieDownload:
    soup = soupManager(download_url)
    download_link = (
        soup.find('div', {'class': 'fshow'})
        .find('a', {'class': 'dwnLink'})['href']
    )
    soup = soupManager(download_link)
    download_link = (
        soup.find('div', {'class': 'fshow'})
        .find('a', {'class': 'dwnLink', 'rel': 'nofollow'})['href']
    )
    d_info = soup.find('div', {'class': 'list'}).find(
        'div', {'class': 'fshow'})
    size = ""
    for d in d_info.find_all('div', {'class': 'M2'}):
        if d.find('b').text == "File Size:":
            size = d.find('font').text
            break
    return MovieDownload(
        url=[download_link.replace('server_3', f'server_{
                                   i}') for i in range(1, 4)],
        size=size
    )


async def getCoolMovies(url: str = _movieListPageUrl(1)) -> list[dict]:
    soup = soupManager(url)
    movies_container = soup.find_all('div', {'class': 'list'})
    movies_model: list[dict] = []
    for movie in movies_container[0].find_all('div', {'class': 'fl'}):
        movie_model = Movie(
            title=movie.find('a', {'class': 'fileName'})['title'],
            movie_page_url=movie.find('a', {'class': 'fileName'})['href'],
            image_url=movie.find('img')['src'],
            quality_type=movie.find('span').text.strip('Source:').strip()
        )
        movies_model.append(movie_model.toDict())
    return movies_model


async def getCoolMoviesRandom(
        url: str = _movieListPageUrl(randrange(1,10))
) -> list[dict]:
    soup = soupManager(url)
    movies_container = soup.find_all('div', {'class': 'list'})
    movies_model: list[dict] = []
    for movie in movies_container[0].find_all('div', {'class': 'fl'}):
        movie_model = Movie(
            title=movie.find('a', {'class': 'fileName'})['title'],
            movie_page_url=movie.find('a', {'class': 'fileName'})['href'],
            image_url=movie.find('img')['src'],
            quality_type=movie.find('span').text.strip('Source:').strip()
        )
        movies_model.append(movie_model.toDict())
    return movies_model


async def getCoolMovieInfo(
        url: str = "https://www.coolmoviez.int.in/movie/15903/Gladiator_ii_(2024)_english_movie.html"
) -> dict:
    soup = soupManager(url)
    title = soup.find("h1").text.strip()
    image_url = soup.find('p', {'class': 'showimage'}).find(
        'img', {'class': 'absmiddle'})['src']
    category = soup.find(
        'div', {'class': 'description'}).find('i').text.strip()
    m1s = soup.find_all('div', {'class': 'M1'})
    m2s = soup.find_all('div', {'class': 'M2'})
    casts: list[str] = []
    description = ""
    release_data = ""
    format_quality = ""
    for m1 in m1s:
        cast = m1.find('b').text.strip()
        match cast:
            case "Starcast:":
                for c in m1.find_all('i'):
                    casts.append(c.text.strip())
            case "Description:":
                description = m1.find("i").text.strip()
            case "Release Date:":
                release_data = m1.find("i").text.strip()
            case "Quality:":
                format_quality = m1.text.strip('Quality:').strip()
    genre: list[str] = []
    duration = ""
    for m2 in m2s:
        try:
            cast = m2.find('b').text.strip()
            match cast:
                case "Genre:":
                    for c in m2.find_all('i'):
                        genre.append(c.text.strip())
                case "Duration:":
                    duration = m2.find("i").text.strip()
        except AttributeError:
            continue
    download_url = (
        soup.find('div', {'class': 'list'})
        .find('a', {'class': 'fileName'})['href']
    )
    movie_info = MovieInfo(
        image_url=image_url,
        title=title,
        quality_type=format_quality,
        movie_category=category,
        casts=casts,
        description=description,
        genres=genre,
        release_date=release_data,
        duration=duration,
        download=await _getDownload(download_url),
        movie_page_url=url
    )
    return movie_info.toDict()
