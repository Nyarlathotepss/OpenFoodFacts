import requests

class API :

    def __init__(self):
        self.text = str

    def communication_api(self,url):
        self.r = requests.get(''url'')
        self.r = r.text

class Display :

    def disp_list(self,text):
        self.list_info = []

    def sort_info(self,text):
        for word in text :
            self.list_info.append(word) # a  titre d'exemple

    def print_info(self) :
        print(list_info)

