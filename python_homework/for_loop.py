# Print numbers from 1 to 10.
for i in range(1, 11):
    print(i)

# Print numbers from 10 to 1.
for i in range(10, 0, -1):
    print(i)

# Print all even numbers from 1 to 20.
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Print all odd numbers from 1 to 20.
for i in range(1, 21):
    if i % 2 != 0:
        print(i)

# Print the multiplication table of 7.
num = 7
for i in range (1,11):
    print(num,"x",i, "=", num*1)

# Print numbers from 1 to 50 that are divisible by 5.
for i in range(1, 51):
    if i % 5 == 0:
        print(i)

# Find the sum of numbers from 1 to 100.
sum = 0
for i in range(1, 101):
    sum = sum + i
print("Sum =", sum)

# Find the sum of all even numbers from 1 to 50. solve this
sum = 0
for i in range(1, 51):
    if i % 2 == 0:
        sum = sum + i
print("Sum of even numbers =", sum)