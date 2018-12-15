import requests
import pymysql

class API:
    '''Communicate with openfoodfact API '''
    def __init__(self):
        self.json = None

    def communication_api(self,url):
        self.r = requests.get(url)
        self.json = self.r.json()

class Display:
    '''allow to display "text" from API '''
    def __init__(self):
        self.list_info = []

    def print_info(self):
        print(list_info)

class Mysql_bdd:

    host = "localhost"
    user = "root"
    psw =  "password"
    db = "openfoodfact"

    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=psw,
                                 db=db,
                                 charset='utf8mb4')
