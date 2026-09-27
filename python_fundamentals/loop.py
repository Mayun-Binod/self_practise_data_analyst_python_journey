# Print numbers from 1 to 10.
for i in range(1, 11):
    print(i)

# Print even numbers from 1 to 50.
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# Print odd numbers from 1 to 50.
for i in range(1, 51):
    if i % 2 != 0:
        print(i)

# Print numbers from 10 to 1.
for i in range(10, 0, -1):
    print(i)

# Print the multiplication table of a number.
number = 5
for i in range(1, 11):
    print(number, "x", i, "=", number*i)

# Find the sum of numbers from 1 to 100.
total = 0
for i in range(1, 101):
    total = total + i
print("Sum:", total)
