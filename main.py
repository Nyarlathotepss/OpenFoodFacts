from Elements import API, Mysql_bdd, Display, Injection

info = API()
mybdd = Mysql_bdd()
disp_obj = Display()
inj_data = Injection()

while True:
    question_inj = input("Do you want to inject data in database ? :").lower()
    if question_inj in disp_obj.list_pos:
        inj_data.api_to_bdd(mybdd, info)
        break
    elif question_inj in disp_obj.list_neg:
        break

while True:
    disp_favorite = input("Do you want to show favorites items ? :").lower()
    if disp_favorite in disp_obj.list_pos:
        disp_obj.disp_favo(mybdd)
        break
    elif disp_favorite in disp_obj.list_neg:
        break
    else:
        print("your input is wrong, try again")

cat = disp_obj.disp_info_cat(mybdd)
print("The differents categories:")
for t in cat:
    print(t[0], ":", t[1])
select_cat = input("Enter your category's number :")

all_list_products = disp_obj.disp_info_prod(mybdd, select_cat)
for product in all_list_products:
    print(product[0], ":", product[1], "-", product[2], "-", product[3], "-", product[4], "-", product[5])
select_prod = input("Enter your product's number :")

print("There are alternativ products:")
alt_list_products = disp_obj.sel_alt_prod(mybdd, select_cat, select_prod)
for alt in alt_list_products:
    print(alt[0], ":", alt[1], "-", alt[2])

last_select_prod = input("Enter your product's number :")
while True:
    save_favorite = input("Do you want to save your item's choice ? :").lower()
    if save_favorite in disp_obj.list_pos:
        mybdd.insert_fav(last_select_prod)
        break
    elif save_favorite in disp_obj.list_neg:
        break
    else:
        print("your input is wrong, try again")
