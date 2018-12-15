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

from Elements import API, Mysql_bdd

list_category = ["boissons","snacks-sucres","produits-laitiers"]
list_products = []
info = API()
mybdd = Mysql_bdd()
k = 0   #indice
url = None

for category in list_category:
    url = 'https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0='+category+'&sort_by=unique_scans_n&page_size=100&axis_x=energy&axis_y=products_n&action=display&json=1'
    print(url)
    info.communication_api(url)
    while k < 101:
        try :
            list_products.append((info.json['products'][k]['product_name_fr'],info.json['products'][k]['nutrition_grade_fr']))
        except :
            print(category)
        k += 1
    k = 0

for category in list_category:
    try:
        with mybdd.connection.cursor() as cursor:
            sql = "INSERT INTO categorie (nom) VALUES (%s)"
            cursor.execute(sql, category)
        mybdd.connection.commit()
    except Exception as e:
        print(e)

try:
    with mybdd.connection.cursor() as cursor:
        sql = 'SELECT id,nom FROM categorie'
        cursor.execute(sql)
        all_info_cat = cursor.fetchone()
        for info_cat in all_info_cat:
            print(all_info_cat)
except Exception as e:
    print(e)
