# projet-snake-
2 eme projet : jeu snake 

# groupe BI TD1
# Hanichi Lokman 
# Rumer Wilfried 
# Ami Sada Demya 
# Bellacene Annissa 
# Bieuville Aristide 
# URL de dépot GitHub : https://github.com/uvsq20001657/projet-snake-

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
