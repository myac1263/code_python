# A proper divisor of a number is any divisor of that number other than the number itself. 
# For example, the proper divisors of 12 are as follows:  1, 2, 3, 4, 6
# An abundant number occurs when the sum of its proper divisor is greater than the number itself (12 is considered to be abundant)
# A deficient number occurs when the sum of its proper divisor is less than the number itself
# A perfect number occurs when the sum of its proper divisor is equal to the number itself
# Create a program that determines if the inputted number is either abundant, deficient, or perfect.

num = int(input("Enter a number: "))
divider = 1
total = 0 
while divider < num:
    if num % divider == 0:
        total = total + divider #factoring
    divider += 1

if total > num:
    print("Abundant")
elif total == num:
    print("Perfect")
else:
    print("Deficient")