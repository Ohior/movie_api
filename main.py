# # main.py

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


from bs4 import BeautifulSoup

import requests

url = 'https://9jarocks.net/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
# # Extract data
# title = soup.title.text
# print(title)