# Utiliser les données publiques de l'openfoodfact
===================================================

lien [github] (https://github.com/Nyarlathotepss/OpenFoodFacts.git)!
lien [trello] (https://trello.com/millet68/boards)!


Ce document a pour but d'expliquer l'utilisation du programme.
Vous devez importer les différentes bibliothèques necessaires à l'aide du fichier requirements.txt

## Créer la base de données
----------------------------

Connectez vous tout d'abord sur votre bdd MySQL et positionnez vous sur la base dans laquelle vous voulez créer les tables
Une fois cela fait, dans python éxécuter le programme tab_bdd.py
Le programme vous propose 2 choix possibles : destruction ou création
Sélectionner c pour créer les différentes tables

Une fois cette étape réalisée le programme injecte les données dans les différentes tables


## Utiliser le programme utilisateur
--------------------------------

Exécuter le fichier main.py

* Le programme vous demande si vous voulez afficher vos favoris
	* réponse possible : oui, yes, o, non, no, n

* Le programme vous demande de choisir parmis les différents id de catégories proposées.
	* réponse possible : numéro de la catégorie

* Le programme vous affiche les différents produits liés à la catégories et vous demande d'en choisir 1.
	* reponse possible : numéro du produit

* Le programme va alors vous proposer 5 produits avec une valeur nutritive moins élevée.
	* reponse possible : numéro du produit alternatif

* Le programme vous demande si vous voulez sauvegarder le produit alternatif dans vos favoris.
	* réponse possible : oui, yes, o, non, no, n


