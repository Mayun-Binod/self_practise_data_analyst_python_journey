# Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# Print numbers from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

# Print even numbers from 1 to 20   
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# Print odd numbers from 1 to 20
i = 1
while i <= 20:
    if i % 2 == 1:
        print(i)
    i += 1

# Print multiplication table of 5
num = 5
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1