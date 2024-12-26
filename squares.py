# Write a program that inputs the number of tiles and then prints out the maximum side length. 
# You may assume that the number of tiles is less than ten thousand. 

import math

num_tiles = int(input("Input the number of tiles: ")) # int is a typecasting function
side_length =  math.floor(math.sqrt(num_tiles)) #floor rounds a number down to the nearest integer less than or equal to the number
#placing math. infront of the math modulus things (floor, sqrt ...)

print (f"The largest square has side length {side_length}.")