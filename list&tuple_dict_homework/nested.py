# Create a tuple containing three inner tuples.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(numbers)

# Access the first item of the second inner tuple.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(numbers[1][0])

# Access the last item of the third inner list.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(numbers[2][-1])

# Change an item inside an inner list.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
numbers[0][1] = 200
print(numbers)

# Add a new item to an inner list using append().
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
numbers[1].append(70)
print(numbers)

# Delete an item from an inner list using pop().
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
numbers[2].pop(1)
print(numbers)

# Create a nested list of students and access the name of the second student.
students = [
    ["sandhya", 19, "Kathmandu"],
    ["binod", 23, "Pokhara"],
    ["prakriti", 20, "Chitwan"]
]
print(students[1][0])

# Create a nested list of numbers and find the sum of one inner list.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
total = sum(numbers[1])
print(total)