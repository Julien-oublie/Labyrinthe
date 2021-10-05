from tkinter import *
from grille import *
from bdd_game import *

#creer la fenetre
window = Tk()

#personaliser la fentre
window.title("Labyrinthe")
window.geometry("1200x700")
window.minsize(900, 800)
window.config(background='#41B77F')

#creer fram
frame = Frame(window,bg='#41B77F', bd=1, relief=SUNKEN)

#ajouter du texte
label_title=Label(frame, text="Bienvenue sur le jeu labyrinthe", font=("",40), bg="#41B77F",fg='white')
label_title.pack()

#ajouter un second texte
label_title=Label(frame, text="Appuie sur le boutton pour commencer", font=("",25), bg="#41B77F",fg='white')
label_title.pack()
#ajouter un premier bouton
boutton_game=Button(frame, text="GO !", font=("",25), bg="white",fg='#41B77F')
boutton_game.pack()
#ajouter frame
frame.pack(expand=YES)



#afficher la fenetre
window.mainloop()






