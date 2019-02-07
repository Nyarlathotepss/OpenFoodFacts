from elements import API, MysqlBdd, Display, Injection


class Interface:
    """Show information from bdd to user
    User can take different choices"""
    def __init__(self):
        self.list_id_category = []
        self.list_id_product = []
        self.list_id_alternative = []
        self.display_obj = Display()
        self.select_category = None
        self.select_product = None
        self.inj_data = Injection()
        self.mybdd = MysqlBdd()
        self.info = API()

    def display_favories(self):
        """Display the favories to user"""
        while True:
            user_display_favories = input("Do you want to show favorites items ? :").lower()
            if user_display_favories in self.display_obj.list_pos:
                self.display_obj.display_favories(self.mybdd)
                break
            elif user_display_favories in self.display_obj.list_neg:
                break
            else:
                print("your input is wrong, try again")

    def display_category_choice(self, categories):
        """Display the different category to user"""
        print("The different's categories:")
        for t in categories:
            print(t[0], ":", t[1])
            self.list_id_category.append(t[0])

    def display_product_choice(self, products):
        """Display the different product to user"""
        print("The different's products:")
        print(products)
        for product in products:
            print(product[0], ":", product[1], "-", product[2], "-", product[3], "-", product[4], "-", product[5])
            self.list_id_product.append(product[0])

    def display_alternative_product(self, alternative_products):
        """Display the different alternative products"""
        print("There are alternative products:")
        for a in alternative_products:
            print(a[0], ":", a[1], "-", a[2])
            self.list_id_alternative.append(a[0])

    def save_favory(self):
        """Allow to save the user choice about product"""

        while True:
            response_save_favory = input("Do you want to save your item's choice ? :").lower()
            if response_save_favory in self.display_obj.list_pos:
                mybdd.insert_fav(self.select_product)
                print("Your favory has been saves")
                break
            elif response_save_favory in self.display_obj.list_neg:
                break
            else:
                print("your input is wrong, try again")

    def check_user_choice(self, list_id, user_select):
        """Check is the user input is correct"""
        while True:
            try:
                user_select = int(user_select)
            except TypeError:
                user_select = input("You have to type number :")
                continue
            if user_select not in list_id:
                user_select = input("Your input is wrong, try again :")
            else:
                break

    def get_category(self):
        """Display category > let user take a choice > check if the input is correct"""
        category = self.display_obj.display_info_category(self.mybdd)  # got info from bdd about category (id and name)
        self.display_category_choice(category)  # display the different categories
        select_category = input("Enter your category's number :")  # user choice id
        self.check_user_choice(self.list_id_category, select_category)  # check if the id is correct

    def get_product(self):
        """Display product > let user take a choice > check if the input is correct"""
        all_list_products = self.display_obj.display_info_product(self.mybdd, self.select_category)
        self.display_product_choice(all_list_products)
        select_product = input("Enter your product's number :")
        self.check_user_choice(self.list_id_product, select_product)

    def get_alternative_product(self):
        """Display alternative product > let user take a choice > check if the input is correct"""
        alternative_list_products = self.display_obj.select_alternative_product(self.mybdd, self.select_category,
                                                                                self.select_product)
        self.display_alternative_product(alternative_list_products)
        select_alternative_product = input("Enter your product's number :")
        self.check_user_choice(self.list_id_alternative, select_alternative_product)


if __name__ == '__main__':

    display_user = Interface()
    display_user.display_favories()

    display_user.get_category()
    display_user.get_product()
    display_user.get_alternative_product()

    display_user.save_favory()


