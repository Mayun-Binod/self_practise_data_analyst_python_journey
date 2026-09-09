# Print numbers from 1 to 10 using a while loop.
i = 1
while i <= 10:
    print(i)
    i += 1

# Print numbers from 10 to 1 using a while loop.
i = 10
while i >= 1:
    print(i)
    i -= 1

# Print even numbers from 1 to 20 using a while loop.
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# Create a countdown from 10 to 1.
i = 10
while i >= 1:
    print(i)
    i -= 1

# Create a program that keeps asking the user for a number until they enter 0.
number = int(input("Enter a number: "))
while number != 0:
    print("You entered:", number)
    number = int(input("Enter a number: "))
print("Program ended")

# Create a password program that keeps asking for the password until the correct password is entered. solve this
password = "python123"
user_password = input("Enter password: ")
while user_password != password:
    print("Incorrect password")
    user_password = input("Enter password: ")

print("Correct password")

