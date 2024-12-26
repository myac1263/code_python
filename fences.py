# You are to create a program that determines how many paint cans we would need.
# Each plank of the fence requires one paint can.
# Your supplier only sells paint cans by the dozen (12) for $14.95.
# There are 3 fenced sections, and their length will be denoted by a series of ‘F’ for each fence plank.
# Output how many cans you’d need, how many paint cans you have leftover, and how much it would cost.

from math import ceil

section_one = input("How many fence planks are there in section one:")
section_two = input("How many fence planks are there in section two:")
section_three = input("How many fence planks are there in section three:")
print(f'{section_one} {section_two} {section_three}')

cans = len(section_one) + len(section_two) + len(section_three) #each length would be the number of fences in that section

boxes = ceil(cans / 12) #ceil allows me to round up
leftover = 12*boxes - cans

total_cost = 14.95 * boxes

print(f"We need {cans} of cans. We would have {leftover} leftovers and it would cost us {total_cost} dollars")