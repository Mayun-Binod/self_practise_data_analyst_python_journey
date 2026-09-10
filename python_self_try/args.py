# Create a function using *args that prints every argument.
def print_args(*args):
    for value in args:
        print(value)
print_args(10, 20, 30, 40)

# Create a function using *args that returns the total of all numbers.
def args_total(*args):
    total = 0
    for number in args:
        total = total + number
    return total
print(args_total(10, 20, 30, 40))

# Create a function using *args that returns the largest number.
def args_largest(*args):
    largest = args[0]
    for number in args:
        if number > largest:
            largest = number
    return largest
print(args_largest(10, 50, 20, 30))

# Create a function using *args that returns the smallest number.
def args_smallest(*args):
    smallest = args[0]
    for number in args:
        if number < smallest:
            smallest = number
    return smallest
print(args_smallest(10, 5, 20, 30))

# Create a function using *args that counts how many arguments were passed.
def count_args(*args):
    count = 0
    for value in args:
        count = count + 1
    return count
print(count_args(10, 20, 30, 40))

# Create a function using *args that returns the average of all numbers.
def args_average(*args):
    total = 0
    for number in args:
        total = total + number
    return total / len(args)
print(args_average(10, 20, 30, 40))

# Create a function using *args that returns the sum of only even numbers.
def even_sum_args(*args):
    total = 0
    for number in args:
        if number % 2 == 0:
            total = total + number
    return total
print(even_sum_args(10, 15, 20, 25, 30))

# Create a function using *args that returns the sum of only positive numbers.
def positive_sum_args(*args):
    total = 0
    for number in args:
        if number > 0:
            total = total + number
    return total
print(positive_sum_args(-10, 20, 5, 30, 40))

# Create a function using *args that accepts multiple names and prints each name.
def print_names(*args):
    for name in args:
        print(name)
print_names("Binod", "Ram", "Shyam", "Hari")

# Create a function using *args that finds the longest name. solve this
def longest_name(*args):
    longest = args[0]
    for name in args:
        if len(name) > len(longest):
            longest = name
    return longest
print(longest_name("Ram", "Binod", "Sandhya", "shyam"))


