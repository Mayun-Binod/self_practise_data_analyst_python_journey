# ==========================================
# Python OOP - Class, Object and Public
# ==========================================


# 1. Basic Class and Object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating an object
person1 = Person("Ram", 25)

print("Name:", person1.name)
print("Age:", person1.age)


# ==========================================
# 2. Public Attributes
# ==========================================

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


student1 = Student("Sita", 20, "A")

print("\nStudent Information")
print("Name:", student1.name)
print("Age:", student1.age)
print("Grade:", student1.grade)


# ==========================================
# 3. Multiple Objects
# ==========================================

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print("\nCar 1")
print("Brand:", car1.brand)
print("Model:", car1.model)

print("\nCar 2")
print("Brand:", car2.brand)
print("Model:", car2.model)


# ==========================================
# 4. Public Attribute Can Be Changed
# ==========================================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee = Employee("Hari", 30000)

print("\nBefore Change")
print("Name:", employee.name)
print("Salary:", employee.salary)

# Changing public attribute
employee.salary = 40000

print("\nAfter Change")
print("Name:", employee.name)
print("Salary:", employee.salary)


# ==========================================
# 5. Class with Method
# ==========================================

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number * self.number


calculator = Calculator(5)

print("\nCalculator")
print("Number:", calculator.number)
print("Square:", calculator.square())