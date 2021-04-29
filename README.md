# projet-snake-
2 eme projet : jeu snake 

# groupe BI TD1
# Hanichi Lokman 
# Rumer Wilfried 
# Ami Sada Demya 
# Bellacene Annissa 
# Bieuville Aristide 
# URL de dépot GitHub : https://github.com/uvsq20001657/projet-snake-



#par Wilfried
import tkinter as tk 
import random as rd


#Variables
HEIGHT = 500
WIDTH = 500

a = rd.randint(70, 430)
b = rd.randint(70, 430)

c = rd.randint(70, 430)
d = rd.randint(70, 430)


#Fonctions
def creer_mur():
    """cree un mur de cote 20 sur l'herbe"""
    mur = canvas.create_rectangle((a, b), (a + 20, b + 20), fill="saddle brown")
   
    
def creer_pomme():
    """cree une pomme ronde de largeur 20"""
    pomme = canvas.create_oval((c, d), (c + 20, d + 20), fill="red")


#Programme principal
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="darkgreen", width=WIDTH, height=HEIGHT)
mur_droit = canvas.create_rectangle((450, 500), (500, 0), fill="saddle brown")
mur_gauche = canvas.create_rectangle((0, 500), (50, 0), fill="saddle brown")
mur_bas = canvas.create_rectangle((0, 500), (500, 450), fill="saddle brown")
mur_haut = canvas.create_rectangle((0, 0), (500, 50), fill="saddle brown")


creer_mur()
creer_mur()
creer_pomme()

canvas.grid()

racine.mainloop()



par lokman
# ce qui augmente de 1 la taille du serpent des qu'il croque la pomme (a mettre dans la fonction moove de damya)
 r=len(Serpent)-1
    while r > 0:
        Serpent[r][0]=Serpent[r-1][0]
        Serpent[r][1]=Serpent[r-1][1]
        can.create_oval(Serpent[r][0], Serpent[r][1], Serpent[r][0] +10, Serpent[r][1]+10,outline='green', fill='green')
        r=r-1
par lokman

#la fonction qui permet de placer une pomme aléatoirement 
def placer_pomme():
    global apple
    global x,y,pX,pY
    global Serpent
    if Serpent[1][0]>pX-7 and  Serpent[1][0]<pX+7:        
        if Serpent[1][1]>pY-7 and Serpent[1][1]<pY+7:
            #On remet une pomme au hasard
            pX = randrange(5, 495)
            pY = randrange(5, 495)
            can.coords(apple,pX, pY, pX+5, pY+5)
            #On joute un nouveau point au serpent
            Serpent.append([0,0])
            #print(Serpent)
       
x = 245
y = 24        
dx, dy = 10, 10
flag = 0
direction = 'haut'
Serpent=[[x,y],[x+2.5,y+2.5],[x+5,y+5],[0,0]]
