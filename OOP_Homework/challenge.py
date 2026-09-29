# Create a class named Rectangle with:
# length
# width
# Create an object and calculate its:
# Area
# Perimeter
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

rectangle1 = Rectangle(10, 5)
area = rectangle1.length * rectangle1.width
perimeter = 2 * (rectangle1.length + rectangle1.width)
print(area)
print(perimeter)

# Create a class named Student with:
# name
# marks
# Create an object and determine whether the student passed or failed based on the marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = Student("sandhya", 65)

if student1.marks >= 40:
    print(student1.name, "Passed")
else:
    print(student1.name, "Failed")

# Create a class named Employee with:
# name
# salary
# Create three objects and find the employee with the highest salary.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee1 = Employee("sandhya", 50000)
employee2 = Employee("Sita", 65000)
employee3 = Employee("binod", 55000)

highest = employee1
if employee2.salary > highest.salary:
    highest = employee2
if employee3.salary > highest.salary:
    highest = employee3

print(highest.name)
print(highest.salary)

# Create a class named Temperature with a celsius attribute. Create an object and convert Celsius to Fahrenheit.
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

temperature1 = Temperature(25)
fahrenheit = (temperature1.celsius * 9 / 5) + 32
print(temperature1.celsius)
print(fahrenheit)

# Create a class named Person with:
# name
# age
# Create two objects and determine which person is older. solve this
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("sandhya", 19)
person2 = Person("Sita", 30)

if person1.age > person2.age:
    print(person1.name, "is older.")
elif person2.age > person1.age:
    print(person2.name, "is older.")
else:
    print("Both are the same age.")
