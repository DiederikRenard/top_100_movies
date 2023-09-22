import requests
from bs4 import BeautifulSoup
import random


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
web_data = response.text

title_list = []
web_soup = BeautifulSoup(web_data, "html.parser")
title = web_soup.find_all(name="h3", class_="title")

for tag in title:
    movie = tag.getText()
    title_list.append(movie)
title_list.reverse()
with open("movies_to_watch.txt", "w", encoding="utf-8") as file:
    for line in title_list:
        file.write(f"{line}\n")


def pick_movie():
    with open("movies_to_watch.txt") as file:
        movies = file.readlines()
        print(random.choice(movies))


pick_movie()
