
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



	def movieData(self, filmName):
		
		number = 0
		queryArray = []
		for s in self.queryTmdb(filmName):
			# sort 20 résultats maximum
			# Les films sont ordonnés par id unique sur tmdb
			# On utilise l'id pour aller chercher les infos plus précise
			movieId = s.get('id')
			movie = tmdb.Movies(movieId)
			response = movie.info()
			
			'''	On se crée un dictionnaire avec seulement les donnée pertinentes et on les combine dans une liste	'''
			dict = {}
			dict['id'] = movieId 
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
			dict['director'] = self.queryDirector(movieId)
			#directors = '/'.join([str(d) for d in dict['director']])
			# Déterminer l'acteur et combiné s'il y en a plus qu'un
			dict['actor'] = self.queryActor(movieId)
			#actors = ' / '.join([str(d) for d in dict['actor'][0:3]])
			# On imprime les 10 premiers résultat en les formatant
			print(str(number) + '-', end=' ')			
			print(dict['titre'], dict['année'], dict['genre'], dict['id'], sep=' | ')
			queryArray.append(dict)
		
		return queryArray

		
	def queryTmdb(self, searchFilm):
		# On fait une requête à l'API
		search = tmdb.Search()
		response = search.movie(query=searchFilm)
		# On retourne un dictionnaire des résultats du film recherché
		return search.results


	def queryActor(self, filmId):
		def __init__(self):
			pass	
		film = tmdb.Movies(filmId)
		response = film.info()
		credits = film.credits()
		actorList = []
		actorRole = ''
		for actors in credits['cast']:
			actorRole = actors['name'] + " as " + actors['character']
			actorList.append(actorRole)
		return actorList

	def queryDirector(self, filmId):
		def __init__(self):
			pass
		film = tmdb.Movies(filmId)
		response = film.info()
		credits = film.credits()
		directorList = []
		director = ''
		for crew in credits['crew']:
			if crew['job'] == 'Director':
				director = crew['name']
				directorList.append(director)
		return directorList	




if __name__ == "__main__":
	q = Query()
	film = input("Entrez le nom du film a chercher : ")
	resultat = q.movieData(film)
	choix = input("Entrez le numéro qui correspond au film voulu : ")
	print("Voici les informations détaillées à propos du film :")
	for key, value in resultat[int(choix) - 1].items():
		print(key, value, sep=' : ', end='\n\n')


	


#on imprime à partir des valeurs du dictionnaire
#format du dictionnaire:
#{'id': '', 'titre': '', 'année': '', 'genre': '', 'réalisateur': '', 'acteur': ''}

'''for film in queryArray:
	print(str(queryArray.index(film) + 1), end=('- '))
	for key, value in film.items():
		if key != 'id':
			print(value, end=' | ')
	print("\n")'''