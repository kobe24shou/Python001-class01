import requests
from bs4 import BeautifulSoup
import pandas as pd

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':user_agent}

url = "https://m.maoyan.com/films?showType=3#movie/classic"

r = requests.get(url, headers=header)

soup = BeautifulSoup(r.text, "lxml")
movie_list = soup.find_all("div", attrs={"class": "movie-info"})
movie_data = []

for movie in movie_list:
    title = movie.select('div.title')[0].get_text()
    actors = movie.select('div.actors')[0].get_text()
    show_time = movie.select('div.show-info')[0].get_text()
    movie_data.append((title, actors,show_time))

movies = pd.DataFrame(data=movie_data)
movies.to_csv('top10_movies.csv', encoding='utf-8', index=False, header=False)
print(movies)