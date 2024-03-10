# Task 1: Start
# Prompt the user to enter their current time and 
# the time zone they want to convert it to.

# Use a try block to attempt the time zone conversion, 
# catching any ValueError associated with an invalid time zone entry.

from datetime import datetime, timezone, timedelta
curr_time = input("Enter current time: ")
target_zone = input("Enter target timezone: ")


def convert(current_time, target_timezone):
    try:
        # Convert the input time to a datetime object
        current_datetime = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")

        # Get the target time zone
        target_timezone_obj = timezone(timedelta(hours=target_timezone))

        # Convert the time to the target time zone
        target_datetime = current_datetime.replace(tzinfo=target_timezone_obj)

        print("Success")
    
    except ValueError:
        print("Error")

# Task 2: Time Conversion
# If the time zone is valid, calculate and display the 
# current time in the specified time zone.

# Use an else block to confirm the successful conversion to the user.



def convert(current_time, target_timezone):
    try:
        # Convert the input time to a datetime object
        current_datetime = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")

        # Get the target time zone
        target_timezone_obj = timezone(timedelta(hours=target_timezone))

        # Convert the time to the target time zone
        target_datetime = current_datetime.replace(tzinfo=target_timezone_obj)

        return target_datetime
    
    except ValueError:
        print("Error")
        return None
    
res = convert(curr_time, target_zone)
    
if res != None:
    print(res)
else:
    
    print("Error Invalid values")

# Task 3: Traveler's Aid
# In the except block, provide a list of valid time zone 
# options and ask the user to select from the list.

# Include a finally block that wishes the user safe travels, 
# ensuring a friendly end to the interaction regardless of the outcome.
curr_time = input("Enter current time: ")
target_zone = input("Enter target timezone: ")

def convert(current_time, target_timezone):
    try:
        # Convert the input time to a datetime object
        current_datetime = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")

        # Get the target time zone
        target_timezone_obj = timezone(timedelta(hours=target_timezone))

        # Convert the time to the target time zone
        target_datetime = current_datetime.replace(tzinfo=target_timezone_obj)

        return target_datetime
    
    except ValueError:
            print("Error")
            print("Valid time zone options: -12 to +12")
            user_timezone = input("Please select a valid time zone from the list: ")
            return convert(current_time, user_timezone)
    finally:
        print("Safe travels")
        
res = convert(curr_time, target_zone)
