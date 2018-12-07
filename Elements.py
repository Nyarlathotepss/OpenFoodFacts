import requests
import pymysql

class API :
    '''Communicate with openfoodfact API '''
    def __init__(self):
        self.json = None

    def communication_api(self,url):
        self.r = requests.get(url)
        self.json = self.r.json()

class Display :
    '''allow to display "text" from API '''
    def __init__(self):
        self.list_info = []

    def print_info(self):
        print(list_info)

class Mysql_bdd :

    host = input("host name :")
    user = input("user name :")
    psw =  input("password :")
    db = input("database name :")

    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=psw,
                                 db=db,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)



