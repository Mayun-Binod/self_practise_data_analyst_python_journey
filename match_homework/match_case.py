# Ask the user to enter a number from 1 to 5 and print the corresponding number in words.
number = int(input("Enter a number (1-5): "))
match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case _:
        print("Invalid number")

# Ask the user to enter a day number (1–7) and print the day name.
day = int(input("Enter day number (1-7): "))
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid day")

# Ask the user to enter a month number (1–12) and print the month name.
month = int(input("Enter month number (1-12): "))
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
# Ask the user to enter a grade (A, B, C, D, F) and print a suitable message.
grade = input("Enter your grade (A, B, C, D, F): ")()
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Needs Improvement")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")

# Create a menu:
# 1 → Add
# 2 → Subtract
# 3 → Multiply
# 4 → Divide
# 5 → Exit
choice = int(input("Enter your choice (1-5): "))
match choice:
    case 1:
        print("Add")
    case 2:
        print("Subtract")
    case 3:
        print("Multiply")
    case 4:
        print("Divide")
    case 5:
        print("Exit")
    case _:
        print("Invalid choice")