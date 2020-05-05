import tkinter as tk
import random
import csv
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

class gfcModel():
    def __init__(self):
        self.films = []
        self.readCSV()

    def addFilm(self, film):
        self.films.append(film)

    def getFilms(self):
        return self.films

    def getFilm(self, index):
        return self.films[index]

    def readCSV(self):
        csv_file = open('./FichesFilms.csv')
        csv_reader = csv.reader(csv_file, delimiter=',')
        #line_count = 0
        for row in csv_reader:
            newFilm = Film()
            newFilm.id = row[0]
            newFilm.name = row[1]
            newFilm.genre = row[2]
            newFilm.releaseDate = row[3]
            newFilm.directors = row[4]
            newFilm.actors = row[5]
            newFilm.personnalGrade = row[6]
            newFilm.comments = row[7]
            self.films.append(newFilm)
        
        csv_file.close()

    def editCSV(self):
        csv_file = open('./FichesFilms.csv', "w")
        csv_writer = csv.writer(csv_file, delimiter=',')
        for film in self.films:
            csv_writer.writerow([film.id] + [film.name] + [film.genre] + [film.releaseDate] + [film.directors] + [film.actors] + [film.personnalGrade] + [film.comments])

        csv_file.close()
        
    def generateNewID(self, idsInMemory):
        id = 0 #Id reserve de base
        while(id in idsInMemory):
            id = random.randint(1, 100000) #Id valid selon tmdb (peu pertinent)
        return id
            

    
class gfcView():
    def __init__(self):
        #self.frame = gcfFrame(master=master)
        pass
        

    def mainMenu(self):
        print("Bienvenue dans votre GCF (Gestionnaire de Critiques de Films)")
        print("        1. Nouvelle critique")
        print("        2. Chercher une critique existante")
        print("        3. Voir la liste de toutes les critiques")
        print("        4.Quitter")
        print()
        print("Entrez votre choix")
        reponse = input()
        print()
        return reponse

    def newReviewV(self):
        #Desole de casser le mvc en prenant du input mais le but de cette architecture est de simplifier par compartiment, ce qui dans une cli app peut etre dur
        inputs = Film()
        print("Nouvelle Critique")
        print("         Nom: ")
        inputs.name = input()
        print("         Genre: ")
        inputs.genre = input()
        print("         Date de sortie: ")
        inputs.releaseDate = input()
        print("         Directeur/rice(s): ")
        directors = []
        d = " "
        while(d != ""):
            d = input()
            if (d != ""):
                directors.append(input())

        inputs.directors = directors
        print("         Acteur/rice(s): ")
        actors = []
        a = " "
        while(a != ""):
            a = input()
            if(a != ""):
                actors.append(input())

        inputs.actors = actors
        print("         Votre note: ")
        inputs.personnalGrade = input()
        print("         Commentaire: ")
        inputs.comments = input()

        return inputs
        

    def searchReviewV(self, films):
        print("Entrez le numero de la critique desiree: ")
        id = input()
        for f in films:
            if f.id == id:
                print("    Genre: " + f.genre)
                print("    Date de sortie: " + f.releaseDate)
                print("    Directeur/trice(s): " + f.directors)
                print("    Acteur/trice(s): " + f.actors)
                print("    Note: " + f.personnalGrade) 
                print("    Commentaire(s): " + f.comments)
                input()
                break

    def displayAllReviewsV(self, films):
        print("Voici toutes les critiques")
        for f in films:
            print(f.id + ": " + f.name)
        input()


    def quit(self):
        print("Au revoir.")

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
        print("Le numero de la critique est " + id)
        input()

    def searchReviewC(self):
        self.view.searchReviewV(self.model.films)

    def displayAllReviewsC(self):
        self.view.displayAllReviewsV(self.model.films)

    def quitC(self):
        self.model.editCSV()
        self.view.quit()

    def callFunc(self, choice):
        switcher = {
            '1': self.newReviewC,
            '2': self.searchReviewC,
            '3': self.displayAllReviewsC,
            '4': self.quitC
        }

        func = switcher.get(choice, lambda: "Numero invalide")
        func()

    def run(self):
        #self.gcfRoot.title("Gestionnaire de Critiques de Films")
        #self.gcfRoot.geometry("400x400")
        #self.gcfRoot.deiconify()
        #self.gcfRoot.mainloop()

        choice = ''
        while(choice != '4'):
            choice = self.view.mainMenu()
            self.callFunc(choice)
        
        #self.gcfApp = gcfFrame(master=self.gcfRoot)
        #self.gcfApp.mainloop()

if __name__ == "__main__":

    c = gfcController()
    c.run()
    
