
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
		
		#Légende
		#print("\n\t Nom \t | \t Date de sortie \t | \t Genre \t | \t Id \t | \t Réalisateur/trice(s)\n")
		
		for number, s in enumerate(self.queryTmdb(filmName), start=1):
			'''
			 		sort 20 résultats maximum
			 		Les films sont ordonnés par id unique sur tmdb
			 		On utilise l'id pour aller chercher les infos plus précise
			'''
			movieId = s.get('id')
			movie = tmdb.Movies(movieId)
			response = movie.info()
			
			'''	On se crée un dictionnaire avec seulement les donnée pertinentes et on les combine dans une liste	'''
			dict = {}
			dict['Id'] = movieId 
			dict['Nom'] = s.get('title')
			dict['Date de sortie'] = s.get('release_date')
			list = []

			# Déterminer le genre et combiné s'il y en a plus qu'un
			genres = movie.genres
			for genre in genres:
				for key, value in genre.items():
					if key == 'name':
						list.append(value)
			dict['Genre'] = '/'.join([str(v) for v in list])

			# Déterminer le réalisateur et combiné s'il y en a plus qu'un
			dict['Réalisateur/trice(s)'] = self.queryDirector(movie)
			directors = '/'.join([str(d) for d in dict['Réalisateur/trice(s)']])
			dict['Réalisateur/trice(s)'] = directors
			# Déterminer l'acteur et combiné s'il y en a plus qu'un
			dict['Acteur/trice(s)'] = self.queryActor(movie)
			actors = ' / '.join([str(d) for d in dict['Acteur/trice(s)'][0:10]])
			dict['Acteur/trice(s)'] = actors
			# On imprime les 10 premiers résultat en les formatant
			
			print(str(number) + '-', end=' ')			
			print(dict['Nom'], dict['Date de sortie'], dict['Genre'], dict['Id'], directors, sep=' | ')
			queryArray.append(dict)
		return queryArray

		
	def queryTmdb(self, searchFilm):
		# On fait une requête à l'API
		search = tmdb.Search()
		response = search.movie(query=searchFilm)
		# On retourne un dictionnaire des résultats du film recherché
		return search.results


	def queryActor(self, movie):	
		credits = movie.credits()
		actorList = []
		actorRole = ''
		for actors in credits['cast']:
			actorRole = actors['name'] + " as " + actors['character']
			actorList.append(actorRole)
		return actorList

	def queryDirector(self, movie):
		credits = movie.credits()
		directorList = []
		director = ''
		for crew in credits['crew']:
			if crew['job'] == 'Director':
				director = crew['name']
				directorList.append(director)
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
	'''	
	def formatChoice(self, resultat):
		# resultatFormate = {}
		# resultatFormate['Id'] = resultat['Id']
		# resultatFormate['Nom'] = resultat['Nom']
		# resultatFormate['Date de sortie'] = 
		for key, value in resultat.items():
			if key == 'Réalisateur/trice(s)':
				print(key, end=' : \n')
				for v in value:
					print('\t\t\t' + v)
				print('\n\n')
			elif key == 'Acteur/trice(s)':
				print(key, end=' : \n')
				for v in value[0:5]:
					print('\t\t\t' + v)
				print('\n\n')
			else:	
				print(key, value, sep=' : \n\t\t\t', end='\n\n')
	'''

	def printChoice(self, resultatFormate):
		#À changer pour l'entré d'information automatique
		print("Voici les informations détaillées à propos du film :")
		for key, value in resultatFormate.items():
			
			if key == 'Acteur/trice(s)':
				print(key, value.replace('/', '\n\t\t\t'), sep=':\n\t\t\t', end='\n\n')
				
			else:	
				print(key, value, sep=' : \n\t\t\t', end='\n\n')

		


if __name__ == "__main__":
	q = Query()
	q.queryChoice()

	


#on imprime à partir des valeurs du dictionnaire
#format du dictionnaire:
#{'id': '', 'titre': '', 'année': '', 'genre': '', 'réalisateur': '', 'acteur': ''}

'''for film in queryArray:
	print(str(queryArray.index(film) + 1), end=('- '))
	for key, value in film.items():
		if key != 'id':
			print(value, end=' | ')
	print("\n")'''