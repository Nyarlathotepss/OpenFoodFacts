from Elements import API, Mysql_bdd, Display

list_category = ["boissons","snacks-sucres","produits-laitiers"]
info_products = None
info = API()
mybdd = Mysql_bdd()
k = 0   #indice
url = None
LIMIT_PRODUCT = 101
disp_obj = Display()


for i, category in enumerate(list_category):# On balaie les 3 catégories
    try:# Pour chaque categorie on injecte cela dans bdd SQL
        with mybdd.connection.cursor() as cursor:
            sql = "INSERT INTO categorie (nom) VALUES (%s)"
            cursor.execute(sql, category)
    except Exception as e :
        print(e)
    mybdd.connection.commit()

    url = 'https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0='+category+'&sort_by=unique_scans_n&page_size=100&axis_x=energy&axis_y=products_n&action=display&json=1'
    info.communication_api(url)

    while k < LIMIT_PRODUCT:
        try :#On recupère les info du JSON par page
            info_products = (info.json['products'][k]['product_name'],info.json['products'][k]['ingredients_text_fr'],info.json['products'][k]['nutrition_grade_fr'],info.json['products'][k]['purchase_places'])
        except Exception as e:
            print(category)
        try:#Puis on les insère directement dans la BDD sans passer par une table
            with mybdd.connection.cursor() as cursor:
                sql = "INSERT INTO produit(nom, ingredient, nutriscore, magasin, categorie) VALUES (%s, %s, %s, %s, %s)"  # on insère les données ds table produit
                id = str(i + 1)
                cursor.execute(sql, (info_products[0], info_products[1], info_products[2], info_products[3], id))
        except Exception as e:
            print(e)
        mybdd.connection.commit()
        k += 1
    k = 0

while True:
    disp_favorite = input("Do you want to show favorites items ? :").lower()
    if disp_favorite in disp_obj.list_pos:
        disp_obj.disp_favo(mybdd)
        break
    elif disp_favorite in disp_obj.list_neg:
        break
    else:
        print("your input is wrong, try again")
print("blabla:",end="")
disp_obj.disp_info_cat(mybdd)
select_cat = input("Enter your category's number :")
disp_obj.disp_info_prod(mybdd, select_cat)
select_prod = input("Enter your product's number :")
disp_obj.sel_alt_prod(mybdd, select_cat, select_prod)
last_select_prod = input("Enter your product's number :")
while True:
    save_favorite = input("Do you want to save your item's choice ? :")
    if save_favorite in disp_obj.list_pos :
        mybdd.insert_fav(last_select_prod)
        disp_obj.disp_favo(mybdd)
        break
    elif save_favorite in disp_obj.list_neg:
        break
    else :
        print("your input is wrong, try again")




