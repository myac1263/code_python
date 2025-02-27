# Write a program to decide if a telephone number is a telemarketer number or not, based on the last four digits. 
# telemarketer number = answer the phone, and otherwise, we should ignore it.

# telemarketers like to use seven-digit phone, and has the last four digits with these characterists: 
#     the first of these four digits is an 8 or 9;
#     the last digit is an 8 or 9;
#     the second and third digits are the same.

phone_num = input("Enter a phone number: ")

if len(phone_num) == 7:
    if phone_num[3] == 8 or phone_num[3] == 9:
        print("Telemarketer number")
    elif phone_num[6] == 8 or phone_num[6] == 9:
        print("Telemarketer number")
    elif phone_num[1] == phone_num[2]:
        print("Telemarketer number")
    else:
        print("Not telemarketer number")