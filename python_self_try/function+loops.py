# Create a function that prints numbers from 1 to n.
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)
print_numbers(10)

# Create a function that prints even numbers from 1 to n.
def print_even(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)
print_even(10)

# Create a function that prints odd numbers from 1 to n.
def print_odd(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)
print_odd(10)

# Create a function that returns the sum from 1 to n.
# Must use:
# sum = 0
def sum_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum
print(sum_numbers(10))

# Create a function that returns the sum of even numbers from 1 to n.
def sum_even(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum = sum + i
    return sum
print(sum_even(10))

# Create a function that returns the sum of odd numbers from 1 to n.
def sum_odd(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            sum = sum + i
    return sum
print(sum_odd(10))

# Create a function that returns the factorial of a number.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
print(factorial(5))

# Create a function that returns the sum of digits.
# Example:
# Input: 1234
# Output: 10
def sum_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum = sum + digit
        number = number // 10
    return sum
print(sum_digits(1234))


# Create a function that reverses a number.
# Example:
# Input: 12345
# Output: 54321
def reverse_number(number):
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10
    return reverse
print(reverse_number(12345))

# Create a function that checks whether a number is prime.
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
print(is_prime(17))

# Create a function that checks whether a number is a palindrome.
def palindrome(number):
    original = number
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10
    if original == reverse:
        return True
    else:
        return False
print(palindrome(121))












