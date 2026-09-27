# Print numbers from 1 to 10 using while.
i = 1
while i <= 10:
    print(i)
    i = i + 1

# Print even numbers from 1 to 50 using while.
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i = i + 1

# Print numbers from 10 to 1 using while.
i = 10
while i >= 1:
    print(i)
    i = i - 1

# Find the sum of numbers from 1 to 100 using while.
i = 1
total = 0
while i <= 100:
    total = total + i
    i = i + 1
print("Sum:", total)

# Print the multiplication table of a number using while. solve this
number = 5
i = 1
while i <= 10:
    print(number, "x", i, "=", number * i)
    i = i + 1