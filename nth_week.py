# Weeks of My Life Calendar
from datetime import datetime

# Birthday in the format (day, month, year)
birthday = (24, 6, 1990) # Enter birth date here.

# Convert the birthday tuple to a datetime object
birthday_date = datetime(birthday[2], birthday[1], birthday[0])

# Get the current date
current_date = datetime.now()

# Calculate the difference between the current date and the birthday
delta = current_date - birthday_date

# Calculate the age in weeks (with seconds for accuracy) and years
age_in_weeks = int(delta.total_seconds() / (7 * 24 * 3600))
age_in_years = delta.days // 365

# Calculate the standard week of the current year
week_of_year_standard = current_date.strftime("%U")

# Calculate the week of the current year (custom definition ending on June 24th)
custom_year_start = datetime(current_date.year, 6, 25)
if current_date < custom_year_start:
    custom_week_of_year = 1
else:
    delta_custom = current_date - custom_year_start
    custom_week_of_year = 1 + int(delta_custom.total_seconds() / (7 * 24 * 3600))

# Calculate the number of weeks until your next birthday (with seconds for accuracy)
next_birthday = birthday_date.replace(year=current_date.year)
if current_date > next_birthday:
    next_birthday = next_birthday.replace(year=current_date.year + 1)
weeks_to_next_birthday = int((next_birthday - current_date).total_seconds() / (7 * 24 * 3600))

# Print the results
print(f"You are {age_in_weeks} weeks old = {age_in_years} years and {weeks_to_next_birthday} weeks until your next birthday.")
print(f"We are currently in week {custom_week_of_year} of the custom year ending on June 24th.")
print(f"We are currently in week {week_of_year_standard} of the standard year.")

