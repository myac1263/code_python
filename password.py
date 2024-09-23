import random

print ("Welcome to our password generating app!")

pwd_length = int(input("Enter the length of the password: "))

lowercase = list(range(97, 123))
uppercase = list (range(65, 91)) # range never includes the last value
digits = list(range(48, 58))
special = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list (range(123, 127))

pwd_symbols = lowercase.copy() # a list of possible character for our password

has_upper = input("Include uppercase characters? (y/n): ")
if has_upper == "Y" or has_upper == "y" :
    pwd_symbols.extend(uppercase)
    # pwd.symbols = pwd_symbols + uppercase

has_special = input("Include special characters? (y/n): ")
if has_special == "Y" or has_special == "y" :
    pwd_symbols.extend(special)
    # pwd_symbols = pwd_symbols + uppercase

has_digits = input ("Include digits? (y/n): ")
if has_digits == "Y" or has_digits == "y" :
    pwd_symbols.extend(digits)
    # pwd_symbols = pwd_symbols + uppercase

new_password = "" # Empty string to hold our new password

while len(new_password) != pwd_length:
    random_symbol = chr(random.choice(pwd_symbols))
    new_password = new_password + random_symbol
# end of while loop

print(f"{new_password} has been generted.")
