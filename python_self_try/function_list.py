# Create a function that accepts a list and returns its total.
def list_total(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total
print(list_total([10, 20, 30, 40]))

# Create a function that accepts a list and returns the largest number.
def list_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
print(list_largest([10, 50, 20, 30]))

# Create a function that accepts a list and returns the smallest number.
def list_smallest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest
print(list_smallest([10, 5, 20, 30]))

# Create a function that accepts a list and returns the number of even values.
def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count = count + 1
    return count
print(count_even([10, 15, 20, 25, 30]))

# Create a function that accepts a list and returns the sum of positive numbers.
def positive_sum(numbers):
    total = 0
    for number in numbers:
        if number > 0:
            total = total + number
    return total
print(positive_sum([-5, 10, -2, 20, 30]))

# Create a function that accepts a list and returns the average.
def average(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total / len(numbers)
print(average([10, 20, 30, 40]))

# Create a function that accepts a list and returns the second-largest number.
def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]
    for number in numbers:
        if number > largest:
            second = largest
            largest = number
        elif number > second and number != largest:
            second = number
    return second
print(second_largest([10, 50, 20, 40, 30]))


