
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

	def queryTmdb(self, searchTerm, type):
		# On fait une requête à l'API
		search = tmdb.Search()
	
		if type == "film":		
			response = search.movie(query=searchTerm)
		elif type == person:
			response = search.person(query=searchTerm)

		return search.results

	def movieData(self, filmName):
		
		number = 0
		queryArray = []

		for s in self.queryTmdb(filmName, "film"):
			# sort 20 résultats maximum
			# Les films sont ordonnés par id unique sur tmdb
			# On utilise l'id pour aller chercher les infos plus précise
			id = s.get('id')
			movie = tmdb.Movies(id)
			response = movie.info()
			
			'''	On se crée un dictionnaire avec seulement les donnée pertinentes et on les combine dans une liste	'''
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
			
			# On imprime les 10 premiers résultat en les formatant
			print(str(number) + '-', end=' ')			
			print(dict['titre'], dict['année'], dict['genre'], dict['id'], sep=' | ')
			queryArray.append(dict)

		

	def queryActor(self, filmId):
		def __init__(self):
			pass	
		film = tmdb.Movies(filmId)
		response = film.info()
		credits = film.credits()
		for actors in credits['cast'][0:10]:
			print( actors['name'], actors['character'], sep=' as ')

	def queryDirector(self, filmId):
		def __init__(self):
			pass
		film = tmdb.Movies(filmId)
		response = film.info()
		credits = film.credits()
		for crew in credits['crew']:
			if crew['job'] == 'Director':
				print( crew['name'], crew['job'], sep=' as ')
					




if __name__ == "__main__":
	q = Query()
	#film = input("Entrez le nom du film a chercher :")
	#q.movieData(film)
	#q.queryActor("matrix")
	#search = tmdb.Search()
	#response = search.movie(query='The Matrix')
	#id = search.results[0].get('id')
	q.queryActor(603)
	q.queryDirector(603)


	


#on imprime à partir des valeurs du dictionnaire
#format du dictionnaire:
#{'id': '', 'titre': '', 'année': '', 'genre': '', 'réalisateur': '', 'acteur': ''}

'''for film in queryArray:
	print(str(queryArray.index(film) + 1), end=('- '))
	for key, value in film.items():
		if key != 'id':
			print(value, end=' | ')
	print("\n")'''