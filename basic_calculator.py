# Basic Python Calculator
# This program performs basic arithmetic operations depending on user inputs

# Get input from the users
num1 = float(input("Enter the first number: "))  # Convert to float to support decimals
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")  # Operation as string

# Perform the operation using if-elif-else
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == "/":
    # Handle division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Error: Invalid operation. Please enter +, -, *, or /.")
