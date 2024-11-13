
from core.soup_manager import soupManager
from utils.tools import displayInFile

FZ_MOVIE_URL = "https://fzmovies.net/movieslist.php?catID=2&by=latest"


async def getFZmovies():
    soup = soupManager(FZ_MOVIE_URL)
    movies_container = soup.find_all('div', {'class': 'mainbox'})
    await displayInFile(str(movies_container[0]))
