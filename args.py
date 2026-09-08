# Create a function using *args that prints all the numbers provided.
def numbers(*args):
    for i in args:
        print(i)

numbers(10, 20, 30, 40, 50)

# Create a function using *args that returns the sum of all numbers.
def total(*args):
    return sum(args)

result = total(10, 20, 30, 40)
print(result)

# Create a function using *args that returns the largest number.
def largest(*args):
    return max(args)

result = largest(10, 50, 20, 80, 30)
print(result)

# Create a function using *args that counts how many numbers were provided. solve this
def count_numbers(*args):
    return len(args)

result = count_numbers(10, 20, 30, 40, 50)
print(result)


