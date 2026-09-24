# Create a calculator using +, -, *, / with match-case.
number1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
number2 = float(input("Enter second number: "))
match operator:
    case "+":
        print("Result:", number1 + number2)
    case "-":
        print("Result:", number1 - number2)
    case "*":
        print("Result:", number1 * number2)
    case "/":
        if number2 != 0:
            print("Result:", number1 / number2)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator")

# Ask for a traffic-light color and print:
# red → Stop
# yellow → Wait
# green → Go
color = input("Enter traffic light color: ")()
match color:
    case "red":
        print("stop")
    case "yellow":
        print("wait")
    case "green":
        print("go")
    case _:
        print("invalid color")

# Ask the user to enter a number from 1–7 and use match-case to print whether it is a weekday or weekend.
day = int(input("Enter day number (1-7): "))
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("weekday")
    case 6 | 7:
        print("weekend")
    case _:
        print("invalid day")
# Create a restaurant menu using match-case and print the selected food and its price.
choice = int(input("Enter food choice (1-4): "))
match choice:
    case 1:
        print("momo - 150")
    case 2:
        print("chowmein - 120")
    case 3:
        print("pizza - 300")
    case 4:
        print("burger - 200")
    case _:
        print("invalid choice")

# Ask the user to enter a character representing a direction:
# N → North
# S → South
# E → East
# W → West
direction = input("Enter direction (N, S, E, W): ").upper()
match direction:
    case "N":
        print("North")
    case "S":
        print("South")
    case "E":
        print("East")
    case "W":
        print("West")
    case _:
        print("Invalid direction")
