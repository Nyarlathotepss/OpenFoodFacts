# Utiliser les donn�es publiques de l'openfoodfact
===================================================

lien [github] (https://github.com/Nyarlathotepss/OpenFoodFacts.git)!
lien [trello] (https://trello.com/millet68/boards)!


Ce document a pour but d'expliquer l'utilisation du programme.
Vous devez importer les diff�rentes biblioth�ques necessaires � l'aide du fichier requirements.txt

## Cr�er la base de donn�es mysql
----------------------------

Dans votre console python �xecuter le programme tab_bdd.py.
Saisissez les diff�rentes informations demand�es concernant votre bdd mysql.
Le programme vous propose 2 choix possibles : destruction ou cr�ation
S�lectionner "c" pour cr�er les diff�rentes tables, "d" pour supprimer et "dc" pour supprimer puis cr�er.

Apr�s la cr�ation des tables le programme injecte les informations des produits directement dans la bdd.


## Utiliser le programme utilisateur
--------------------------------

Ex�cuter le fichier main.py

* Le programme vous demande si vous voulez afficher vos favoris
	* r�ponse possible : oui, yes, o, non, no, n

* Le programme vous demande de choisir parmis les diff�rents id de cat�gories propos�es.
	* r�ponse possible : num�ro de la cat�gorie

* Le programme vous affiche les diff�rents produits li�s � la cat�gories et vous demande d'en choisir 1.
	* reponse possible : num�ro du produit

* Le programme va alors vous proposer 5 produits avec une valeur nutritive moins �lev�e.
	* reponse possible : num�ro du produit alternatif

* Le programme vous demande si vous voulez sauvegarder le produit alternatif dans vos favoris.
	* r�ponse possible : oui, yes, o, non, no, n


