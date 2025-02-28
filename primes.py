# Prime Factors: the prime numbers that multiply together to give the original number.
# primeFactor(12) → [2,2,3] ; 
# primeFactor(90) → [2,3,3,5] ; 
# primeFactor(100) → [2,2,5,5] ;
# Write a program that outputs the prime factors of a number. Assume that the inputted number is an integer, positive and greater than 1.


num = int(input("Enter a positive number: "))
a_list = []
while num % 2 == 0:
    a_list.append(2)
    num = num // 2
if num > 1:
    divider = 3
    while num != 1:
        if num % divider == 0:
            a_list.append(divider)
            num == num // divider
        else:
            divider += 2
print(f"Prime Factor of {num}: {a_list}")