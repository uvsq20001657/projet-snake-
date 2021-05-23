
# projet-snake-
#2 eme projet : jeu snake 

# groupe BI TD1
# Hanichi Lokman 
# Rumer Wilfried 
# Ami Sada Demya 

# Bieuville Aristide 
# URL de dépot GitHub : https://github.com/uvsq20001657/projet-snake-


from tkinter import *

from random import randrange

 
def deplacement(): #fonction qui va permettre au serpent d'etre en mouvement de facon automatique et de le fire grandir a chaque fois qu'il mange une pomme.   par lokman
  
    global y,pX,pY,x,Serpent

    can.delete('all')
    i=len(Serpent)-1
   #fonction qui va permettre au serpent de grandir de  1 a chaque fois qu'il mange une pomme
    while i > 0:
        Serpent[i][0]=Serpent[i-1][0]
        Serpent[i][1]=Serpent[i-1][1]
    #creation du serpent
        can.create_oval(Serpent[i][0], Serpent[i][1], Serpent[i][0] +10, Serpent[i][1]+10,outline='green', fill='green')
        i=i-1
  #creation des 4 murs et de la pomme
 #je reprend ici les memes mur que wilfried a crée pour le menu
    can.create_rectangle(pX, pY, pX+10, pY+10, fill='red')
    mur_droit = can.create_rectangle((450, 500), (500, 0), fill="saddle brown")
    mur_gauche = can.create_rectangle((0, 500), (50, 0), fill="saddle brown")
    mur_bas = can.create_rectangle((0, 500), (500, 459), fill="saddle brown")
    mur_haut = can.create_rectangle((0, 0), (500, 50), fill="saddle brown")
   
    if direction  == 'gauche':
        #le serpent ira a gauche si on appuie sur la fleche de gauche jusqu'à ce qu'il rencontre le mur gauche
        if Serpent[0][0] > 49:
             Serpent[0][0]  = Serpent[0][0] - dx
    elif direction  == 'droite':
              #le serpent ira a droite si on appuie sur la fleche de droitejusqu'à ce qu'il rencontre le mur de droite
        if Serpent[0][0] <445:
            Serpent[0][0]  = Serpent[0][0] + dx
    elif direction  == 'haut':
             #le serpent ira en haut si on appuie sur lafleche du haut jusqu'à ce qu'il rencontre le mur du haut
        if Serpent[0][1]> 49:
            Serpent[0][1]  = Serpent[0][1] - dy
    elif direction  == 'bas':
            #le serpent ira enn bas si on appuie sur la fleche du bas jusqu'à ce qu'il rencontre le mur du bas
        if Serpent[0][1] < 451:
            Serpent[0][1]  = Serpent[0][1] + dy
#au lancement de la partie , le serpent sera dans le mur gauche mais une fois qu'il sortira de c mur , il lui sera impossible de rentrer dans un des 4murs 
    #création de la tête du serpent , je change la couleur pour qu'on puisse la differencier du corps 
        
    can.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0]+10, Serpent[0][1]+10, fill='red')
   
   
   
    if flag != 0:
        fen.after(60, deplacement)
        #une fois que le serpend a grandit car il a mangé une pomme , j'appelle la focntion d'aristide pour en replacer une 
        test()

   
#augmentation de la vitesse et création des fonctions qui dirigent le serpent par damya
def speed():
    global pX,pY
    global flag
        #cette fonction permet de lancer le jeu dans un premier temps et ensuite d'augmenter la vitesse de deplacement du serpent
    if flag == 0:
        flag = 1
    deplacement()
 #on crée les fonctions qui vont permettre de diriger le serpent grâce au fleches du clavier
def left(event):
    global direction
    direction = 'gauche'

def right(event):
    global direction
    direction = 'droite'
 
def up(event):
    global direction
    direction = 'haut'
 
def down(event):
    global direction
    direction = 'bas'
   #placement des pommes de facon aléatoire par aristide
def test():
    #cette fonction placera la pomme initiale et celles d'après de façon aléatoire
    global pomme,x,y,pX,pY, Serpent
    
    if Serpent[1][0]>pX-7 and  Serpent[1][0]<pX+7:        
        if Serpent[1][1]>pY-7 and Serpent[1][1]<pY+7:
           #dés que le serpent mange la pomme , on en replace une nouvelle au hasard
            pX = randrange(60, 440)
            pY = randrange(60, 440)
            can.coords(pomme,pX, pY, pX+5, pY+5)
            
            Serpent.append([0,0])

x = 245
y = 24        
dx, dy = 10, 10
flag = 0
direction = 'haut'
Serpent=[[x,y],[x+2.5,y+2.5],[x+5,y+5],[0,0]]
#placement de la pomme initiale
pX = randrange(50, 450)
pY = randrange(50, 450)


#création du canvas par wilfried
fen = Tk()
can = Canvas(fen, width=500, height=500, bg='black')
can.pack(side=BOTTOM, padx=5, pady=5)
fen.title(" projet SNAKE ")

#on recréé la pomme et les 4murs pour le menu cette fois ci

pomme = can.create_rectangle(pX, pY, pX+5, pY+5,  fill='red')
mur_droit = can.create_rectangle((450, 500), (500, 0), fill="saddle brown")
mur_gauche = can.create_rectangle((0, 500), (50, 0), fill="saddle brown")
mur_bas = can.create_rectangle((0, 500), (500, 459), fill="saddle brown")
mur_haut = can.create_rectangle((0, 0), (500, 50), fill="saddle brown")
#création des boutons 
#ce bouton lancera le jeu la premiere fois qu'on appuyera dessus et,ensuite dés qu'on appuie dessus , la vitesse augmentera
b1 = Button(fen, text='speed', command=speed, bg='black' , fg='white')
b1.pack(side=LEFT, padx=5, pady=5)
 #ce bouton va fermer la fenetre quand on appuyera dessus
b2 = Button(fen, text='Quitter', command=fen.destroy, bg='black' , fg='white')
b2.pack(side=RIGHT, padx=5, pady =5)

tex1 = Label(fen, text="Cliquez une fois sur'speed' pour commencer , cliquez plusieurs fois pour augmenter la vitesse", bg='black' , fg='white')
tex1.pack(padx=0, pady=11,)
#association des touches avec les fonctions de directions
fen.bind('<Right>', right)
fen.bind('<Left>', left)
fen.bind('<Up>' , up)
fen.bind('<Down>', down)

 

fen.mainloop()
