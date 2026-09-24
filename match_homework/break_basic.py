# Print numbers from 1 to 10, but stop the loop when the number reaches 6.
for i in range(1, 11):
    if i == 6:
        break
    print(i)

# Ask the user to enter numbers repeatedly. Stop when the user enters 0.
while True:
    numbers = int(input("Enter a number (0 to stop): "))
    if numbers == 0:
        break
    print("You entered:", numbers)

# Print numbers from 1 to 20 and use break to stop when you reach 15.
for i in range(1, 20):
    if i == 15:
        break
    print(i)

# Search for the number 7 in a list. Stop searching once 7 is found.
numbers = [2, 4, 5, 7, 8, 10]
for i in numbers:
    print("Checking:", i)
    if i == 7:
        print("7 found")
        break

# Create a password program that gives the user attempts until the correct password is entered.use break when the password is correct.
correct_password = "python123"
while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Correct password")
        break
    print("Incorrect password")
