# Create a list of 10 numbers and print every item using a for loop.
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for number in numbers:
    print(number)

# Print only even numbers from a list.
numbers = [10, 15, 20, 25, 30, 35]
for number in numbers:
    if number % 2 == 0:
        print(number)

# Print only odd numbers from a list.
numbers = [10, 15, 20, 25, 30, 35]
for number in numbers:
    if number % 2 != 0:
        print(number)

# Find the sum of all numbers in a list using a loop.
numbers = [10, 20, 30, 40, 50]
total = 0
for i in numbers:
    total = total + i
print(total)

# Find the largest number in a list using a loop.
numbers = [10, 50, 20, 80, 30]
largest = numbers[0]
for i in numbers:
    if number > largest:
        largest = i
print(largest)

# Find the smallest number in a list using a loop.
numbers = [10, 50, 20, 80, 30]
smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print(smallest)

# Count how many positive numbers are in a list.
numbers = [-10, 20, -30, 40, 50, -60]
count = 0
for i in numbers:
    if i > 0:
        count = count + 1
print(count)

# Count how many negative numbers are in a list.
numbers = [10, 20, 30, 40, 50, 60]
count = 0
for i in numbers:
    if i < 0:
        count = count + 1
print(count)

# Create a new list containing only numbers greater than 50.
numbers = [20, 60, 45, 80, 30, 90]
new_list = []
for i in numbers:
    if i > 50:
        new_list.append(number)
print(new_list)


# Print the multiplication of each number in a list by 2.
numbers = [2, 4, 6, 8, 10]
for i in numbers:
    print(i*2)