# inputs
game1 = input("Enter game1 result: ") # assuming that game result will be either w/l

win_counter = 0
for i in range(6): # range(6) -> 0,1,2,3,4,5
    current_result = input(f"Enter the game {i+1} result:")

    if current_result == "w":
        win_counter += 1 # win_counter = win_counter + 1 
# end of for loop

# processing
group = 0 # this is called a variable initialization, creating it for future use
if win_counter > 4
    group = 1
elif: win_counter > 2
    group = 2
elif: win_counter > 0
    group = 3

# output
if group == 0:
    print("The player is eliminated.")
else:
    print(f'The player is placed in group {group}')