import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")
title_html = soup.find_all(class_="title", name="h3")
titles = [item.text for item in title_html]
titles = titles[::-1]

for title in titles:
    try:
        with open("movies.txt", "r") as file:
            with open("movies.txt", "a", encoding="utf-8") as file_data:
                file_data.write(f"{title}\n")
    except:
        with open("movies.txt", "w", encoding="utf-8") as file:
            file.write(f"{title}\n")