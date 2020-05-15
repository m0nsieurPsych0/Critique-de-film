**Gestionnaire de Critique de Film**
------------------------------------

**Auteurs**

* Louis Barbonnet
* Karl Boulais


**Présentation**
----------------
Ce programme sert de base de donnée locale pour gérer des fiches de critique de visionnement de film. Le coeur du programme est l'intéraction avec l'API de « The Movie Data Base » (TMDB). En effet, les informations pertinentes pour le film voulu sont automatiquement remplie dans chaque fiche de sorte que vous pourrez vous concentrez à écrire votre critique!
Nous ne réinventons pas la roue et nous simplifions une tâche qui normalement(nous trouvons) est laborieuse. De plus, avec peu de modification, il serait possible de créer plus de sections aux fiches et d'y inclure plus d'informations comme le budget et le pays où le film à été tournée.

**Logiciel requis pour utiliser le GCF**
----------------------------------------
* python 3
* tmdbsimple
	* pip install tmdbsimple

**Constitution d'une fiche**
----------------------------
===================== =============
Sections:			  Remplis par:
===================== =============
Id                    tmdb
Nom                   tmdb
Genre                 tmdb
Année de sortie       tmdb
Réalisateur/trice(s)  tmdb
Acteur/trice(s)       tmdb
Note sur 10           utilisateur
Commentaire(s)		  utilisateur
===================== =============


**Recherche de film**
---------------------
Vous pouvez chercher le nom du film autant en utilisant son titre en anglais qu'en français. Par contre, le résultat qui sera retourné sera toujours en anglais.


**Format de la base de donnée**
-------------------------------
Le format généré par le programme est *'ficheFilmDB.csv'*. Il est donc possible de modifier à l'extérieur (ex: avec notepad ou excel) et de voir les changements dans le GCF. 
La première ligne du fichier est l'entêtes des différentes sections qui compose les colonnes du fichier.

==== ===== ======= ================ ====================== ================= ====== ================ 
'Id' 'Nom' 'Genre' 'Date de sortie' 'Réalisateur/trice(s)' 'Acteur/trice(s)' 'Note' 'Commentaire(s)'
==== ===== ======= ================ ====================== ================= ====== ================ 

Le programme traite chaque ligne du fichier comme une fiche. Vous pouvez modifier le contenu, mais le nombre de colonne doit rester le même. Par conséquent, vous ne pouvez pas ajouter une nouvelle catégorie de donnée dans le fichier ex: 'Budget'. Pour ce faire vous devrez modifier le code.

*Faites attention, si vous le modifier avec excel ou d'autre programme, car il se peut que le fichier soit convertie en un autre format et devienne incompatible avec le programme GCF*


**Autre informations pertinentes**
----------------------------------
Le programme tente de suivre le model de code MVC. Malheureusement, de par la nature d'un programme avec un interface graphique en ligne de commande, nous devons prendre du input au moment de l'affichage de certaines lignes.

Si vous décidez de modifier le programme, sâchez qu'il est encore en BETA à ce point-ci et que son code n'est pas particulièrement clean.


