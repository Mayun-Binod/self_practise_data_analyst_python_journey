# Write a program that produces a SyntaxError. Identify and fix the mistake.
1name = 5
print(1name)

# Write a program that produces a NameError by using a variable before defining it.
print(name)

# Write a program that produces a TypeError by performing an operation on incompatible data types.
name = "sandhya"
age = 19
result = name+age
print(result)

# Write a program that produces a ValueError when converting user input into an integer.
age = int("hello")
print(age)

# Write a program that produces a ZeroDivisionError when dividing a number by zero.
a = 20
b = 0
c = a/b
print(c)

# Write a program that produces an IndexError by accessing an invalid list index.
number = [10, 20, 30]
print(number[5])

# Write a program that produces a KeyError by accessing a dictionary key that does not exist.
student = {
    "name": "sandhya",
    "age": 19
}
print(student["address"])