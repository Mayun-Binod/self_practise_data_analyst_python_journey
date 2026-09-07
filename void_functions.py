# Write a void function that prints "Hello, Python!".
def hello():
    print("Hello, Python!")

hello()

# Write a void function that takes a person's name and prints: Hello, Binod
def takes(name):
    print("Hello,", name)

takes("Binod")

# Write a void function that takes two numbers and prints their sum.
def add(a, b):
    print(a + b)

add(10, 20)

# Write a void function that takes a number and prints whether it is even or odd.
def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(7)

# Write a void function that takes a number and prints its multiplication table from 1 to 10.
def table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

table(5)


