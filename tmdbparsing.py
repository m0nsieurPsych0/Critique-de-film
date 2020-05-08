
from PIL import Image, ImageTk
from io import BytesIO
import base64
import tmdbsimple as tmdb
from urllib.request import urlopen


tmdb.API_KEY = 'a1f4134f61b7b8a5fe7c2f84d028e282'

class Film:
    def __init__(self, id):
        self.movie = tmdb.Movies(id)
        self.info = self.movie.info()
        self.name = self.movie.title
        self.genres = self.info['genres']
        self.releaseDate = self.info['release_date']
        self.urlImage = self.info['poster_path']
        self.photo = self.printPoster()


class Query():
	def __init__(self):
		pass
		
	def printQuery(self, filmName):
		search = tmdb.Search()
		response = search.movie(query=filmName)
		number = 0
		query_dict
		for s in search.results:
   			id = s['id']
   			movie = tmdb.Movies(id)
   			response = movie.info()
   			genres = movie.genres
   			list = []
   			number += 1
   			for genre in genres:
   				for key, value in genre.items():
   					if key == 'name':
   						list.append(value)
   			joined_genre = '/'.join([str(v) for v in list])
   			print(str(number) + '-', end=' ')			
   			print(s['title'], s['id'], s['release_date'], joined_genre, sep=' | ', )


   			



if __name__ == "__main__":
	q = Query()
	#input("Entrez le nom du film a chercher :")
	q.printQuery('The Matrix')
