import qrcode
from time import sleep

PRODUCTS = []
Factor = []

def Read_Database():
    with open("Pylearn7\Assignment 7\Database.txt", "r") as Database:
        for line in Database:
            line = line.strip()
            product_list = line.split(",")
            
            if len(product_list) == 4:
                my_dictionary = {"code": product_list[0], "name": product_list[1], "price": product_list[2], "storage": product_list[3]}
                PRODUCTS.append(my_dictionary)

Read_Database()
print("Loading is completed!")

def Show_Menu():
    print("1 : Add")
    print("2 : Edit")
    print("3 : Remove")
    print("4 : Search")
    print("5 : Show list")
    print("6 : Buy")
    print("7 : QRcode product")
    print("8 : Exit")

def Add():

    code = int(input("Please enter your product id : "))
    name = str(input("Please enter your product name : "))
    price = int(input("Please enter your product price : "))
    storage = int(input("Please enter your product storage : "))
    new_product = {"code":code,"name":name,"price":price,"storage":storage}
    PRODUCTS.append(new_product)
    print("Product add operation was successful.")

def Edit():

    choice = int(input("Which one do you want to change?(1 = name | 2 = price| 3 = storage) : "))
    if choice == 1:
        for row in PRODUCTS:
            print(row["name"],"\t",row["price"],"\t",row["storage"])
        select = input("Select your product name : ")
        for row in PRODUCTS:
            if row["name"] == select:
                new_product = input("New name: ")
                row["name"] = new_product
        print("Product edit operation was successful.")
    if choice == 2:
        for row in PRODUCTS:
            print(row["name"],"\t",row["price"],"\t",row["storage"])
        select = input("Select your product name : ")
        for row in PRODUCTS:
            if row["name"] == select:
                new_product = input("New price : ")
                row["price"] = new_product
        print("Product Edit operation success.")
    if choice == 3:
        for row in PRODUCTS:
            print(row["name"],"\t",row["price"],"\t",row["storage"])
        select = input("Select your product name : ")
        for row in PRODUCTS:
            if row["name"] == select:
                new_product = input("New storage : ")
                row["storage"] = new_product
        print("Product edit operation was successful.")

def Remove():

    global PRODUCTS
    code = int(input("Please enter your product id : "))
    new_products = [row for row in PRODUCTS if row['code'] != code]
    PRODUCTS = new_products
    print("Product remove operation was successful.")

def Search():

    user_Search = input("Please enter your product id or name : ")
    for product in PRODUCTS:
        if product["code"]==user_Search or product["name"]==user_Search:
            print(product["code"],"\t",product["name"],"\t",product["price"])
            break
    else:
        print("Not found!")

def Show_List():

    print("Loading...")
    sleep(3)
    for row in PRODUCTS:
        print(row["code"],"\t",row["name"],"\t",row["price"])

def Buy():

    while True:
        for row in PRODUCTS:
            print(row["code"],"\t",row["name"],"\t",row["price"],"\t",row["storage"])
        select = input("Please enter your product code : ")
        for row in PRODUCTS:
            if select == row["code"]:
                user_count_Buy = int(input("Please enter how much you want : "))
                if user_count_Buy <= int(row["storage"]):
                    row["storage"] = int(row["storage"]) - user_count_Buy
                    user_Basket = [row["name"],user_count_Buy,row["price"]]
                    Factor.append(user_Basket)
                    print("Product buy operation was successful.")
                    break
                else:
                    print("We dont have enough products for you!")
        else:
            print("We dont have any products with this code.")
        continue_shopping = input("Do you want to continue shopping? (y/n): ")
        if continue_shopping.lower() != "y":
            Print_Factor()
            break

def save_in_Database():

    with open("Database.txt","w") as Database:
        for row in PRODUCTS:
            code = row["code"]
            name = row["name"]
            price = row["price"]
            storage = row["storage"]
            data = str(f"{code},{name},{price},{storage}\n")
            Database.write(data)

def Print_Factor():

    for row in Factor:
        print(row)

def Make_QRcode():

    product_code = int(input("Please enter your product code : "))
    for row in PRODUCTS:
        if product_code == int(row["code"]):
            code = row["code"]
            name = row["name"]
            price = row["price"]
            storage = row["storage"]
            product_info = f"{code},{name},{price},{storage}"
            qr_code = qrcode.make(product_info)
            qr_code.save("product-QRcode.png")
            print("Product QRcode now is available.")
    else:
        print("We dont have any products with this code.")

while True:

    Show_Menu()
    user_operation = int(input("Please enter you want: "))
    if user_operation == 1:
        Add()
    elif user_operation == 2:
        Edit()
    elif user_operation == 3:
        Remove()
    elif user_operation == 4:
        Search()
    elif user_operation == 5:
        Show_List()
    elif user_operation == 6:
        Buy()
    elif user_operation == 7:
        Make_QRcode()
    elif user_operation == 8:
        save_in_Database()
        exit(0)
    else:
        print("Please enter a number between 1 to 8")