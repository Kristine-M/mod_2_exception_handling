# Task 1: Start
# Begin by setting up a simple user input loop 
# that asks the user to enter the temperature in Fahrenheit.

# Ensure that your program only accepts numerical input and 
# provides a friendly error message if the user enters something 
# that can't be converted to a number.

while True:
    try:
        fahrenheit_input = int(input("Enter the temperature in fahrenheit: "))

    except ValueError:
        print("Invalid number for the temperature")
        break

# Task 2: Temperature Conversion
# Write a function that converts the Fahrenheit temperature to 
# Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

# Use a try block to catch any potential errors during the conversion 
# process, such as division by zero or overflow errors.

def conversion(fahrenheit):
    
    try:
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    except ZeroDivisionError:
        print("Result is division by zero")
        return None
    except OverflowError:
        print("Overflow errors")
        return None


# Task 3: User Experience
# Implement an else block that prints the converted temperature
# in a user-friendly format.

# Add a finally block that thanks the user for using the weather 
# forecast application, ensuring that this message is displayed 
# regardless of whether an exception was caught or not.

try:
    fahrenheit = int(input("Enter the temperature in Fahrenheit: "))
    
   
    result = conversion(fahrenheit)

    if result is not None:
        print(f"{fahrenheit} converts to {result} Celsius")
    else:
        print("Error check fahrenheit input")

except ValueError:
    print("Invalid number for the temperature")

finally:
    print("Thank you for using the weather forecast application!")