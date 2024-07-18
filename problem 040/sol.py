# Python solution file
import datetime

def find_day_of_week(month, day, year):
    # Create a date object
    date_obj = datetime.date(year, month, day)
    
    # Get the day of the week as an integer (0 = Monday, ..., 6 = Sunday)
    day_of_week = date_obj.weekday()
    
    # Define day names in order
    day_names = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    
    # Return the day of the week in uppercase
    return day_names[day_of_week]

# Reading input
input_date = input().strip()
month, day, year = map(int, input_date.split())

# Find the day of the week
day_of_week = find_day_of_week(month, day, year)

# Print the result
print(day_of_week)
