from datetime import date

# Input: Date of Birth
year = int(input("Enter birth year (YYYY): "))
month = int(input("Enter birth month (MM): "))
day = int(input("Enter birth day (DD): "))

# Today's date
today = date.today()

# DOB as date object
dob = date(year, month, day)

# Age calculation
age = today.year - dob.year

# Adjust if birthday has not occurred yet this year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("Your age is:", age)
