
import tmdbsimple as tmdb
import os
import platform

tmdb.API_KEY = 'a1f4134f61b7b8a5fe7c2f84d028e282'

class Query():
	def __init__(self):
		pass


	def clrscr(self):
		if platform.system() == "Linux":
			return os.system("clear")
		elif platform.system() == "Windows":
			return os.system("cls")
	
	def movieData(self, filmName):
		number = 0
		queryArray = []
		
		for number, s in enumerate(self.queryTmdb(filmName), start=1):
			'''
			 		sort 20 résultats maximum
			 		Les films sont ordonnés par id unique sur tmdb
			 		On utilise l'id pour aller chercher les infos plus précise
			'''
			movieId = s.get('id')
			movie = tmdb.Movies(movieId)
			response = movie.info()
			
			'''	On se crée un dictionnaireionnaire avec seulement les donnée pertinentes et on les combine dans une liste	'''
			dictionnaire = {}
			dictionnaire['Id'] = movieId 
			dictionnaire['Nom'] = s.get('title')
			dictionnaire['Date de sortie'] = s.get('release_date')
			

			# Déterminer le genre et combiné s'il y en a plus qu'un
			dictionnaire['Genre'] = self.queryGenre(movie)

			# Déterminer le réalisateur et combiné s'il y en a plus qu'un
			dictionnaire['Réalisateur/trice(s)'] = self.queryDirector(movie)
			
			# Déterminer l'acteur et combiné s'il y en a plus qu'un
			dictionnaire['Acteur/trice(s)'] = self.queryActor(movie)

			print(str(number) + '-', end=' ')			
			print(dictionnaire['Nom'], dictionnaire['Date de sortie'], dictionnaire['Genre'], dictionnaire['Id'], dictionnaire['Réalisateur/trice(s)'], sep=' | ')
			queryArray.append(dictionnaire)
		return queryArray

		
	def queryTmdb(self, searchFilm):
		# On fait une requête à l'API
		search = tmdb.Search()
		response = search.movie(query=searchFilm)
		# On retourne un dictionnaireionnaire des résultats du film recherché
		return search.results


	def queryGenre(self, movie):
		genres = movie.genres
		genreList = []
		for genre in genres:
			for key, value in genre.items():
				if key == 'name':
					genreList.append(value)
		genresList = '/'.join([str(g) for g in genreList])
		return genresList
		
	def queryActor(self, movie):	
		credits = movie.credits()
		actorList = []
		actorRole = ''
		for actors in credits['cast']:
			actorRole = actors['name'] + " as " + actors['character']
			actorList.append(actorRole)
		actorList = '/'.join([str(a) for a in actorList])
		return actorList

	def queryDirector(self, movie):
		credits = movie.credits()
		directorList = []
		director = ''
		for crew in credits['crew']:
			if crew['job'] == 'Director':
				director = crew['name']
				directorList.append(director)
		directorList = '/'.join([str(d) for d in directorList])
		return directorList	

	def queryChoice(self):
		choix = 0
		while choix <= 0:
			self.clrscr()
			"\t\t\tNouvelle Critique\n\n"
			film = input("Entrez le nom du film à chercher : ")
			resultat = self.movieData(film)
			print("\n*Si votre choix n'est pas affiché entrez \'0\' pour faire une autre recherche\n")
			choix = int(input("Entrez le numéro qui correspond au film voulu : "))
			if choix > len(resultat):
				print("Erreur, veuillez réessayer.")
				choix = 0
				self.clrscr()
		self.clrscr()
		self.printChoice(resultat[choix - 1])


	def printChoice(self, resultatFormate):
		#À changer pour l'entré d'information automatique
		print("Voici les informations détaillées à propos du film :")
		for key, value in resultatFormate.items():
			
			if key == 'Acteur/trice(s)':
				print(key, value.replace('/', '\n\t\t\t'), sep=' :\n\t\t\t', end='\n\n')
				
			else:	
				print(key, value, sep=' : \n\t\t\t', end='\n\n')

		


if __name__ == "__main__":
	q = Query()
	q.queryChoice()
