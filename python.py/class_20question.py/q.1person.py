
from datetime import datetime

class Person:
    def __init__(self, name, country, DOB):
        self.name = name
        self.country = country
        self.DOB = DOB

    def calculate_age(self, today_date):
        age = today_date.year - self.DOB.year - ((today_date.month, today_date.day) < (self.DOB.month, self.DOB.day))
        return age

# Get user input
name = input("Enter your name: ")
country = input("Enter your country: ")

# Get the date of birth as a string and convert it to a datetime object
DOB_str = input("Enter your DOB (YYYY-MM-DD): ")
DOB = datetime.strptime(DOB_str, "%Y-%m-%d")

# Get today's date
today_date = datetime.now()

# Create a Person object
person = Person(name, country, DOB)

# Calculate and display the age
age = person.calculate_age(today_date)
print(f"Age: {age} years")

