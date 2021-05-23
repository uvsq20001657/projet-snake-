
from tkinter import *

from random import randrange
#la fonction game over ne fonctionne pas
def game_over ():
    global mur_bas, mur_droit, mur_gauche , mur_haut , gameover, Serpent
    if Serpent == mur_droit or mur_bas or mur_haut or mur_gauche:
        can.delete(all) 
        can.coords(gameover, 300, 300)
    elif Serpent == can.create_oval(): 
        can.delete('all')
        can.coords(gameover, 300, 300)

def deplacement(): #fonction qui va permettre au serpent d'etre en mouvement de façon automatique et de le faire grandir à chaque fois qu'il mange une pomme.   par lokman
  
    global y,pX,pY,x,Serpent

    can.delete('all')
    i=len(Serpent)-1
   #fonction qui va permettre au serpent de grandir de 1 à chaque fois qu'il mange une pomme
    while i > 0:
        Serpent[i][0]=Serpent[i-1][0]
        Serpent[i][1]=Serpent[i-1][1]
    #création du serpent
        can.create_oval(Serpent[i][0], Serpent[i][1], Serpent[i][0] +10, Serpent[i][1]+10, fill='green')
        i=i-1
  #creation des 4 murs et de la pomme
    can.create_rectangle(pX, pY, pX+10, pY+10, fill='red')
 #je reprend ici les memes mur que wilfried a crée pour le menu
   
    mur_droit = can.create_rectangle((450, 500), (500, 0), fill="saddle brown")
    mur_gauche = can.create_rectangle((0, 500), (50, 0), fill="saddle brown")
    mur_bas = can.create_rectangle((0, 500), (500, 459), fill="saddle brown")
    mur_haut = can.create_rectangle((0, 0), (500, 50), fill="saddle brown")
   
    if direction  == 'left':
        #le serpent ira a gauche si on appuie sur la flèche de gauche jusqu'à ce qu'il rencontre le mur gauche
        if Serpent[0][0] > 49:
             Serpent[0][0]  = Serpent[0][0] - dx
    elif direction  == 'right':
              #le serpent ira a droite si on appuie sur la fleche de droitejusqu'à ce qu'il rencontre le mur de droite
        if Serpent[0][0] <445:
            Serpent[0][0]  = Serpent[0][0] + dx
    elif direction  == 'up':
             #le serpent ira en haut si on appuie sur la fleche du haut jusqu'à ce qu'il rencontre le mur du haut
        if Serpent[0][1]> 49:
            Serpent[0][1]  = Serpent[0][1] - dy
    elif direction  == 'down':
            #le serpent ira en bas si on appuie sur la flèche du bas jusqu'à ce qu'il rencontre le mur du bas
        if Serpent[0][1] < 451:
            Serpent[0][1]  = Serpent[0][1] + dy

    #création de la tête du serpent , je change la couleur pour qu'on puisse la differencier du corps 
        
    can.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0]+10, Serpent[0][1]+10, fill='red')
   
   
   
    if flag != 0:
        fen1.after(50, deplacement)
        #une fois que le serpent a grandit car il a mangé une pomme, j'appelle la fonction d'aristide pour en replacer une 
        placer_pomme()

   
#augmentation de la vitesse et création des fonctions qui dirigent le serpent par damya
def speed():
    global pX,pY
    global flag
        #cette fonction permet de lancer le jeu dans un premier temps et ensuite d'augmenter la vitesse de déplacement du serpent
    if flag == 0:
        flag = 1
    deplacement()
 #on crée les fonctions qui vont permettre de diriger le serpent grâce au flèches du clavier
def gauche(event):
    global direction
    direction = 'left'

def droite(event):
    global direction
    direction = 'right'
 
def haut(event):
    global direction
    direction = 'up'
 
def bas(event):
    global direction
    direction = 'down'

#placement des pommes de facon aléatoire par aristide
def placer_pomme():
#cette fonction placera la pomme initiale et celles d'après de façon aléatoire
    global pomme,x,y,pX,pY, Serpent
    
    if Serpent[1][0]>pX-8 and  Serpent[1][0]<pX+8:        
        if Serpent[1][1]>pY-8 and Serpent[1][1]<pY+8:
#dès que le serpent mange la pomme , on en replace une nouvelle au hasard
            pX = randrange(60, 440)
            pY = randrange(60, 440)
            can.coords(pomme,pX, pY, pX+5, pY+5)
             
            Serpent.append([0,0])


#la fonction score que nous n'avons pas réussi a faire fonctionner 
#def score():
 #Label(fen, text='Score:  ').grid(row=0,column=0)

 #scores = StringVar()
 #Score = Entry(fen, textvariable=scores)
 #Score.grid(row=0,column=1)
 #scores.set('0')
    
    


x = 245
y = 245        
dx, dy = 10, 10
flag = 0
direction = 'up'
#le serpent sera placé au milieu de l'aire de jeu au début et il se déplacera vers le haut
Serpent=[[x,y],[x+2.5,y+2.5],[x+5,y+5],[0,0]]


#placement de la pomme initiale
pX = randrange(50, 450)
pY = randrange(50, 450)

#création du canvas par wilfried
fen1 = Tk()
can = Canvas(fen1, width=500, height=500, bg='black')
can.pack(side=BOTTOM, padx=5, pady=5)
fen1.title(" projet SNAKE ")
gameover=can.create_text(300,300,text="GAME OVER")
#on recréé la pomme et les 4murs pour le menu cette fois ci

pomme = can.create_rectangle(pX, pY, pX+5, pY+5,  fill='red')
mur_droit = can.create_rectangle((450, 500), (500, 0), fill="saddle brown")
mur_gauche = can.create_rectangle((0, 500), (50, 0), fill="saddle brown")
mur_bas = can.create_rectangle((0, 500), (500, 459), fill="saddle brown")
mur_haut = can.create_rectangle((0, 0), (500, 50), fill="saddle brown")

#création des boutons 
#ce bouton lancera le jeu la premiere fois qu'on appuyera dessus et,ensuite dés qu'on appuie dessus , la vitesse augmentera
b1 = Button(fen1, text='speed', command=speed, bg='black' , fg='white')
b1.pack(side=LEFT, padx=5, pady=5)
 
#ce bouton va fermer la fenetre quand on appuyera dessus
b2 = Button(fen1, text='Quitter', command=fen1.destroy, bg='black' , fg='white')
b2.pack(side=RIGHT, padx=5, pady =5)

tex1 = Label(fen1, text="Cliquez une fois sur'speed' pour commencer , cliquez plusieurs fois pour augmenter la vitesse", bg='black' , fg='white')
tex1.pack(padx=0, pady=11,)

#association des touches avec les fonctions de directions
fen1.bind('<Right>', droite)
fen1.bind('<Left>', gauche)
fen1.bind('<Up>' , haut)
fen1.bind('<Down>', bas)

ptex1 = Label(fen1, text="utiliser les flèches pour diriger le serpent", bg='black' , fg='white')
ptex1.pack(padx=0, pady=11,)

ptext2 =Label(fen1, text="utiliser la touche quitter pour fermer le jeu", bg='black' , fg='white')
ptext2.pack(padx=0, pady=11,)
fen1.mainloop()
