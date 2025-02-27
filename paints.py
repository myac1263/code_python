# Peter the painter just finished painting two rectangular paintings and would like to display both on a rectangular wall which has the smallest perimeter possible. 
# The first painting has a base of length A units and a height of length B units. 
# The second painting has a base of length X units and a height of length Y units.

# Peter has a few conditions on how to arrange his paintings on the rectangular wall. 
# condition 1: the paintings must be upright, meaning that the bases of the paintings are parallel to the floor
# condition 2: he would like to display both paintings in full, meaning that they cannot overlap each other. 

# Please help determine the rectangular wall of minimum perimeter such that the paintings can be displayed without violating his conditions.

length_a = int(input("Input base of length A units: "))
length_b = int(input("Input height of length B units: "))
length_x = int(input("Input base of length X units: "))
length_y = int(input("Input height of length Y units: "))

print(f"Inputs: {length_a} {length_b} {length_x} {length_y}")

p1_total_base = (length_a) + (length_x)
p1_total_height = max(length_b, length_y)
p1 = (p1_total_base) + (p1_total_height)

p2_total_height = (length_b) + (length_y)
p2_total_base = max(length_a, length_x)
p2 = (p2_total_base) + (p2_total_height)

if p1 > p2:
    print(f"An optimal arrangement would be with a perimeter of {p2} units, using a base of {p2_total_base} units and a height of {p2_total_height} units")
else:
    print(f"An optimal arrangement would be with a perimeter of {p1} units, using a base of {p1_total_base} units and a height of {p1_total_height} units")

## i could just do all the calculations together to speed up the process instead of seperating each variable
