import pandas
import pandas as pd
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
soup = BeautifulSoup(source.text,'html.parser')

movies = soup.find('tbody', class_='lister-list').find_all('tr')

rank = [movie.find('td', class_ ='titleColumn').get_text(strip=True).split('.') [0] for movie in movies]

names = [movie.find('td', class_ ='titleColumn').get_text(strip=True) for movie in movies]

ratings = [movie.find('td', class_ ='ratingColumn imdbRating').strong.get_text(strip=True) for movie in movies]

years = [movie.find('td', class_ ='titleColumn').span.get_text(strip=True).strip('()') for movie in movies]


#print(rank)
#print(names)
#print(ratings)
#print(years)


    {  'Rank': rank,
    'Names': names,
    'Year': year,
    'Ratings': ratings,
    }

top_movies = pandas.DataFrame(s,
)

print(top_movies)

#top_movies.to_csv('Top_Movies.csv')
