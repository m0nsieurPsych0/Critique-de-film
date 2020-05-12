import csv
import os

class testCSV():
	def __init__(self):
		self.fieldnames = ['id', 'Nom', 'Genre', 'Date de sortie', 'Directeur/trice(s)', 'Acteur/trice(s)', 'Note', 'Commentaire(s)']

	def writeCSV(self, dictionnaire):
	    #On lit le fichier en tant que dictionnaire
	    #On spécifie que chaque colonne vaut une clef dans le dictionnaire
	    
	    if os.path.exists('./ficheFilmDB.csv'):
	    	print("fichier exist!")
	    	with open('ficheFilmDB.csv', mode='a+') as csv_file:
	        	csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
	        	csv_writer.writerows(dictionnaire)
	    else:
	    	print("fichier n'existe pas!")
	    	with open('ficheFilmDB.csv', mode='w') as csv_file:
	            csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
	            csv_writer.writeheader()
	            csv_writer.writerows(dictionnaire)
	
	def readCSV(self):
		#On lit le fichier en tant que dictionnaire
		#On spécifie que chaque colonne vaut une clef dans le dictionnaire
		with open('ficheFilmDB.csv', mode='r') as csv_file:
			csv_reader = csv.DictReader(csv_file, fieldnames=self.fieldnames)
			line_count = 0
			arrayOfDic = []
			for row in csv_reader:
				if line_count == 0:
					line_count += 1
				else:
					arrayOfDic.append(row)
			return arrayOfDic



if __name__ == '__main__':
	dictionnaire = [{'id':'603', 'Nom':'The Matrix', 'Genre':'action/science fiction', 'Date de sortie':'1999', 'Directeur/trice(s)':'wachowski', 'Acteur/trice(s)':'Keanuuu', 'Note':'10/10', 'Commentaire(s)':'wow!'}]
	#print(dictionnaire)
	t = testCSV()
	t.writeCSV(dictionnaire)
	content = t.readCSV()
	for dictionary in content:
		for k, v in dictionary.items():
			print(k, v, sep=' : ')
		print('\n') 
	