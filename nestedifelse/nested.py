# Nested If-Else Questions with Answers


# 1. Check whether a number is positive or negative.
num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")


# 2. Check whether a person can vote.
age = int(input("\nEnter your age: "))

if age >= 18:
    if age >= 60:
        print("You can vote and you are a senior citizen.")
    else:
        print("You can vote.")
else:
    print("You cannot vote.")


# 3. Check whether a number is even and positive.
num = int(input("\nEnter a number: "))

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")


# 4. Find the greater number between two numbers.
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

if a > b:
    if a > 0:
        print("First number is greater and positive.")
    else:
        print("First number is greater but not positive.")
else:
    if b > 0:
        print("Second number is greater and positive.")
    else:
        print("Second number is greater but not positive.")


# 5. Check username and password.
username = input("\nEnter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Incorrect username.")


# 6. Check eligibility for driving license.
age = int(input("\nEnter your age: "))

if age >= 18:
    if age <= 60:
        print("You are eligible for a driving license.")
    else:
        print("Age is above the allowed range.")
else:
    print("You are not eligible for a driving license.")


# 7. Check student's result.
marks = int(input("\nEnter your marks: "))

if marks >= 40:
    if marks >= 80:
        print("Pass - Excellent.")
    elif marks >= 60:
        print("Pass - Good.")
    else:
        print("Pass.")
else:
    print("Fail.")


# 8. Check whether a number is divisible by 5 and 10.
num = int(input("\nEnter a number: "))

if num % 5 == 0:
    if num % 10 == 0:
        print("The number is divisible by both 5 and 10.")
    else:
        print("The number is divisible by 5 but not by 10.")
else:
    print("The number is not divisible by 5.")


# 9. Check temperature.
temperature = float(input("\nEnter temperature: "))

if temperature >= 0:
    if temperature >= 30:
        print("It is hot.")
    else:
        print("It is normal.")
else:
    print("It is freezing.")


# 10. Simple ATM withdrawal.
balance = float(input("\nEnter your balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount > 0:
    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful.")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance.")
else:
    print("Invalid withdrawal amount.")


# 11. Check student's admission eligibility.
age = int(input("\nEnter your age: "))
marks = int(input("Enter your marks: "))

if age >= 18:
    if marks >= 60:
        print("Eligible for admission.")
    else:
        print("Age is eligible, but marks are not enough.")
else:
    print("Age is not eligible.")


# 12. Check shopping discount.
amount = float(input("\nEnter shopping amount: "))

if amount >= 5000:
    if amount >= 10000:
        discount = amount * 0.20
        print("20% discount.")
    else:
        discount = amount * 0.10
        print("10% discount.")

    final_amount = amount - discount
    print("Final amount:", final_amount)
else:
    print("No discount.")
    print("Final amount:", amount)