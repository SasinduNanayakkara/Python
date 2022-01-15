from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
webPage_html = response.text  # get the source code

soup = BeautifulSoup(webPage_html, "html.parser")  # beautiful soup object
all_movies = soup.find_all(name="h3", class_="title")  # get the movie titles with tags
movie_titles = [movie.getText() for movie in all_movies]  # get the movie title
movies = movie_titles[::-1]  # reverse the movie list

with open("movies.txt", mode="w") as file:  # create movies.txt file
    for movie in movies:
        file.write(f"{movie}\n")  # add the each movie title to the file
