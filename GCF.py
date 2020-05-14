import tkinter as tk
import random
import csv
import os
import platform
from PIL import Image, ImageTk
from io import BytesIO
import base64
import tmdbsimple as tmdb
from urllib.request import urlopen

class Film():
    id = None
    name = None
    genre = None
    releaseDate = None
    directors = []
    actors = []

    personnalGrade = None
    comments = None

    def __init__(self):
        pass
        

class gcfFrame(tk.Frame):
    def __init__(self, master=None):

        self.newReviewBtn = None
        self.editReviewBtn = None

        self.nameTxtF = None
        self.genreTxtF = None
        self.validationBtn = None

        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()
        
    def destroyAllWidgets(self):
        self.nameTxtF.destroy()
        self.genreTxtF.destroy()
        self.validationBtn.destroy()

    def createWidgets(self):
        try:
            self.destroyAllWidgets()
        except:
            print("")

        self.newReviewBtn = tk.Button(self, text = "Nouvelle Critique", command = self.newReview)
        self.newReviewBtn.grid(column = 0, row = 0)

        self.editReviewBtn = tk.Button(self, text = "Critique Existante", command = self.editReview)
        self.editReviewBtn.grid(column = 0, row = 1)


    def newReview(self):
        self.editReviewBtn.destroy()
        self.newReviewBtn.destroy()

        nameTemp = tk.StringVar()
        self.nameTxtF = tk.Entry(self, width = 15, textvariable = nameTemp)
        self.nameTxtF.grid(column = 0, row = 0)

        genreTemp = tk.StringVar()
        self.genreTxtF = tk.Entry(self, width = 15, textvariable = genreTemp)
        self.genreTxtF.grid(column = 0, row = 1)

        self.validationBtn = tk.Button(self, text = "Fini", command = self.createWidgets)
        self.validationBtn.grid(column = 0, row = 2)



    def editReview(self):
        pass

'''MODEL'''
class gfcModel():
    def __init__(self):
        self.films = []
        self.fieldnames = ['id', 'Nom', 'Genre', 'Date de sortie', 'Directeur/trice(s)', 'Acteur/trice(s)', 'Note', 'Commentaire(s)']
        self.readCSV()

    def addFilm(self, film):
        self.films.append(film)

    def getFilms(self):
        return self.films

    def getFilm(self, index):
        return self.films[index]


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
            firstRow = True
            arrayOfDic = []
            for row in csv_reader:
                if firstRow == True:
                    firstRow = False
                else:
                    arrayOfDic.append(row)
            return arrayOfDic



    def generateNewID(self, idsInMemory):
        id = 0 #Id reserve de base
        while(id in idsInMemory):
            id = random.randint(1, 100000) #Id valid selon tmdb (peu pertinent)
        return id
            
'''VIEW'''  
class gfcView():
    def __init__(self):
        self.MINCHOIX = int(1)
        self.MAXCHOIX = int(4)

    def clrscr(self):
        if platform.system() == "Linux":
            return os.system("clear")
        elif platform.system() == "Windows":
            return os.system("cls")


    def mainMenu(self):
        titre = "Bienvenue dans votre GCF (Gestionnaire de Critique de Film)"
        listeDeChoix = ["1. Nouvelle critique", "2. Chercher une critique existante", "3. Voir la liste de toutes les critiques", "4. Quitter"] 
        self.clrscr()
        print(titre, end="\n\n")
        for choix in listeDeChoix:
            print("\t" + choix)
        print("\n")

        

    def appendInput(self, UserInput):
        i = " "
        while(i != ""):
            i = input("\t-")
            if (i != ""):
                UserInput.append(i)

        return UserInput


    def newReviewV(self):
        '''
            Desole de casser le mvc en prenant du input mais le but de cette architecture
            est de simplifier par compartiment, ce qui dans une cli app peut etre dur
        '''
        inputSections = ["\tNom: ", "\tGenre: ", "\tDate de sortie: ", "\tDirecteur/rice(s): ", "\tActeur/rice(s): ", "\tVotre note: ", "\tCommentaire: "]
        titre = "\t\t\tNouvelle Critique\n\n"
        
        self.clrscr()
        print(titre)

        inputs = Film()
        
        inputs.name = input("\n\tNom: ")
        inputs.genre = input("\n\tGenre: ")
        inputs.releaseDate = input("\n\tDate de sortie: ")
        print("\n\tDirecteur/rice(s): ")
        directors = []
        inputs.directors = self.appendInput(directors)
        actors = []
        print("\n\tActeur/rice(s): ")
        inputs.actors = self.appendInput(actors)
        inputs.personnalGrade = input("\n\tVotre note: ")
        inputs.comments = input("\n\tCommentaire: ")
        input()
        
        return inputs
        

    def searchReviewV(self, csvContent):
        self.clrscr()
        id = input("Entrez le numero de la critique desirée : ") 
        '''Personne ne va chercher de film par numéro de fiche | je vais ajouter la recherche par titre si j'ai le temps'''
        for dictionary in csvContent:
            if dictionary['id'] == str(id):
                for k, v in dictionary.items():
                    print(k, v, sep=' : ')
        input('\n')
        
    def displayAllReviewsV(self, csvContent):
        self.clrscr()
        print("Voici la liste de toutes les critiques: \n")
        for dictionary in csvContent:
            print(dictionary['id'], dictionary['Nom'], sep=' : ')
        input('\n')


    def quit(self):
        self.clrscr()
        input("\n\n\t\t\tAu revoir.")
        self.clrscr()

'''CONTROLLER'''
class gfcController():
    def __init__(self):
        #self.gcfRoot = tk.Tk()
        self.model = gfcModel()
        #self.view = gfcView(self.gcfRoot)
        self.view = gfcView()
        self.idsInMemory = [0]
    

    def newReviewC(self):
        newReview = self.view.newReviewV()
        id = self.model.generateNewID(self.idsInMemory)
        newReview.id = id
        self.model.films.append(newReview)
        self.idsInMemory.append(id)
        input("\nLe numero de la critique est " + str(id))


    def searchReviewC(self):
        csvContent = self.model.readCSV()
        self.view.searchReviewV(csvContent)

    def displayAllReviewsC(self):
        csvContent = self.model.readCSV()
        self.view.displayAllReviewsV(csvContent)

    def quitC(self):
        #self.model.editCSV()
        self.view.quit()
        quit()

    def callFunc(self, choix):
        switcher = {
            '1': self.newReviewC,
            '2': self.searchReviewC,
            '3': self.displayAllReviewsC,
            '4': self.quitC
        }

        func = switcher.get(choix, lambda: input("La sélection n'est pas valide, réessayez."))
        func()

    def run(self):
        #self.gcfRoot.title("Gestionnaire de Critiques de Films")
        #self.gcfRoot.geometry("400x400")
        #self.gcfRoot.deiconify()
        #self.gcfRoot.mainloop()

        #choix = 0
        while(True):
            self.view.mainMenu()
            self.callFunc(input("Entrez votre choix: "))
        
        #self.gcfApp = gcfFrame(master=self.gcfRoot)
        #self.gcfApp.mainloop()

if __name__ == "__main__":

    c = gfcController()
    c.run()
    
