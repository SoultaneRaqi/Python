def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Welcome to the Python Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        operation = input("\nSelect an operation (+, -, *, /) or type 'exit' to quit: ")
        
        if operation.lower() == 'exit':
            print("Thank you for using the calculator!")
            break
        
        if operation in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                if operation == '+':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif operation == '-':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif operation == '*':
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif operation == '/':
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        else:
            print("Invalid operation. Please select one of +, -, *, /.")

# Run the calculator
calculator()
