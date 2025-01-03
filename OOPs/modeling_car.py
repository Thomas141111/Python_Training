# Modeling a car
class Car():
    def __init__(self,make,model,year):
        self.make= make
        self.model= model
        self.year= year

    def start_engine(self):
        print(f"Started engine of the {self.make}")

    def drive(self):
        print(f"You are driving a {self.model} of {self.year}")

car1= Car("Hatchback","z-series",'2020')
car1.start_engine()
car1.drive()

# 2.Bank account
class BankAccount:
    def __init__(self, name, balance):
        self.name= name
        self.balance= balance

    def show_balance(self):
        return f"Your current balance is {self.balance}"

    def deposit(self):
        amount = int(input("Enter amount you want to deposit: "))
        self.balance += amount
        print(f"Amount deposited successfully. Updated balance is {self.balance}")

    def withdraw(self):
        amount = int(input("Enter amount you want to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"Amount withdrawn successfully. Updated balance is {self.balance}")

my_account = BankAccount("Tom", 500)
print(my_account.show_balance())
my_account.deposit()
my_account.withdraw()

# Shopping Cart
all_items = []

class Items():
    def __init__(self, name, price):
        item = {name: price}
        all_items.append(item)

class ShoppingCart():

    def add_items(self, name, price):
        item = {name: price}
        all_items.append(item)
        print(f"Item {item} added")

    def remove_item(self, item_name):
        for item in all_items:
            if item_name in item:
                all_items.remove(item)
                print(f"Item {item_name} removed")
                return

        print("Item not found")

    def get_total(self):
        total = sum(price for item in all_items for price in item.values())
        print("The sum is: ", total)

    def show_items(self):
        print("Items in cart:")
        for item in all_items:
            for name, price in item.items():
                print(f"{name}: {price}")

cart = ShoppingCart()
Items("Lays", 20)
Items("Maggie", 80)
Items("Coke", 100)

cart.add_items("Slice", 100)
cart.add_items("Vegetables", 50)
cart.show_items()
cart.remove_item("Slice")
cart.show_items()
cart.get_total()

