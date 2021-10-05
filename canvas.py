from tkinter import *
from grille import *
from bdd_game import *

fenetre = Tk()

fenetre.title("Labyrinthe")
fenetre.geometry("1200x700")
fenetre.minsize(900, 700)



while i < size-1:
    while j < size-1:
        if mat[i][j] == "/":
            mon_canvas = Canvas(fenetre, width=35, height=35, bg="black")
            mon_canvas.pack(pady=20)

fenetre.mainloop()
