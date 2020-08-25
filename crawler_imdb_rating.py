import time
import requests

from bs4 import BeautifulSoup



def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
	t_end = time.time() + 60 * 2
	while time.time() < t_end:
        	for link in s.findAll('td', class_=['titleColumn','ratingColumn imdbRating']):
        	    tet = link.select('td > a')
        	    print(tet)
		    tet_2 = link.select('td > strong')
        	    print(tet_2)

web(1,'https://www.imdb.com/chart/top-english-movies')


