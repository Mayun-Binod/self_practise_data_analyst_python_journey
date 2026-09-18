# Create a tuple of 5 numbers and print each number using a for loop.
numbers = (10, 20, 30, 40, 50)
for i in numbers:
    print(i)

# Print only even numbers from a tuple.
numbers = (10, 15, 20, 25, 30, 35)
for number in numbers:
    if number % 2 == 0:
        print(number)

# Print only odd numbers from a tuple.
numbers = (10, 15, 20, 25, 30, 35)
for number in numbers:
    if number % 2 != 0:
        print(number)

# Find the sum of numbers in a tuple using a loop.
numbers = (10, 20, 30, 40, 50)
total = 0
for number in numbers:
    total = total + number
print(total)

# Count how many numbers are greater than 10.
numbers = (5, 15, 8, 20, 25, 3, 30)
count = 0
for number in numbers:
    if number > 10:
        count = count + 1
print(count)
