# projet-snake-
2 eme projet : jeu snake 

# groupe BI TD1
# Hanichi Lokman 
# Rumer Wilfried 
# Ami Sada Demya 

# Bieuville Aristide 
# URL de dépot GitHub : https://github.com/uvsq20001657/projet-snake-
# (par lokman)je me charge de la fonction qui permet au serpent de se déplacer et de le faire grandir à chaque fois qu'il mange une pomme , pour ne pas que le serpent traverse les 4 murs qu'a mit wilfried , j'ai utilisé les structures conditionnelles if et elif , il faut que le serpent soit dans des coordonnées précises pour qu'il puisse se déplacer par exemple voici les conditions pour qu'il puisse aller à gauche 

if direction  == 'gauche':
        if Serpent[0][0] > 49:
             Serpent[0][0]  = Serpent[0][0] - dx
"ce qui veut dire que tant que le le serpent n'est pas au niveau du mur gauche, il continuera à aller à gauche si on appuie sur la flèche gauche du clavier, et j'ai fait le même procédé pour les 3 autres directions.

# pour ce qui est de faire grandir le serpent à chaque fois qu'il croque une pomme , à l'aide d'une variable "i" et d'une boucle while , le serpent grandira de 1 cercle vert à chaque fois qu'il mange la pomme. Ensuite pour remettre une pomme j'appelle la fonction "test" qu'à crée Aristide pour en replacer une aléatoirement.
# le serpent commencera au milieu de l'air de jeu et il se dirigera vers le haut.
# (par damya) je me charge d'augmenter la difficulté du jeu en augmentant la vitesse de notre serpent et ensuite de le diriger                      .                            pour les fonctions de directions j'ai crée 4 fonctions pour les 4 directions. Je reprend la varirable globale "direction" de Lokman ainsi que les 4 directions qu'il a créé ("gauche", "droite", "haut", "bas") et j'associe chaque fonction à une direction (par exemple :la direction"droite" de lokman avec la fonction right que j'ai crée si je veux que le serpent aille a droite et je refais pour les 3 autres directions) 
# ensuite il ne me reste plus qu'à associer chacune des fonctions aux flèches du clavier donc pour cela par exemple si on reste toujours sur la fonction right j'associe la flèche droite a la fonction right grâce à un fen.bind et je réitere pour les 3 autres directions.

# (par aristide) je me charge de placer la pomme initiale ainsi que celles qui suivent dès que le serpent mange la précédente . Comme je dois placer les pommes aléatoirement j'utilise la librairie random. Je place la pomme initiale de façon aléatoire avec des coordonnéés comprises entre 50 et 450 pour ne pas qu'une pomme apparaisse dans un des murs. Ensuite pour les pommes qui suivent j'ai utilisé la structure conditionnelle "if" , donc si les coordonnées du serpent et de la pomme sont  identiques (donc le serpent a mangé la pomme) j'en replace une aléatoirement en utilisant encore "random" pour donner de nouvelles cordonnées à la pomme.

#(par damya) je me charge du "gamme over", c'est a dire que le jeu s'arrette lorsque le serpent touche un mur ou lorsque sa tete entre en collision avec son propre corps.

# (par wilfried) je me charge de la partie visuelle du jeu donc pour commencer j'ai créé un canvas noir de 500 qui represente  l'aire de jeu , ensuite 4 murs marron de 50 qui delimitent la zone où le serpent peut se déplacer et où les pommes peuvent apparaitre, j'ai ensuite créé deux boutons : le boutton "quitter" qui permettra de fermer la fenêtre si on clique dessus et ensuite le boutton "speed" qui est associé à la fonction de damya , si on clique une fois dessus , le jeu commence et ensuite dés qu'on clique dessus , le serpent se déplace plus vite (plus on appuie , plus il va vite).

 # dans notre groupe on était 5 mais malheureusement , la personne qui devait se charger du score et du game over a quitté le projet à la derniere minute. Pour le score, on a créé une fonctions qui ne marchent pas malheureusement comme vous pouvez le voir dans notre code. Pour le score , on a aussi essayé de créer une variable globale "score" et de l'insérer dans la fonction "placer_pomme " d'aristide car elle utiliste les mêmes conditions lorsqu'on place une pomme au hasard après que la précedente à été engloutie . Donc pour cela j'ai mis "score = score+1" mais cela n'a pas dutout marché.
