import asyncio
from json import dumps
from re import search, sub
from bs4 import BeautifulSoup
from requests import get
from model.movie_model import MovieModel, MoviesPageModel
from scrapers.coolmovies_scrapers import getCoolMovies, getCoolMovieInfo, getCoolMoviesRandom
from scrapers.fzmovies_scraper import getFZmovies
from utils.constants import NIJA_ROCK_URL


# async def getHtmlPage(url: str = NIJA_ROCK_URL) -> BeautifulSoup:
#     response = get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     return soup


# async def getNijRockMoviesPage(movie_url: str)->str:
#     soup = await getHtmlPage(movie_url)
#     div = soup.find('div', class_='entry-header')
#     movie_id = movie_url.split('-')[-1].replace('.html', '')
#     movie_block = soup.find('div', class_='entry-content')
#     title = div.find('h1', class_='post-title entry-title').text.strip()
#     time_ago = div.find('span', class_='date meta-item tie-icon').text.strip()
#     image_url = movie_block.find('p').find('img')['src']
#     movie_downloads = [
#         {f"download-{index}": data['href']}
#         for index, data in enumerate(movie_block.find_all('a', class_='fa-fa-download'))
#     ]
#     movie_info = list(
#         map(
#             lambda data: {
#                 data.split(":")[0].strip():
#                 sub(r'[^\w\s.,!?]', '', data.split(":", 1)[1]).strip()
                
#             },
#             movie_block.find("blockquote").text.split('\n')
#         )
#     )
#     p_tag  = movie_block.find_all('p')
#     movie_detail = ""
#     for p in p_tag:
#         if not p.find_all(True) and not p.attrs:
#             movie_detail = p.text
#     movie_page = MoviesPageModel(
#         time_ago=time_ago,
#         movie_id=movie_id,
#         image_url=image_url,
#         title=title,
#         description=movie_detail,
#         movie_url=movie_url,
#         download_url=movie_downloads,
#         movie_info=movie_info,
#     )
#     return dumps(movie_page.__dict__, indent=2, ensure_ascii=False)


# async def getRecentNijRockMovies(url:str):
#     soup = await getHtmlPage(url=url)
#     div = soup.find('div', class_='slide')
#     list_of_movies: list[MovieModel] = []
#     recent_movies: list = div.find_all('div', {'class': 'tie-standard'})
#     for movie1_index, movie1 in enumerate(recent_movies):
#         image_url = recent_movies[movie1_index]['style']
#         image_url = search(r'url\((.*?)\)', image_url).group(1)
#         for movie2 in movie1.find_all('div', {'class': 'thumb-content'}):
#             time_ago = movie2.find('div', {'class': 'thumb-meta'}).text
#             description = movie2.find('div', {'class': 'thumb-desc'}).text
#             title = movie2.find('h2', {'class': 'thumb-title'}).text
#             page_url = movie2.find(
#                 'h2', {'class': 'thumb-title'}).find('a')['href']
#             movie_id = page_url.split('-')[-1].replace('.html', '')
#             movie_model = MovieModel(
#                 time_ago= time_ago,
#                 movie_id= movie_id,
#                 image_url= image_url,
#                 title= title,
#                 description= description,
#                 movie_url= page_url,
#             )
#             list_of_movies.append(movie_model.__dict__)
#     return dumps(list_of_movies, indent=2, ensure_ascii=False)



async def mainExecution():
    # await getFZmovies()
    # await getCoolMovies()
    # await getCoolMovieInfo()
    await getCoolMoviesRandom()

if __name__ == '__main__':
    asyncio.run(mainExecution())
