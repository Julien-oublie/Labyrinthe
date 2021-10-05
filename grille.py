from random import randrange
from tkinter import *

size = 5
mat =[[-1 for i in range(size)] for i in range(size)]
mat[1][0] = 0
mat[size-2][size-1] = 0

def createCase(mat):
    inc = 1
    for i in range(1, size-1, 2):
        for j in range(1, size-1, 2):
            inc = inc + 1
            mat[i][j] = inc


def createMurIncassable(mat):
    for i in range(2, size-2, 2):
        for j in range(2, size-2, 2):
            mat[i][j] = -1



def createMur(mat):
    for i in range(1, size-1, 1):
        for j in range(2, size-2, 2):
            mat[i][j] = 1
    for i in range(2, size-2, 2):
        for j in range(1, size-1, 1):
            mat[i][j] = 1




def getRandMur(mat):
    lst = []
    for i in range(1, size-1):
        for j in range(1, size-1):
            if mat[i][j] == 1:
                if i % 2 == 0:
                    if mat[i - 1][j] != mat[i + 1][j]:
                        lst.append([i,j])
                else:
                    if mat[i][j - 1] != mat[i][j + 1]:
                        lst.append([i,j])
    if len(lst) == 0:
        return -5
    else:
        randmur = lst[randrange(len(lst))]
        return randmur


def remplirCase(oldval, newval, mat):
    for i in range(1,size-1):
        for j in range(1,size-1):
            if mat[i][j] == oldval:
                mat[i][j] = newval


createCase(mat)
createMur(mat)
createMurIncassable(mat)

randmur = getRandMur(mat)
count = 10
while randmur != -5 and count != 0:
    count = count
    x = randmur[0]
    y = randmur[1]
    mat[x][y] = -2
    for i in range(1,size-1,1):
        for j in range(1,size-1,1):
            if mat[i][j] == -2:
                mat[i][j] = 0
                if i % 2 == 0:
                    if mat[i - 1][j] > mat[i + 1][j]:
                        remplirCase(mat[i - 1][j], mat[i + 1][j], mat)
                    else:
                        remplirCase(mat[i + 1][j], mat[i - 1][j], mat)
                else:
                    if mat[i][j - 1] > mat[i][j + 1]:
                        remplirCase(mat[i][j - 1] , mat[i][j + 1], mat)
                    else:
                        remplirCase(mat[i][j + 1] , mat[i][j - 1], mat)
    randmur = getRandMur(mat)

for i in range(size):
    for j in range(size):
        value = 0
        if mat[i][j] == -1:
            value = "w"
        elif mat[i][j] == 1:
            value = "/"
        else:
            value = mat[i][j]
        print(value, " ", end='')
    print(' ')


fenetre = Tk()

fenetre.title("Labyrinthe")
fenetre.geometry("1200x700")
fenetre.minsize(900, 700)



while i < size-1:
    while j < size-1:
        if mat[i][j] == "/":
            mon_canvas = Canvas(fenetre, width=35, height=35, bg="black")
            mon_canvas.create_rectangle()
            mon_canvas.pack(pady=20)

fenetre.mainloop()