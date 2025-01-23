import json
import os


class Warehouse:
def __init__(self, file_name):
        self.file = {}
        if os.path.isfile(file_name):
            with open(file_name,"r") as file:
                file = json.load(file)
            if not type(file) == dict:
                return
            for key,value in file.items():
                self.file[key] = value

    def add_product(self,ID,name,amount,price):
        if ID in self.file:
            print("The product in warehouse")
        else:
            if amount <= 0:
                print("Error! amount less than zero!!")
            elif price <= 0:
                print("Error! price less than zero!!")
            else:
                self.file[ID] = {"name":name,"amount":amount,"price":price}
                print(f"The product entered the warehouse!!")

    def product_price_update(self,ID,price):
        if ID in self.file:
            self.file[ID]["price"] = price
            print("price updated successfully")
        else:
            print("The product isn't in warehouse")

    def product_amount_release(self,ID,amount):
        if ID not in self.file:
            print("The product not in warehouse!")
            return
        if self.file[ID]["amount"] > amount:
            self.file[ID]["amount"] -= amount
            print("The amount updated!!")
        else:
            print("The amount is large in exists")

    def search_product(self,ID):
        return self.file[ID]

    def return_all_product(self):
        return self.file

    def keeping(self,name):
        with open(name,"w") as file:
            json.dump(self.file,file)


my_warehouse = Warehouse("my.json")
my_warehouse.add_product(1111,"cup",100,10)
my_warehouse.add_product(1112,"coffee",20,35)
my_warehouse.add_product(1113,"sugar",100,2)
my_warehouse.add_product(1114,"tea",1000,5)
print(my_warehouse.return_all_product())

my_warehouse.keeping("my.json")