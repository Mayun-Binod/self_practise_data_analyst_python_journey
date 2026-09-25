# Create a list of 5 fruits and print each fruit using a for loop.
fruits = ["apple", "banana", "mango", "orange", "grapes"]
for fruit in fruits:
    print(fruit)

# Create a list of 5 numbers and print each number.
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number)

# Create a list of 5 names and print each name.
names = ["Ram", "Sita", "Hari", "Gita", "Mina"]
for name in names:
    print(name)

# Print all even numbers from a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for number in numbers:
    if number % 2 == 0:
        print(number)

# Print all odd numbers from a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for number in numbers:
    if number % 2 == 1:
        print(number)

# Create a list of 5 fruits and print each fruit using a while loop.
fruits = ["apple", "banana", "mango", "orange", "grapes"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Print all numbers in a list using their index.
numbers = [10, 20, 30, 40, 50]
i = 0
while i < len(numbers):
    print(i, numbers[i])
    i += 1

# Print the first 3 items of a list using a while loop.
fruits = ["apple", "banana", "mango", "orange", "grapes"]
i = 0
while i < 3:
    print(fruits[i])
    i += 1

# Print a list in reverse order using a while loop.
numbers = [10, 20, 30, 40, 50]
i = len(numbers) - 1
while i >= 0:
    print(numbers[i])
    i -= 1

# Find the length of a list using len() and use it with a while loop.
fruits = ["apple", "banana", "mango", "orange", "grapes"]
length = len(fruits)
i = 0
while i < length:
    print(fruits[i])
    i += 1