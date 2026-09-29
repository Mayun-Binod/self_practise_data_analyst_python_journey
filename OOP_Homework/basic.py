# Create a class named Student and create one object from it.
class Student:
    def __init__(self, name, age,):
        self.name = name
        self.age = age

student1=Student ("sandhya", 19)
print (student1.name)
print (student1.age)

# Create a class named Person with the attributes:
# name
# age
# Create an object and print the attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("sandhya", 19)
print (person1.name)
print (person1.age)

person2 = Person("prakriti", 21)
print (person2.name)
print (person2.age)

# Create a class named Car with the attributes:
# brand
# model
# year
# Create one object and display its information.
class Phone:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

phone1 = Phone("apple", "iphone16", 2025)
print(phone1.brand)
print(phone1.model)
print(phone1.year)

# Create a class named Book with:
# title
# author
# price
# Create an object and print all three attributes.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

book1 = Book("eco", "Adam Smith", 500)
print(book1.title)
print(book1.author)
print(book1.price)

# Create a class named Employee with:
# name
# position
# salary
# Create two objects with different values and display their information.
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

employee1 = Employee("sunita", "Developer", 50000)
print (employee1.name)
print (employee1.position)
print (employee1.salary)

employee2 = Employee("Sandhya", "Designer", 60000)
print (employee2.name)
print (employee2.position)
print (employee2.salary)