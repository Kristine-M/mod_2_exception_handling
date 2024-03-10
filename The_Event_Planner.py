# Task 1: Start
# Create a function that accepts a date string from 
# the user and attempts to convert it into a Python datetime object.

# Use a try block to handle the conversion and catch 
# ValueError if the user enters an invalid date format.

from datetime import datetime

def convert_to_datetime(date_string):
    try:
        # Attempt to convert the date string to a datetime object
        datetime_object = datetime.strptime(date_string, "%Y-%m-%d")
        return datetime_object
    
    except ValueError:
        print("Invalid date format. Date must be in the format YYYY-MM-DD.")
        return None
 

# Task 2: Reminder Setup

# If the date conversion is successful, allow the user 
# to set a reminder for the event.
# Use an else block to confirm the reminder setup 
# and display the event date and time back to the user.

date_input = input("Insert a date in the YYYY-MM-DD format: ")

res = convert_to_datetime(date_input)

if res == None:
    print("Wrong format")
else:
    reminder_date = res
    print(reminder_date)
    

# Task 3: User Guidance
# In the except block, provide a clear explanation of 
# the expected date format and prompt the user to try 
# entering the date again.

# Ensure that the user is thanked for using the event 
# planner in a finally block, maintaining a positive user experience.

try:
    date_input = input("Insert a date in the YYYY-MM-DD format: ")

    res = convert_to_datetime(date_input)
    
    print(res)

except ValueError:
    print("Enter in a 4 digit number of the year followed by a dash and a number for the the month followed by the dash and a number of the day")

finally:
    print("Thank you for using the event planner!")