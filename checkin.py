birth_year = int(input("Enter your birth year: "))
current_year = 2024
# birth_year = input()
# birth_year = int(birth_year)

age = current_year - birth_year
if age > 30:
    print(f"You are {age} years old. damn")
else:
    print(f"You are {age} years old.")