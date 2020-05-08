
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
	# self.photo = self.printPoster()


class Query():

	def __init__(self):
		pass

	def printQuery(self, filmName):
		search = tmdb.Search()
		response = search.movie(query=filmName)
		number = 0
		queryArray = []
		# dict = {'id': '', 'titre': '', 'année': '', 'genre': '', 'réalisateur':
		# '', 'acteur': ''}
		for s in search.results[0:5]:
			#Les films sont ordonnés par id unique sur tmdb
			id = s.get('id')
			movie = tmdb.Movies(id)
			response = movie.info()
			
			dict = {}
			dict['id'] = id 
			dict['titre'] = s.get('title')
			dict['année'] = s.get('release_date')
			list = []
			number += 1
			# Déterminer le genre et combiné s'il y en a plus qu'un
			genres = movie.genres
			for genre in genres:
				for key, value in genre.items():
					if key == 'name':
						list.append(value)
			dict['genre'] = '/'.join([str(v) for v in list])
			# Déterminer le réalisateur et combiné s'il y en a plus qu'un
			# Déterminer l'acteur et combiné s'il y en a plus qu'un
			
			#print(str(number) + '-', end=' ')			
			# print(s['title'], s['id'], s['release_date'], dict['genre'], sep=' | ', )
			#print(dict['titre'], dict['année'], dict['genre'], sep=' | ')
			queryArray.append(dict)
		#on imprime 
		for film in queryArray:
			print(str(queryArray.index(film) + 1), end=('- '))
			for key, value in film.items():
				if key != 'id':
					print(value, end=' | ')
			print("\n")



if __name__ == "__main__":
	q = Query()
	# input("Entrez le nom du film a chercher :")
	q.printQuery('fight club')
