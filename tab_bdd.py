import pymysql
from elements import Injection, API


class bdd:
    """Connect to dbb and creating or deleting the tables"""

    def __init__(self):
        host = input("host name :")
        user = input("user name :")
        psw = input("password :")
        db = input("database name :")

        self.connection = pymysql.connect(host=host,
                                          user=user,
                                          password=psw,
                                          db=db,
                                          charset='utf8mb4')

    def creation(self):
        """created 3 tables :categorie, produit and favorie"""
        with self.connection.cursor() as cursor:
            try:
                sql = "CREATE TABLE Categorie(\
                id SMALLINT AUTO_INCREMENT,\
                nom VARCHAR(30)NOT NULL,\
                PRIMARY KEY(id)\
                )\
                ENGINE=INNODB;"
                cursor.execute(sql)
                sql = "CREATE TABLE Produit(\
                id SMALLINT AUTO_INCREMENT,\
                nom VARCHAR(200)NOT NULL UNIQUE,\
                ingredient TEXT,\
                nutriscore CHAR(10),\
                magasin CHAR(100),\
                url TEXT,\
                categorie SMALLINT,\
                PRIMARY KEY(id)\
                )\
                ENGINE=INNODB;"
                cursor.execute(sql)
                sql = "ALTER TABLE Produit\
                ADD CONSTRAINT categorie\
                FOREIGN KEY(categorie)\
                REFERENCES Categorie(id);"
                cursor.execute(sql)
                sql = "CREATE TABLE Favori(\
                id SMALLINT,\
                id_produit_substitue SMALLINT,\
                PRIMARY KEY(id)\
                )\
                ENGINE=INNODB;"
                cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                print(e)

    def destruction(self):
        """deleted the 3 tables"""

        with self.connection.cursor() as cursor:
            try:
                sql = "DROP TABLE favori;"
                cursor.execute(sql)
                sql = "DROP TABLE produit;"
                cursor.execute(sql)
                sql = "DROP TABLE categorie;"
                cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                print(e)


if __name__ == '__main__':
    injection_data = Injection()
    my_bdd = bdd()
    get_information_api = API()
    action = input("what do you want ? destruction (press d), creation (press c) or both (press dc) ?:")
    if action == "d":
        my_bdd.destruction()
    elif action == "c":
        my_bdd.creation()
        injection_data.api_to_bdd(my_bdd, get_information_api)
    elif action == "dc":
        my_bdd.destruction()
        my_bdd.creation()
        injection_data.api_to_bdd(my_bdd, get_information_api)
