# MohammadAli Mirzaei

import sqlite3
basket = []

class Shop:

    def show_menu(self):
        print("1-Show Products")
        print("2-Add New")
        print("3-Edit")
        print("4-Remove")
        print("5-Buy")
        print('6- Show the Basket')
        print('7- Exit')
        print("--------------------------------")


    def load_database(self):
        global con, my_cursor
        con = sqlite3.connect("Shop\shop.db")
        my_cursor = con.cursor()


    def show_list(self):
        result = my_cursor.execute("SELECT * FROM products WHERE 1")
        prod_selected = result.fetchall()
        for prod in prod_selected:
            print(prod)
        print("--------------------------------")


    def add_new(self):
        new_prod_name = input("Enter a name for your new product... ")
        new_prod_price = input("Enter price of your new product... ")
        new_prod_number = input("Enter nuumber of your new product... ")
        my_cursor.execute(f"INSERT INTO products(id,prod_name,prod_cost,remain) VALUES('null,{new_prod_name},{new_prod_price},{new_prod_number}')")
        print("PRODCT INSERTED SUCCESSFULLY")
        con.commit()
        print("--------------------------------")


    def edit(self):
        id = input("Enter product id for edit... ")
        choise = input("Enter new name... ")
        price = input("Enter new price... ")
        num = input("Enter remain number in store... ")
        my_cursor.execute(f"UPDATE products SET prod_name='{choise}',prod_cost='{price}',remain='{num}' WHERE id={id}")
        con.commit()
        print("PRODCT EDITED SUCCESSFULLY")
        print("--------------------------------")
        Shop.show_list()


    def remove(self):
        choise = input("Enter genre id... ")
        my_cursor.execute(f"DELETE FROM genres WHERE GenreId = '{choise}'")
        con.commit()
        print("PRODCT REMOVED SUCCESSFULLY")
        print("--------------------------------")
        Shop.show_list()

    def show_basket(self):
        print('=====================================================')
        print("name\t\tprice\t\tcount\t\tsum")
        sum = 0
        for item in basket:
            print(item['name'], "\t", item['price'], "\t", item['count'], "\t", item['sum'])
            sum +=item['sum']
            print('-------------------------------------------------')
        print("Total: ",sum)    
        print('=====================================================')

    def buy(self):
        while True:
            code = int(input("Enter prod code: "))
            result = my_cursor.execute(f"SELECT * FROM products WHERE id = {code}")
            prod_selected = result.fetchone()
            if prod_selected[0] == code:
                while True:
                    user_count = int(input("Enter product count: "))
                    if user_count > prod_selected[3]:
                        print('Store does not have enough product...')
                    else:
                        user_shop = {'name':prod_selected[1], 'price':prod_selected[2], 
                                        'count':user_count, 'sum':(prod_selected[2] * user_count)}
                        basket.append(user_shop)
                        prod_remain = prod_selected[3] - user_count
                        result = my_cursor.execute(f"UPDATE products SET remain={prod_remain} WHERE id={code}")
                        break
            else:
                print('Product not found...')
                
            pos = input("do you want to buy more? y / n: ")
            if pos == 'n':
                print('============================')
                print("name\t\tprice\t\tcount\t\tsum")
                sum = 0
                for item in basket:
                    print(item['name'], "\t", item['price'], "\t", item['count'], "\t", item['sum'])
                    sum +=item['sum']
                print('--------------------')
                print("Total: ",sum)
                break
    
shop = Shop()
while True:
    shop.show_menu()
    choise = int(input())
    shop.load_database()

    match choise:
        case 1:
            shop.show_list()
        case 2:
            shop.add_new()
        case 3:
            shop.edit()
        case 4:
            shop.remove()
        case 5:
            shop.buy()
        case 6:
            shop.show_basket()
        case 7:
            exit(0)
