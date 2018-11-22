"""
GET
C'est la méthode la plus courante pour demander une ressource. Une requête GET est sans effet sur la ressource, il doit être possible de répéter la requête sans effet.
HEAD
Cette méthode ne demande que des informations sur la ressource, sans demander la ressource elle-même.
POST
Cette méthode doit être utilisée lorsqu'une requête modifie la ressource.
OPTIONS
Cette méthode permet d'obtenir les options de communication d'une ressource ou du serveur en général.
CONNECT
Cette méthode permet d'utiliser un proxy comme un tunnel de communication.
TRACE
Cette méthode demande au serveur de retourner ce qu'il a reçu, dans le but de tester et d'effectuer un diagnostic sur la connexion.
PUT
Cette méthode permet d'ajouter une ressource sur le serveur.
DELETE
Cette méthode permet de supprimer une ressource du serveur.
"""
'''
import requests
r= requests.get('https://world.openfoodfacts.org/categories.json')
r= requests.get('https://fr.openfoodfacts.org/categorie/boissons-lactees.json')
r.text
'''

from Elements import API, Display

toto = API()
toto.communication_api('https://fr.openfoodfacts.org/categorie/coffee-drinks.json')