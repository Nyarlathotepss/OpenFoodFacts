import requests
import pymysql

class API:
    """Communicate with API"""
    def __init__(self):
        self.json = None

    def communication_api(self,url):
        self.r = requests.get(url)
        self.json = self.r.json()

class Display:
    """display info from BDD when user take a choice"""

    def __init__(self):
        self.category_info = None
        self.produit_info = None

    def disp_info_cat(self, bdd):
        with bdd.connection.cursor() as cursor:
            try:
                sql = "SELECT * FROM categorie"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
            except Exception as e:
                print(e)

    def disp_info_prod(self, bdd, user_input):
        with bdd.connection.cursor() as cursor:
            try:
                sql = "SELECT id, nom, nutriscore FROM produit WHERE categorie = '{0}'".format(user_input)
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
            except Exception as e:
                print(e)

    def sel_alt_prod(self, bdd, user_input_cat, user_input_prod):
        with bdd.connection.cursor() as cursor:
            try:
                sql = "SELECT id, nom, nutriscore FROM produit WHERE categorie = '{0}' AND nutriscore < (SELECT nutriscore FROM produit WHERE id = '{1}') LIMIT 5".format(user_input_cat, user_input_prod)
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
            except Exception as e:
                print(e)

class Mysql_bdd:
    '''Allow to connect to mysql's bdd'''

    host = "localhost"
    user = "root"
    psw =  "password"
    db = "openfoodfact"

    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=psw,
                                 db=db,
                                 charset='utf8mb4')