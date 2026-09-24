# Print numbers from 1 to 10, but skip number 5.
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Print numbers from 1 to 20, but skip all even numbers.
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)

# Print numbers from 1 to 20, but skip all odd numbers.
for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(i)

# Take 10 numbers from the user and skip negative numbers.
for i in range(10):
    number = int(input("Enter a number: "))
    if number < 0:
        continue
    print("Positive number:", number)

# Print numbers from 1 to 30, but skip numbers divisible by 3. solve this
for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)