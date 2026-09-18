# Create a list of numbers and add a new number using append().
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

# Add an item at index 2 using insert().
numbers = [10, 20, 30]
numbers.insert(2, 25)
print(numbers)

# Add multiple items using extend().
numbers = [10, 20, 30]
numbers.extend([50, 60, 70])
print(numbers)

# Remove a specific item using remove().
numbers = [10, 20, 30,25]
numbers.remove(25)
print(numbers)

# Remove the last item using pop().
numbers = [10, 20, 30,25]
numbers.pop()
print(numbers)

# Remove an item using its index with pop().
numbers = [10, 20, 30,25]
numbers.pop(1)
print(numbers)

# Empty a list using clear().
numbers = [10, 20, 30,25]
numbers.clear()
print(numbers)

# Sort a list in ascending order using sort().
numbers = [50, 10, 40, 20, 30]
numbers.sort()
print(numbers)

# Sort a list in descending order.
numbers = [50, 10, 40, 20, 30]
numbers.sort(reverse=True)
print(numbers)

# Reverse a list using reverse().
numbers = [50, 10, 40, 20, 30]
numbers.reverse()
print(numbers)

# Find the position of an item using index().
numbers = [10, 20, 30, 40, 50]
print(numbers.index(30))

# Count how many times an item appears using count().
numbers = [10, 20, 10, 30, 10, 40]
print(numbers.count(10))

# Create a copy of a list using copy().
numbers = [10, 20, 30]
new_numbers = numbers.copy()
print(new_numbers)



