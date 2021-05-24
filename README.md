# projet-snake-
2 eme projet : jeu snake 

# groupe BI TD1
# Hanichi Lokman 
# Rumer Wilfried 
# Ami Saada Damya 

# Bieuville Aristide 
# URL de dépot GitHub : https://github.com/uvsq20001657/projet-snake-
# (par lokman)je me charge d'abord de la fonction qui permet au serpent de se déplacer et de le faire grandir à chaque fois qu'il mange une pomme , pour ne pas que le serpent traverse les 4 murs qu'a mit wilfried , j'ai utilisé les structures conditionnelles if et elif , il faut que le serpent soit dans des coordonnées précises pour qu'il puisse se déplacer par exemple voici les conditions pour qu'il puisse aller à gauche 

   if direction  == 'left':
        if Serpent[0][0] > 50:
             Serpent[0][0]  = Serpent[0][0] - dx
"ce qui veut dire que tant que le le serpent n'est pas au niveau du mur gauche, il continuera à aller à gauche si on appuie sur la flèche gauche du clavier, et j'ai fait le même procédé pour les 3 autres directions.

# pour ce qui est de faire grandir le serpent à chaque fois qu'il croque une pomme , à l'aide d'une variable "i" et d'une boucle while , le serpent grandira de 1 cercle vert à chaque fois qu'il mange la pomme. Ensuite pour remettre une pomme j'appelle la fonction "placer_pomme" qu'à crée Aristide pour en replacer une aléatoirement.
# le serpent commencera au milieu de l'air de jeu et il se dirigera vers le haut.
 # Je me charge ensuite d'augmenter la difficulté du jeu en augmentant la vitesse de notre serpent grace a une fonction a qui j'ai associé le bouton speed qui lancera le jeu la première fois ou on clique dessus et ensuite le serpent se déplacera plus vite pour augmeenter la difficulté à chaque fois qu'on clique dessus.
 
# (par damya)d'abord je me charge du "game over", c'est a dire que le jeu s'arrête lorsque le serpent touche un mur ou lorsque sa tete entre en collision avec son propre corps avec la fonction Serpent.destroy() et j'affiche un message pour signaler au joueur qu'il a perdu. On peut voir au debut du code que j'ai ajouté la fonction intersect pour faciliter l'appel des coordonées du serpent et des murs, en effet la première fonction définit les positions des murs, la deuxième regroupe les positions des murs dans une liste qui est comparée à la position du snake et la troisième c'est le snake contre lui même. Le true signifie ''si y' a confrontation alors la fonction est vraie'' et ensuite ce "vrai" on s'en sert pour ''si la fonction est vraie alors game over'' qu'on retrouve plus bas avec la fonction Serpent.destroy.  Je me charge ensuite  de  diriger le serpent, pour les fonctions de directions j'ai crée 4 fonctions pour les 4 directions. Je reprend la varirable globale "direction" de Lokman ainsi que les 4 directions qu'il a créé ("right", "left", "down", "up") et j'associe chaque fonction à une direction (par exemple :la direction"right" de lokman avec la fonction droite que j'ai crée si je veux que le serpent aille a droite et je refais pour les 3 autres directions). Enfin, il ne me reste plus qu'à associer chacune des fonctions aux flèches du clavier donc pour cela par exemple si on reste toujours sur la fonction right j'associe la flèche droite a la fonction "droite" grâce à un fen.bind et je réitere pour les 3 autres directions.

# (par aristide) je me charge de placer la pomme initiale ainsi que celles qui suivent dès que le serpent mange la précédente . Comme je dois placer les pommes aléatoirement j'utilise la librairie random. Je place la pomme initiale de façon aléatoire avec des coordonnéés comprises entre 50 et 450 pour ne pas qu'une pomme apparaisse dans un des murs. Ensuite pour les pommes qui suivent j'ai utilisé la structure conditionnelle "if" , donc si les coordonnées du serpent et de la pomme sont  identiques (donc le serpent a mangé la pomme) j'en replace une aléatoirement en utilisant encore "random" pour donner de nouvelles cordonnées à la pomme, j'en profite aussi  pour rajouter 1 au score car le score utilise la même condition (que le serpent mange la pomme).


# (par wilfried) je me charge de la partie visuelle du jeu donc pour commencer j'ai créé un canvas noir de 500 qui represente  l'aire de jeu , ensuite 4 murs marron de 50 qui delimitent la zone où le serpent peut se déplacer et où les pommes peuvent apparaitre, j'ai ensuite créé deux boutons : le boutton "quitter" qui permettra de fermer la fenêtre si on clique dessus et ensuite le boutton "speed" qui est associé à la fonction de lokman , si on clique une fois dessus , le jeu commence et ensuite dés qu'on clique dessus , le serpent se déplace plus vite (plus on appuie , plus il va vite).
