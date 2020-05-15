import csv
import os
import platform
import tmdbParsing as tmdb

class Film():
    def __init__(self):
        pass
        

'''MODEL'''
class gfcModel():
    def __init__(self):
        self.fieldnames = ['Id', 'Nom', 'Genre', 'Date de sortie', 'Réalisateur/trice(s)', 'Acteur/trice(s)', 'Note', 'Commentaire(s)']
        self.warning_and_info = "Si vous modifiez le fichier avec un autre programme comme excel, le fichier pourrait être corrompu. Assurez-vous de faire des modifications manuellement que si vous utiliser un éditeur de texte."


        '''
        Chaque ligne est lu en tant que dictionnaire.
        Chaque colonne vaut une clef dans le dictionnaire spécifié avec la list "fieldnames"
        '''

    def overWriteCSV(self, dictionnaire):
        with open('ficheFilmDB.csv', mode='w') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(dictionnaire)


    def writeCSV(self, dictionnaire):        
        if os.path.exists('./ficheFilmDB.csv'):
            with open('ficheFilmDB.csv', mode='a+') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
                csv_writer.writerow(dictionnaire)
        else:
            with open('ficheFilmDB.csv', mode='w') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
                csv_writer.writeheader()
                csv_writer.writerow(dictionnaire)
    
    def readCSV(self):
        with open('ficheFilmDB.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, fieldnames=self.fieldnames)
            firstRow = True
            filmsList = []
            for row in csv_reader:
                if firstRow == True:
                    firstRow = False
                else:
                    filmsList.append(row)
            return filmsList
            
'''VIEW'''  
class gfcView():
    def __init__(self):
        pass

    def clrscr(self):
        if platform.system() == "Linux":
            return os.system("clear")
        elif platform.system() == "Windows":
            return os.system("cls")

    def mainMenu(self):
        titre = "Bienvenue dans votre GCF (Gestionnaire de Critique de Film)"
        listeDeChoix = ["1. Nouvelle critique", "2. Consulter une critique", "3. Effacer une critique", "4. Quitter"] 
        self.clrscr()
        print(titre, end="\n\n")
        for choix in listeDeChoix:
            print("\t" + choix)
        print("\n")  


    def newReviewV(self):
        titre = "\t\t\t\tNouvelle Critique\n\n"
        self.clrscr()
        
        choix = 0
        while choix <= 0:
            self.clrscr()
            print(titre)
            film = input("Entrez le nom du film à chercher : ")
            
            #Si le choix est vide on retourne au menu principal
            if not film: return

            resultats = tmdb.Query().movieData(film)
            print("\n*Si votre choix n'est pas affiché entrez \' 0 \' pour faire une autre recherche\n")
            
            choix = input("Entrez le numéro qui correspond au film voulu : ")
            #Si le choix est vide on retourne au menu principal
            if not choix: return

            #Si le choix n'est pas un nombre on affecte 21 qui est toujours plus grand que le nombre de résultat retourné par tmdb qui est 20
            try:
                choix = int(choix)
            except ValueError:
                choix = 21
            if choix > len(resultats):
                input("Erreur, veuillez réessayer.")
                choix = 0
                

        self.clrscr()
        print(titre)
        filmChoisi = resultats[choix - 1]
        tmdb.Query().printChoice(filmChoisi)
        
        filmChoisi['Note'] = input("Note (sur /10): \n\t\t\t")

        filmChoisi['Commentaire(s)'] = input("Commentaire(s): \n\t\t\t")
        return filmChoisi

    def missingFile(self):
        input("\nLe fichier \"ficheFilmDB.csv\" n'existe pas ou est vide. \n\n\t\t\t\t\t  Vous devez créer une nouvelle critique.")


    def searchReviewV(self, csvContent):
        self.clrscr()
        
        self.displayAllReviewsV(csvContent)

        id = input("\nEntrez le numero de la critique à consulter : ") 
        for dictionary in csvContent:
            if dictionary['Id'] == str(id):
                for key, value in dictionary.items():
                    if key == 'Acteur/trice(s)':
                        print(key, value.replace('\\', '\n\t\t\t'), sep=':\n\t\t\t', end='\n\n')
                
                    else:   
                        print(key, value, sep=' : \n\t\t\t', end='\n\n')
        
    def displayAllReviewsV(self, csvContent):
        self.clrscr()
        print("\t\t\t\tVoici la liste de toutes les critiques\n\n")
        for dictionary in csvContent:
            print(dictionary['Id'], dictionary['Nom'], sep=' : ')
        

    def deleteReviewV(self, csvContent):
        self.clrscr()
        self.displayAllReviewsV(csvContent)
        id = input("\nEntrez le numero de la critique à effacer : ")
        for dictionary in csvContent:
            if dictionary['Id'] == str(id):
                csvContent.remove(dictionary)
                break
        return csvContent
        


    def quit(self):
        self.clrscr()
        input("\n\n\t\t\tAu revoir.")
        self.clrscr()

'''CONTROLLER'''
class gfcController():
    def __init__(self):
        self.model = gfcModel()
        self.view = gfcView()
    

    def newReviewC(self):
        newReview = self.view.newReviewV()
        if not newReview: return
        self.model.writeCSV(newReview)
        

    def searchReviewC(self):
        if os.path.exists('./ficheFilmDB.csv'):
            csvContent = self.model.readCSV()
            if len(csvContent) > 0:
                self.view.searchReviewV(csvContent)
                input('\n')
            else:
                self.view.missingFile()
        else:
            self.view.missingFile()

    def displayAllReviewsC(self):
        if os.path.exists('./ficheFilmDB.csv'):
            csvContent = self.model.readCSV()
            if len(csvContent) > 0:
                self.view.displayAllReviewsV(csvContent)
                input('\n')
            else:
                self.view.missingFile()
        else:
            self.view.missingFile()

    def deleteReviewC(self):
        if os.path.exists('./ficheFilmDB.csv') and self.model.readCSV():
            csvContent = self.model.readCSV()
            csvContentMod = self.view.deleteReviewV(csvContent)
            input('\n')
            self.model.overWriteCSV(csvContentMod)
        else:
            self.view.missingFile()


    def quitC(self):
        self.view.quit()
        quit()

    def callFunc(self, choix):
        switcher = {
            '1': self.newReviewC,
            '2': self.searchReviewC,
            '3': self.deleteReviewC,
            '4': self.quitC
        }

        func = switcher.get(choix, lambda: input("La sélection n'est pas valide, réessayez."))
        func()

    def run(self):

        while(True):
            self.view.mainMenu()
            self.callFunc(input("Entrez votre choix: "))

if __name__ == "__main__":

    c = gfcController()
    c.run()
    
