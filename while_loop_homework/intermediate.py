# Find the sum of all numbers in a list using a for loop.
numbers = [10, 20, 30, 40, 50]
total = 0
for i in numbers:
    total += i
print("total:", total)

# Find the largest number in a list without using max().
numbers = [10, 50, 20, 80, 30]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest:", largest)

# Find the smallest number in a list without using min().
numbers = [10, 50, 20, 80, 30]
smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print("Smallest:", smallest)

# Count how many even numbers are in a list.
numbers = [1, 2, 4, 5, 7, 8, 10]
count = 0
for number in numbers:
    if number % 2 == 0:
        count += 1
print("Even numbers:", count)

# Count how many odd numbers are in a list.
numbers = [1, 2, 4, 5, 7, 8, 10]
count = 0
for number in numbers:
    if number % 2 != 0:
        count += 1
print("Odd numbers:", count)

# Search for a particular item in a list using a for loop.
fruits = ["apple", "banana", "mango", "orange"]
search = "mango"
for fruit in fruits:
    if fruit == search:
        print("search")

# Print only numbers greater than 10 from a list.
numbers = [5, 12, 8, 20, 15, 3]
for i in numbers:
    if i > 10:
        print(i)

# Create a new list containing only even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# Use break to stop searching when a particular item is found.
numbers = [10, 20, 30, 40, 50]
items = 30
for i in numbers:
    if i == items:
        print("Numbers")
        break
    print(i)