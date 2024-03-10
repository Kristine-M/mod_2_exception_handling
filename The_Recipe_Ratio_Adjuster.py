# Task 1: Start
# Ask the user for the number of servings the recipe is 
# originally for and the number of servings they wish to make.

# Ensure that the user inputs are valid numbers and handle any 
# ValueError that arises from improper input.

def servings():
    try: 
        origin_serve = int(input("What is the original number of servings? "))
        wanted_serve = int(input("What is the number of servings you want? "))
        
        return origin_serve, wanted_serve

    except ValueError:
        
        print("You inputted an invalid number")
        return None, None

# Task 2: Quantity Calculation
# Calculate the adjustment factor by dividing the desired 
# servings by the original servings.

# Use a try block to catch any arithmetic errors that 
# may occur during the calculation.

original, wanted = servings

def adjustment(original, wanted):
    try:
        adjust = wanted / original
        return adjust
        
    except ZeroDivisionError:
        print("The original is a zero, so zero division happened")
        return None
    


# Task 3: Serving Success
# If the calculation is successful, display the adjusted 
# recipe quantities to the user.

# Use a finally block to print a message encouraging the 
# user to enjoy their cooking, regardless of the outcome of the calculation.

def final(original, wanted):
    try:
        adjust = wanted / original
        print(adjust, "Calculation successful")
        
    except ZeroDivisionError:
        print("The original is a zero, so zero division happened")
    
    finally:
        print("Enjoy cooking up a storm!")
        
real_serving = final(original, wanted)