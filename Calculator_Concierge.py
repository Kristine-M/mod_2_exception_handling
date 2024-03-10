# Task 1: Start
# Set up a calculator that can perform addition, 
# subtraction, multiplication, and division.

# Prompt the user to select an operation and then request two 
# numbers to perform the operation on.

def add(x, y):
    sum =  x + y
    return sum

def subtract(x, y):
    diff = x - y
    return diff

def multiply(x, y):
    product = x * y
    return product

def divide(x, y):
    if y == 0:
        print("Error: Cannot divide by zero.")
        return None
    else:
        quotient = x / y
        return quotient


print("Which operation do you want to do:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter the number: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = 0

if choice == '1':
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")

elif choice == '2':
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")

elif choice == '3':
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")

elif choice == '4':
    result = divide(num1, num2)
    if result is not None:
        print(f"{num1} / {num2} = {result}")


# Task 2: Operation Execution
# For each operation, use a try block to execute the calculation 
# and handle any exceptions that may occur, such as ZeroDivisionError 
# for division operations.

def add(x, y):
    try:
        sum =  int(x + y)
        return sum

    except ValueError:
        print("Invalid value for operation")
        return None


def subtract(x, y):
    try:
        diff = int(x - y)
        return diff
    
    except ValueError:
        print("Invalid value for operation")
        return None
        

def multiply(x, y):
    try:
        product = int(x * y)
        return product
    
    except ValueError:
        print("Invalid value for operation")
        return None

def divide(x, y):
    
    try: 
        quotient = int(x / y)
        return quotient
    
    except ValueError:
        print("Invalid value for operation")
        return None
    
    except ZeroDivisionError:
        print("Result is division by zero")
        return None
    

# Task 3: Polite Error Handling
# In the except blocks, provide friendly error messages that guide 
# the user on what went wrong and how to correct it.
# Include an else block that displays the result of the calculation 
# if everything went smoothly.

def add(x, y):
    try:
        sum =  int(x + y)
        return sum

    except ValueError:
        print("Invalid value for operation. Enter a number")
        return None


def subtract(x, y):
    try:
        diff = int(x - y)
        return diff
    
    except ValueError:
        print("Invalid value for operation. Enter a number")
        return None
        

def multiply(x, y):
    try:
        product = int(x * y)
        return product
    
    except ValueError:
        print("Invalid value for operation. Enter a number")
        return None

def divide(x, y):
    
    try: 
        quotient = int(x / y)
        return quotient
    
    except ValueError:
        print("Invalid value for operation. Enter a number")
        return None
    
    except ZeroDivisionError:
        print("Result is division by zero. Please change the second number to a non zero number")
        return None

print("Which operation do you want to do:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter the number: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = 0

if choice == '1':
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")

elif choice == '2':
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")

elif choice == '3':
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")

elif choice == '4':
    result = divide(num1, num2)
    if result is not None:
        print(f"{num1} / {num2} = {result}")