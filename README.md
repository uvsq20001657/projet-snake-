# projet-snake-
2 eme projet : jeu snake 

# groupe BI TD1
# Hanichi Lokman 
# Rumer Wilfried 
# Ami Sada Demya 

# Bieuville Aristide 
# URL de dépot GitHub : https://github.com/uvsq20001657/projet-snake-
#(par lokman)je me charge de la focntion qui permet au serpent de se deplacer et de le faire grandir a chaque fois qu'il mange une pomme , pour ne pas que le serpent traverse les 4murs qu'a mit wilfried , j'ai utilisé les structures conditionnelles if et elif , il fait que le serpent soit dans des coordonnées précises pour qu'il puisse se déplacer par exemple voici les conditions pour qu'il puisse aller à gauche 

if direction  == 'gauche':
        #le serpent ira a gauche si on appuie sur la fleche de gauche jusqu'à ce qu'il rencontre le mur gauche
        if Serpent[0][0] > 49:
             Serpent[0][0]  = Serpent[0][0] - dx


