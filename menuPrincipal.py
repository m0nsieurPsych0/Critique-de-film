#Python program pour gérer des fiches de visionnement de film

#Utiliser L'API de themoviedatabase.org
#https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>






'''
Constitution d'une fiche:

nom*
catégorie*
année*
réalisateur
acteurs-actrices principaux(3 max)
notes 0-10
commentaires

* info minimale obligatoire


Fonctionnalitées voulues:

1- recherche sur les fiches
	-suprimer
	-modifier
	-ajouter

	-recherche par contenu (lorsqu'on fait une recherche, on vérifie tout les champs et si on ne trouve rien on vérifie les commentaires)

2- utiliser un système de catégorisation rigide (API)
	-sélection de catégorie par proposition en relation avec l'existance d'un film


3- afficher les fiches à l'écran 
	-forme de liste
	-forme de panneau (flèches (droite/gauche)

'''


import platform
import os


class MainMenu():

	def __init__(self):
		self.MINCHOIX = int(1)
		self.MAXCHOIX = int(4)

	def clrscr(self):
		if platform.system() == "Linux":
			return os.system("clear")
		elif platform.system() == "Windows":
			return os.system("cls")


	def mainMenu(self):
		titre = "Bienvenue à votre programme de critique de film!"
		listeDeChoix = ["1. Nouvelle critique", "2. Chercher une critique existante", "3. Voir la liste de toutes les critiques", "4. Quitter"] 
		self.clrscr()
		print(titre, end="\n\n")
		for choix in listeDeChoix:
			print("\t" + choix)
		print("\n")




	def userInput(self):
		choix = input("Entrez votre choix: ")
		choix = int(choix)

		if choix < self.MINCHOIX or choix > self.MAXCHOIX:
			print("La sélection n'est pas valide, réessayez.")
			input()
			return
		else:
			return choix 





if __name__ == '__main__':
	unchoix = 0	
	while unchoix != 4:
		mainMenu = MainMenu()
		mainMenu.mainMenu()
		unchoix = mainMenu.userInput()
		print("Vous avez choisi: " + str(unchoix))
		input()

