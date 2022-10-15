import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")
movie_tag = soup.find_all(name="h3", class_="title")

movie_list = [movie.getText() for movie in movie_tag]

with open("movies.txt", "a", encoding="utf-8") as movies:
    for n in range(len(movie_list)):
        i = n + 1
        movies.write(f"{movie_list[-i]}\n")
