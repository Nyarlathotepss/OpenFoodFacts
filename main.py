from Elements import API, Mysql_bdd

list_category = ["boissons","snacks-sucres","produits-laitiers"]
list_products = None
info = API()
mybdd = Mysql_bdd()
k = 0   #indice
url = None

for category in list_category:# On balaie les 3 catégoeires

    try:
        with mybdd.connection.cursor() as cursor:# Pour chaque categorie on injecte cela dans bdd SQL
            sql = "INSERT INTO categorie (nom) VALUES (%s)"
            cursor.execute(sql, category)
    except Exception as e :
        print(e)

    url = 'https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0='+category+'&sort_by=unique_scans_n&page_size=100&axis_x=energy&axis_y=products_n&action=display&json=1'
    info.communication_api(url)

    while k < 101:
        try :
            list_products = (info.json['products'][k]['product_name'],info.json['products'][k]['ingredients_text_fr'],info.json['products'][k]['nutrition_grade_fr'],info.json['products'][k]['purchase_places'])
        except Exception as e:
            print(category)
        try:
            with mybdd.connection.cursor() as cursor:
                sql = "INSERT INTO produit(nom, ingredient, nutriscore, magasin, categorie) VALUES (%s, %s, %s, %s, %s)"  # on insere les donnée ds table produits
                sl_id_category = "SELECT id FROM categorie WHERE nom ="+ category  # on lie les 2 table avec une clé etrangère
                cursor.execute(sql, (list_products[0], list_products[1], list_products[2], list_products[3], sl_id_category))
        except Exception as e:
            print(e)
        k += 1
    k = 0


