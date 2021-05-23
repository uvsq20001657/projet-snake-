# projet-snake-
2 eme projet : jeu snake 

# groupe BI TD1
# Hanichi Lokman 
# Rumer Wilfried 
# Ami Sada Demya 

# Bieuville Aristide 
# URL de dépot GitHub : https://github.com/uvsq20001657/projet-snake-
# (par lokman)je me charge de la focntion qui permet au serpent de se deplacer et de le faire grandir a chaque fois qu'il mange une pomme , pour ne pas que le serpent traverse les 4murs qu'a mit wilfried , j'ai utilisé les structures conditionnelles if et elif , il fait que le serpent soit dans des coordonnées précises pour qu'il puisse se déplacer par exemple voici les conditions pour qu'il puisse aller à gauche 

if direction  == 'gauche':
        if Serpent[0][0] > 49:
             Serpent[0][0]  = Serpent[0][0] - dx
"ce qui veut dire que tant que le le serpent n'est pas au niveau du mur gauche , il continuera à aller à gauche si on appuie sur la flèche gauche du clavier, et j'ai fait le même procédé pour les 3 autres directions.

# pour ce qui est de faire grandir le serpent à chaque fois qu'il croque une pomme , a l'aide d'une variable "i" et d'une boucle while , le serpent grandira de 1 cercle vert à chaque fois qu'il mange la pomme , ensuite pour remettre une pomme j'appelle la fonction qu'à crée aristide pour en replacer une aléatoirement.


