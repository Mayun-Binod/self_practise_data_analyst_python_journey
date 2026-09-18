# Create a list of 5 fruits and print the list.
fruits = ["apple", "banana", "cherry", "grape", "orange"]
print(fruits)

# Create a list of 5 numbers and access the first item.
numbers = [10, 20, 30, 40, 50]
print(numbers[0])

# Access the last item using a negative index.
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])

# Access the 2nd and 4th items from a list.
numbers = [10, 20, 30, 40, 50]
print(numbers[1])
print(numbers[3])

# Change the 3rd item of a list.
numbers = [10, 20, 30, 40, 50]
numbers[2] = 100
print(numbers)

# Delete the 2nd item using del.
numbers = [10, 20, 30, 40, 50]
del numbers[1]
print(numbers)

# Find the length of a list using len().
numbers = [10, 20, 30, 40, 50]
print(len(numbers))

# Check whether "apple" exists in a list.
fruits = ["apple", "banana", "mango", "orange"]
print("apple" in fruits)

# Slice a list to get the first 3 items.
numbers = [10, 20, 30, 40, 50]
print(numbers[:3])

# Slice a list to get the last 3 items.
numbers = [10, 20, 30, 40, 50]
print(numbers[-3:])

# Reverse a list using slicing.
numbers = [10, 20, 30, 40, 50]
print(numbers[::-1])
