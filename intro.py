# A basic python program

# Note input() always grab terminal data as a String
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# int() converts its parameter/agrment to an integer
birth_year = int(input("Enter your birth year: "))
age = 2024 - birth_year

#print(first_name, last_name, age)
message = f"Hello ({first_name}{last_name}. \nYou are {age} years old.)"
print(message)

if age >= 19:
    print("You are old enough to drink!")
else: 
    print("You are not old enough to drink!")