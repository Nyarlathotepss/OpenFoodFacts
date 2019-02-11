import requests
import pymysql
import constant


class API:
    """Communicate with API"""
    def __init__(self):
        self.json = None

    def communication_api(self, url, dict_parameters):
        """got .json from api"""
        self.r = requests.get(url, dict_parameters)
        self.json = self.r.json()


class Display:
    """got information from BDD when user take a choice"""

    def __init__(self):
        self.list_pos = ("yes", "y", "oui")
        self.list_neg = ("no", "n", "non")

    def display_info_category(self, bdd):
        """display categories information from bdd"""
        with bdd.connection.cursor() as cursor:
            try:
                sql = "SELECT * FROM categorie"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
            except Exception as e:
                print(e)

    def display_info_product(self, bdd, user_input):
        """display products information from bdd"""
        with bdd.connection.cursor() as cursor:
            try:
                sql = "SELECT id, nom, nutriscore, ingredient, magasin, \
                       url FROM produit WHERE categorie = %s"
                cursor.execute(sql, user_input)
                result = cursor.fetchall()
                print(result)
                return result
            except Exception as e:
                print(e)

    def select_alternative_product(self, bdd, user_input_cat, user_input_prod):
        """select 5 different's products with nutriscore smaller than the user's choice"""
        with bdd.connection.cursor() as cursor:
            try:
                sql = "SELECT id, nom, nutriscore FROM produit WHERE categorie = %s \
                AND nutriscore < (SELECT nutriscore FROM produit WHERE id = %s) LIMIT 5"
                cursor.execute(sql, (user_input_cat, user_input_prod))
                print(user_input_cat, user_input_prod)
                result = cursor.fetchall()
                return result
            except Exception as e:
                print(e)

    def display_favorites(self, bdd):
        """display favorites information from bdd"""
        with bdd.connection.cursor() as cursor:
            try:
                sql = "SELECT * FROM produit WHERE id IN (SELECT id FROM favori)"
                cursor.execute(sql)
                result = cursor.fetchone()
                sql = "SELECT * FROM produit WHERE id IN (SELECT id_produit_substitue FROM favori)"
                cursor.execute(sql)
                result1 = cursor.fetchall()
                if result:
                    print(result)
                    print("substitute of :")
                    print(result1)
                else:
                    print("Favorites is empty")
            except Exception as e:
                print(e)


class MysqlBdd:
    """Allow to connect to mysql's bdd"""

    def __init__(self):
        host = input("hostname :")
        user = input("user's name :")
        psw = input("password :")
        db = input("database's name :")

        self.connection = pymysql.connect(host=host,
                                          user=user,
                                          password=psw,
                                          db=db,
                                          charset='utf8mb4')

    def insert_fav(self, id_alternative_product, id_product):
        """insert favorite information to bdd"""
        with self.connection.cursor() as cursor:
            try:
                sql = "INSERT INTO favori(id,id_produit_substitue) VALUES (%s, %s)"
                cursor.execute(sql, (id_alternative_product, id_product))
            except pymysql.Error:
                print('This product already exist in yours favorites')
        self.connection.commit()


class Injection:
    """Inject data from api (json) to database"""
    def __init__(self):
        self.url = None
        self.LIMIT_PRODUCT = constant.limit_products
        self.list_category = constant.list_categories_3
        self.info_products = None
        self.k = 0
        self.list_names_products = []

    def api_to_bdd(self, bdd, api):
        """for each categories name in list_category the method got 100 products from api
        then insert one by one into the database"""
        for i, category in enumerate(self.list_category):  # for each category > insert the category into bdd
            try:
                with bdd.connection.cursor() as cursor:
                    sql = "INSERT INTO categorie (nom) VALUES (%s)"
                    cursor.execute(sql, category)
            except Exception as e:
                print(e)
            bdd.connection.commit()

            url = 'https://fr.openfoodfacts.org/cgi/search.pl?'
            param_url = {'action': 'process',
                         'tagtype_0': 'categories',
                         'tag_contains_0': 'contains',
                         'tag_0': category,
                         'sort_by': 'unique_scans_n',
                         'page_size': self.LIMIT_PRODUCT,
                         'axis_x': 'energy',
                         'axis_y': 'products_n',
                         'json': '1'}

            api.communication_api(url, param_url)

            while self.k < self.LIMIT_PRODUCT:  # for each category > insert x products into bdd
                try:
                    self.info_products = (api.json['products'][self.k]['product_name'],
                                          api.json['products'][self.k]['ingredients_text_fr'],
                                          api.json['products'][self.k]['nutrition_grade_fr'],
                                          api.json['products'][self.k]['purchase_places'],
                                          api.json['products'][self.k]['url'])
                    if self.info_products[0].lower().strip() in self.list_names_products:
                        self.k += 1
                        continue
                    else:
                        self.list_names_products.append(self.info_products[0].lower().strip())
                except KeyError:  # if information doesn't exist in tuple
                    self.k += 1
                    continue

                try:
                    with bdd.connection.cursor() as cursor:
                        sql = "INSERT INTO produit(nom, ingredient, nutriscore" \
                              ", magasin, url, categorie) VALUES (%s, %s, %s, %s, %s, %s)"
                        id = str(i + 1)
                        cursor.execute(sql, (self.info_products[0], self.info_products[1], self.info_products[2],
                                             self.info_products[3], self.info_products[4], id))
                except pymysql.DatabaseError:
                    print("A duplicate name has been deleted")
                bdd.connection.commit()
                self.k += 1
            self.k = 0
