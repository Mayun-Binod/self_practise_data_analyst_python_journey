# Create a list of 5 fruits and print each fruit using a for loop.
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
for fruit in fruits:
    print(fruit)

# Find the largest number in a list.
numbers = [10, 25, 5, 40, 15]
largest = max(numbers)
print(largest)

# Find the smallest number in a list.
numbers = [10, 25, 5, 40, 15]
smallest = min(numbers)
print(smallest)

# Calculate the sum of numbers in a list.
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print(total)

# Count how many even numbers are in a list.
numbers = [10, 15, 20, 25, 30, 35]
count = 0
for number in numbers:
    if number % 2 == 0:
        count += 1
print("Even numbers:", count)

# Add, remove, update, and access elements in a list.
fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
print(fruits[0])
fruits[1] = "Grapes"
fruits.remove("Mango")
print(fruits)

# Create a list and print it in reverse order using a loop.
numbers = [10, 20, 30, 40, 50]
for number in numbers[::-1]:
    print(number)