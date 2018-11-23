import requests

class API :
'''Communicate with openfoodfact API / Informations will be in variable "text" '''
    def __init__(self):
        self.text = str

    def communication_api(self,url):
        self.r = requests.get(''url'')
        self.text = r.text

class Display :
'''allow to display "text" from API '''
    def __init__(self):
        self.list_info = []

    def print_info(self) :
        print(list_info)

