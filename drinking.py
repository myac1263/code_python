# You are to create a python program that reads three user inputted data:
# User's first name (Example: "Marshall")
# User's last name (Example: "Park")
# User's birth year (Example: 2020)
# With the given data, the program will greet the user, state their age, and determine if the user is old enough to drink in Ontario, Canada.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: ")) #convert this into an integer using int()
age = 2024 - birth_year

if birth_year <= 2005:
    print(f"Hello {first_name} {last_name}. You are {age} years old. You are old enough to drink!")

if birth_year >= 2005:
    print(f"Hello {first_name} {last_name}. You are {age} years old. You are not old enough to drink!")