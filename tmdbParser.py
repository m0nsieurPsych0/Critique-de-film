import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import base64
import tmdbsimple as tmdb
from urllib.request import urlopen


tmdb.API_KEY = 'a1f4134f61b7b8a5fe7c2f84d028e282'

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
        im = im.resize((1000, 1000), Image.ANTIALIAS)
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

        self.precedentBtn = None
        self.suivantBtn = None
        self.titreLbl = None
        self.currentImageLbl = None
        self.releaseDateLbl = None
        self.genresLbl = None

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

        self.titreLbl = tk.Label(self, text=self.listFilm[self.index].name)
        self.titreLbl.pack(side="top")

        self.currentImageLbl = tk.Label(image=self.listFilm[self.index].photo)
        self.currentImageLbl.image = self.listFilm[self.index].photo
        self.currentImageLbl.pack(side="bottom")

        self.releaseDateLbl = tk.Label(self, text=self.listFilm[self.index].releaseDate)
        self.releaseDateLbl.pack(side="bottom")

        self.genresLbl = tk.Label(self, text=None)
        for genre in self.listFilm[self.index].genres:
            tempText = str(self.genresLbl['text']) + ( " " + genre["name"])
            self.genresLbl['text'] = tempText
        self.genresLbl.pack(side="bottom")


    def actualizeWidgets(self):
        self.titreLbl['text'] = self.listFilm[self.index].name
        self.currentImageLbl['image'] = self.listFilm[self.index].photo
        self.releaseDateLbl['text'] = self.listFilm[self.index].releaseDate
        self.genresLbl['text'] = ""
        for genre in self.listFilm[self.index].genres:
            tempText = str(self.genresLbl['text']) + ( " " + genre["name"])
            self.genresLbl['text'] = tempText

        

    def precedent(self):
        if (self.index > 0):
            self.index -= 1
            self.actualizeWidgets()

    def suivant(self):
        if (self.index + 1 < len(self.listFilm)):
            self.index += 1
            self.actualizeWidgets()


if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("TMDB Parser")
    filmList=[]
    filmList.append(film(603))
    filmList.append(film(608))
    app = MainFrame(filmList, master=root)
    app.mainloop()
    