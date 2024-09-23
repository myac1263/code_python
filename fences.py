#Sample Input:
#FF
#FFFF
#FFFFFF

#Sample Output:
#12
#0
#14.95

# import statement
from math import ceil

#input 
section1 = input("Enter 1: ")
section2 = input("Enter 2: ")
section3 = input("Enter 3: ")

#processing
cans = len(section1) + len(section2) + len(section3)

boxes = cail(cans / 12)
leftover = 12*boxes - cans

total_cost = 14,95 * boxes 

# output 
print(f"We need {cans} paint cans.")
print(f"We have {leftover} leftover")
print(f"The project costs ${total_costs}.")