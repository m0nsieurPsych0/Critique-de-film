import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import base64
import tmdbsimple as tmdb
from urllib.request import urlopen

'''
root = Tk() #Doit etre au debut du programme, c'est le widget root

lblTest = Label(root,text=title) #On fait un lbl est on lui passe d'abord son parent

#Une des manieres d'afficher des widgets a l'ecran est d'utiliser pack, tres basic mais peu precis
lblTest.pack()

#On fait la loop main de l'app, elle tourn en permanence
root.mainloop()
'''


tmdb.API_KEY = 'a1f4134f61b7b8a5fe7c2f84d028e282'

movie = tmdb.Movies(603)
response = movie.info()

title = movie.title

print(movie.info())

class film:
    def __init__(self, id):
        self.movie = tmdb.Movies(id)
        self.info = self.movie.info()
        self.name = self.movie.title
        self.genres = self.info['genres']
        self.releaseDate = self.info['release_date']
        self.urlImage = self.info['poster_path']
        self.photo = self.printPoster()


    def printPoster(self):

        URL = "https://image.tmdb.org/t/p/w1280" + self.urlImage
        u = urlopen(URL)
        raw_data = u.read()
        u.close()

        im = Image.open(BytesIO(raw_data))
        im = im.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        return photo

        


class photoFrame(tk.Frame):
    def __init__(self, film, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.displayPhoto(film)

    def displayPhoto(self, film):
        photo = film.printPoster
        self.label = tk.Label(image=film.printPoster)
        self.label.image = photo
        self.label.pack()


class MainFrame(tk.Frame):
    def __init__(self, listFilm, master=None):
        self.listFilm = listFilm
        self.index = 0
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.precedentBtn = tk.Button(self)
        self.precedentBtn["text"] = "Precedent"
        self.precedentBtn["command"] = self.precedent
        self.precedentBtn.pack(side="left")

        self.suivantBtn = tk.Button(self)
        self.suivantBtn["text"] = "Suivant"
        self.suivantBtn["command"] = self.suivant
        self.suivantBtn.pack(side="right")

        self.titreLabel = tk.Label(self, text=self.listFilm[self.index].name)
        self.titreLabel.pack(side="top")

        self.currentImage = tk.Label(image=self.listFilm[self.index].photo)
        self.currentImage.image = self.listFilm[self.index].photo
        self.currentImage.pack(side="bottom")

    def precedent(self):
        self.index -= 1

    def suivant(self):
        self.index += 1


if __name__ == "__main__":
    root = tk.Tk()
    filmList=[]
    filmList.append(film(603))
    app = MainFrame(filmList, master=root)
    #phDisplay = photoFrame(filmList[0], master=root)
    app.mainloop()


'''
root = tk.Tk()

URL = "https://image.tmdb.org/t/p/w1280" + filmList[0].urlImage
u = urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
im = im.resize((250, 250), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(im)

label = tk.Label(image=photo)
label.image = photo
label.pack()

root.mainloop()
'''
