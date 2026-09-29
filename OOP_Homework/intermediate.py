# Create a class named Student with:
# name
# age
# grade
# Create three objects and display each student's information.
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Student("sandhya", 19, "B")
student2 = Student("prakriti", 21, "B+")
student3 = Student("binod", 25, "A+")

print(student1.name, student1.age, student1.grade)
print(student2.name, student2.age, student2.grade)
print(student3.name, student3.age, student3.grade)

# Create a class named BankAccount with:
# account_holder
# account_number
# balance
# Create two objects and display their account information.
class Bank_account:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

account1 = Bank_account("sandhya", 1001, 50000)
print(account1.account_holder)
print(account1.account_number)
print(account1.balance)

account2 = Bank_account("binod", 1002, 60000)
print(account2.account_holder)
print(account2.account_number)
print(account2.balance)

# Create a class named Mobile with:
# brand
# model
# price
# storage
# Create three objects and print their details.
class Mobile:
    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage

mobile1 = Mobile("Samsung", "S24", 100000, "256GB")
print(mobile1.brand, mobile1.model, mobile1.price, mobile1.storage)

mobile2 = Mobile("Apple", "iPhone 15", 120000, "128GB")
print(mobile2.brand, mobile2.model, mobile2.price, mobile2.storage)

mobile3 = Mobile("Xiaomi", "14", 80000, "256GB")
print(mobile3.brand, mobile3.model, mobile3.price, mobile3.storage)

# Create a class named Laptop with:
# brand
# processor
# ram
# price
# Create two objects and compare their prices.
class Laptop:
    def __init__(self, brand, processor, ram, price):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.price = price

laptop1 = Laptop("Dell", "Core i5", "16GB", 90000)
laptop2 = Laptop("HP", "Core i7", "16GB", 110000)

if laptop1.price > laptop2.price:
    print(laptop1.brand, "is more expensive.")

elif laptop2.price > laptop1.price:
    print(laptop2.brand, "is more expensive.")

else:
    print("Both laptops have the same price.")

# Create a class named Product with:
# name
# price
# quantity
# Create an object and calculate the total price using:
# price × quantity.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

product1 = Product("Keyboard", 2000, 3)
total_price = product1.price * product1.quantity
print(product1.name)
print(product1.price)
print(product1.quantity)
print(total_price)

