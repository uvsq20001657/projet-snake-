
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
#ajout de coordonnée/intersection pour faciliter le "game_over", donc la fenêtre se fermera grâce à 
# un fen1.destroy qu'il y'a dans la fonction de lokman grâce au valeurs si dessous  
# lorsque le serpent se mangera lui même ou sinon dés qu'il touche un des 4murs de wilfried(damya)
def intersect(Serp,b,can):

      bc=can.coords(b)
      if (Serp[0][0]>= bc[0]  and Serp[0][0]+10 < bc[2]  and Serp[0][1] >= bc[1] and Serp[0][1]+10 < bc[3]):
        return True
      else:
        return False
def intersectlist(can,a, lb):
    for b in lb:
        if intersect(a,b,can):
            return True
    return False

def intersecthimself(Serp):
    for i in range(2 ,len(Serp)):
        if (Serp[1][0] == Serp[i][0]    and Serp[1][1] == Serp[i][1]) :
            return True
    return False

def deplacement(): #fonction qui va permettre au serpent d'etre en mouvement de façon automatique et
                   # de le faire grandir à chaque fois qu'il mange une pomme.   par lokman
  
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
   #destruction du serpent lorsqu'il se touche ou touche un mur par rapport aux intersect que damya a fait plus haut
    if inteif intersectlist(can ,Serpent,[mur_droit,mur_gauche,mur_bas,mur_haut]) or intersecthimself(Serpent) :
        #on affiche un message au joueur pour l'informer qu'il a perdu
      ptext4 =Label(fen1, text="PERDU", bg='blue' , fg='white')
      ptext4.pack(padx=10, pady=11,)
      #on détruit le serpent
      Serpent.destroy()

    if direction  == 'left':
        #le serpent ira a gauche si on appuie sur la flèche de gauche jusqu'à ce qu'il rencontre le mur gauche
        if Serpent[0][0] > 50:
             Serpent[0][0]  = Serpent[0][0] - dx
    elif direction  == 'right':
              #le serpent ira a droite si on appuie sur la fleche de droitejusqu'à ce qu'il rencontre le mur de droite
        if Serpent[0][0] <450:
            Serpent[0][0]  = Serpent[0][0] + dx
    elif direction  == 'up':
             #le serpent ira en haut si on appuie sur la fleche du haut jusqu'à ce qu'il rencontre le mur du haut
        if Serpent[0][1]> 50:
            Serpent[0][1]  = Serpent[0][1] - dy
    elif direction  == 'down':
            #le serpent ira en bas si on appuie sur la flèche du bas jusqu'à ce qu'il rencontre le mur du bas
        if Serpent[0][1] < 450:
            Serpent[0][1]  = Serpent[0][1] + dy

    #création de la tête du serpent , je change la couleur pour qu'on puisse la differencier du corps 
        
    can.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0]+10, Serpent[0][1]+10, fill='red')
   
   
   
    if flag != 0:
        fen1.after(50, deplacement)
        #une fois que le serpent a grandit car il a mangé une pomme, j'appelle la fonction d'aristide pour en replacer une 
        placer_pomme()

   #augmentation de la difficulté du jeu par lokman
def speed():
      #pour augmenter la difficulté j'augmente juste la vitesse de déplacement à l'aide de la variable globale "flag".
    global flag
        #cette fonction permet de lancer le jeu dans un premier temps et ensuite d'augmenter la vitesse de déplacement du serpent
    if flag == 0:
        flag =1
    deplacement()

 #je  crée les fonctions qui vont permettre de diriger le serpent grâce au flèches du clavier (par damya)
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

#la fonction score que nous n'avons pas réussi a faire fonctionner 
#def score():
 #Label(fen, text='Score:  ').grid(row=0,column=0)

 #scores = StringVar()
 #Score = Entry(fen, textvariable=scores)
 #Score.grid(row=0,column=1)
 #scores.set('0')
    
    


#création du canvas par wilfried
fen1 = Tk()
can = Canvas(fen1, width=500, height=500, bg='black')
can.pack(side=BOTTOM, padx=5, pady=5)
fen1.title(" projet SNAKE ")

#on recrée la pomme et les 4murs pour le menu cette fois ci

pomme = can.create_rectangle(pX, pY, pX+10, pY+10,  fill='red')
mur_droit = can.create_rectangle((445, 500), (500, 0), fill="saddle brown")
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



#association des touches avec les fonctions de directions de damya
fen1.bind('<Right>', droite)
fen1.bind('<Left>', gauche)
fen1.bind('<Up>' , haut)
fen1.bind('<Down>', bas)
#affichage des instructions
ptex1 = Label(fen1, text="utiliser les flèches pour diriger le serpent", bg='black' , fg='white')
ptex1.pack(padx=0, pady=11,)

tex1 = Label(fen1, text="Cliquez une fois sur'speed' pour commencer , cliquez plusieurs fois pour augmenter la vitesse", bg='black' , fg='white')
tex1.pack(padx=0, pady=11,)

ptext2 =Label(fen1, text="utiliser la touche quitter pour fermer le jeu", bg='black' , fg='white')
ptext2.pack(padx=0, pady=11,)
fen1.mainloop()
