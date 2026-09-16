# Create two lists and concatenate them using +.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)

# Create a list of numbers and print every item using a for loop.
numbers = [10, 20, 30, 40, 50]
for i in numbers:
    print(i)

# Create a list of numbers and print only even numbers using a loop.
numbers = [10, 15, 20, 25, 30, 35, 40, 45]
for i in numbers:
    if i %2 == 0:
        print(i) 

# Create a list of numbers and print only odd numbers using a loop.
numbers = [10, 15, 20, 25, 30, 35, 40, 45]
for i in numbers:
    if i %2 == 1:
        print(i) 

# Use a loop to calculate the sum of all numbers in a list.
numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total = total + number
print(total)

# Use a loop to find the largest number in a list.
numbers = [25, 10, 80, 45, 60]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print(largest)

# Use a loop to find the smallest number in a list.
numbers = [25, 10, 80, 45, 60]
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print(smallest)

# Use a loop to count how many numbers are greater than 50.
numbers = [20, 65, 45, 80, 90, 30, 55]
count = 0
for i in numbers:
    if i > 50:
        count = count + 1
print(count)
