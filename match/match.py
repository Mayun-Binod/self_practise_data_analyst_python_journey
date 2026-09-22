# MATCH-CASE EXAMPLES
# 1. Day of the Week
day = int(input("\nEnter day number: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")


# 2. Month
month = int(input("\nEnter month number: "))

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid month")


# 3. Simple Calculator
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

match operator:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator")


# 4. Menu System
choice = int(input("\nEnter your choice: "))

match choice:
    case 1:
        print("View Profile")
    case 2:
        print("Update Profile")
    case 3:
        print("Change Password")
    case 4:
        print("Logout")
    case _:
        print("Invalid choice")


# 5. Traffic Light
light = input("\nEnter traffic light: ").lower()

match light:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid traffic light")


# 6. Grade
grade = input("\nEnter your grade: ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")


# 7. User Role
role = input("\nEnter your role: ").lower()

match role:
    case "admin":
        print("You have full access.")
    case "teacher":
        print("You can manage students.")
    case "student":
        print("You can view your courses.")
    case "guest":
        print("You have limited access.")
    case _:
        print("Unknown role")


# 8. Multiple Values in One Case
day = int(input("\nEnter day number: "))

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid day")


# 9. Positive, Negative or Zero
number = int(input("\nEnter a number: "))

match number:
    case n if n > 0:
        print("Positive")
    case n if n < 0:
        print("Negative")
    case 0:
        print("Zero")


# 10. Simple Food Menu
food = input("\nEnter food: ").lower()

match food:
    case "pizza":
        print("Pizza - Rs. 500")
    case "burger":
        print("Burger - Rs. 300")
    case "momo":
        print("Momo - Rs. 150")
    case "chowmein":
        print("Chowmein - Rs. 180")
    case _:
        print("Food not available")