from bs4 import BeautifulSoup
from requests import get


def soupManager(url:str):
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup
