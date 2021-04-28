# projet-snake-
2 eme projet : jeu snake 

# groupe BI TD1
# Hanichi Lokman 
# Rumer Wilfried 
# Ami Sada Demya 
# Bellacene Annissa 
# Bieuville Aristide 
# URL de dépot GitHub : https://github.com/uvsq20001657/projet-snake-


# ce qui augmente de 1 la taille du serpent des qu'il croque la pomme (a mettre dans la fonction moove de damya)
 r=len(Serpent)-1
    while r > 0:
        Serpent[r][0]=Serpent[r-1][0]
        Serpent[r][1]=Serpent[r-1][1]
        can.create_oval(Serpent[r][0], Serpent[r][1], Serpent[r][0] +10, Serpent[r][1]+10,outline='green', fill='green')
        r=r-1
par lokman
