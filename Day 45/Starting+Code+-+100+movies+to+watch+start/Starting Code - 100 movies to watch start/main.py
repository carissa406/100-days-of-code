import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')
titles = soup.find_all("h3", class_="title")

movies = []

for title in titles:
    text = title.getText()
    movies.append(text)

#print(movies)
movies.reverse()
print(movies)

with open('Day 45/Starting+Code+-+100+movies+to+watch+start/Starting Code - 100 movies to watch start/movies.txt', 'w', encoding='utf-8') as file:
    for movie in movies:
        file.write(f'{movie}\n')