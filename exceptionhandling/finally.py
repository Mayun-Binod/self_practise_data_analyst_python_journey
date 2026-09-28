# # Ask the user to enter a number and divide 100 by that number.
# # Use finally to display:
# # Program completed.
# # The message should appear whether an error occurs or not.
# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number
#     print("Result:", result)
# except Exception as e:
#     print("Error:", e)
# finally:
#     print("Program completed.")

# Write a program that attempts to open a file named student.txt.
# Use:
# try → open the file
# except → handle FileNotFoundError
# finally → display "File operation completed."
try:
    file = open("student.txt", "r")
    print("File opened successfully.")
    file.close()
except FileNotFoundError:
    print("student.txt was not found.")
finally:
    print("File operation completed.")

