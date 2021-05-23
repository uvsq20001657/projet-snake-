# projet-snake-
2 eme projet : jeu snake 

# groupe BI TD1
# Hanichi Lokman 
# Rumer Wilfried 
# Ami Sada Demya 

# Bieuville Aristide 
# URL de dépot GitHub : https://github.com/uvsq20001657/projet-snake-
# (par lokman)je me charge de la fonction qui permet au serpent de se deplacer et de le faire grandir a chaque fois qu'il mange une pomme , pour ne pas que le serpent traverse les 4murs qu'a mit wilfried , j'ai utilisé les structures conditionnelles if et elif , il fait que le serpent soit dans des coordonnées précises pour qu'il puisse se déplacer par exemple voici les conditions pour qu'il puisse aller à gauche 

if direction  == 'gauche':
        if Serpent[0][0] > 49:
             Serpent[0][0]  = Serpent[0][0] - dx
"ce qui veut dire que tant que le le serpent n'est pas au niveau du mur gauche , il continuera à aller à gauche si on appuie sur la flèche gauche du clavier, et j'ai fait le même procédé pour les 3 autres directions.

# pour ce qui est de faire grandir le serpent à chaque fois qu'il croque une pomme , a l'aide d'une variable "i" et d'une boucle while , le serpent grandira de 1 cercle vert à chaque fois qu'il mange la pomme , ensuite pour remettre une pomme j'appelle la fonction "test" qu'à crée aristide pour en replacer une aléatoirement.
# le serpent commencera au milieu de l'air de jeu et il se dirigera vers le haut.
# (par damya) je me charge d'augmenter la difficulté du jeu en augmentant la vitesse de notre serpent et ensuite de le diriger                      .                            pour les fonctions de directions j'ai crée 4 fonctions pour les 4 directions , je reprend la varirable globale "direction" de lokman ainsi que les 4 directions qu'il a créé ("gauche", "droite", "haut", "bas") et j'associe chaque fonction  a une direction (par exemple :la direction"droite" de lokman avec la fonction right que j'ai crée si je veux que le serpent aille a droite et je refais pour les 3 autres directions) 
# ensuite il me reste plus qu'à associe chacune des fonctions aux flèches du clavier donc pour cela par exemple si on reste toujours sur la fonction right j'associe la flèche droite a la fonction right grâce à un fen.bind et je réitere pour les 3 autres directions.

# (par aristide) je me charge de placer la pomme initiale ainsi que celles qui suivent dés que le serpent mange la précédente . Comme je dois placer les pommes aléatoirement j'utilise la librairie random . Alors d'abord pour la pomme initiale je la place juste de façon aléatoire avec des coordonnéés comprises entre 50 et 450 pour ne pas qu'une pomme apparaisse dans un des murs. Ensuite pour les pommes qui suivent j'ai utilisé la structure conditionnelle "if" , donc si les coordonnées du serpent et de la pomme sont  identiques (donc le serpent a mangé la pomme) j'en replace une aléatoirement en utilisant encore "random" pour donner de nouvelles cordonnées à la pomme.

# (par wilfried) je me charge de la partie visuelle du jeu donc pour commencer j'ai créé un canvas noir de 500 qui represente  l'aire de jeu , ensuite 4 murs marron de 50 qui delimite la zone ou le serpent peut se déplacer et où les pommes peuvent apparaitre, j'ai ensuite créé deux boutons : le boutton "quitter" qui permettra de fermer la fenêtre si on clique dessus et ensuite le boutton "speed" qui est associé à la fonction de damya , si on clique une fois dessus , le jeu commence et ensuite dés qu'on clique dessus , le serpent se déplace plus vite (plus on appuie , plus il va vite).


 # dans notre groupe on était 5 mais malheureusement , la personne qui devait se charger du score et du game over a quitté le projet à la derniere minute . Pour le score on a tenté de créer une variable "score" et que le score augmente de 1 a chaque fois que la pomme a été mangé donc dans la focntion d'aristide qui place la pomme , on a inséré a la suite de la condition qui crée une nouvelle pomme (donc la condition est : le serpent mange la pomme (ce qui est la meme condition que le score))de mettre un "score=score+1" mais le code ne marchait plus donc on a du faire sans, pour le game over notre fonction actuelle de déplacement  oblige que  les coordonnées du serpent soit entre les murs pour qu’il puisse se déplacer mais avant il n’y avait pas cette condition ,on avait créé une fonction de déplacement où le serpent pouvais se balader dans tout le canvas même dans les murs et on voulait garder la même condition que celle de la fonction actuelle mais pas pour permettre au serpent de se déplacer si les coordonnées étaient comprise entre les murs , mais le contraire , donc , si les coordonnées du serpent sortait de l’aire (donc le serpent était dans un mur)  , le jeu s’arrête  et wilfried fait afficher une fenêtre avec marqué «perdu» mais cela n’a pas fonctionné donc on a changé la fonction pour obtenir l’actuelle fonction de déplacement.


