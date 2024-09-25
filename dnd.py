# import statement 
from random import randrange

#imput
difficulty = int(input("Enter the DC: "))

#processing & output
player_roll = randrange(1,21) # randrange(a,b) never includes b, only goes up to b

print(f"The player has rolled {player_roll} on their D20")

if player_roll >= difficulty:
    print("The player was successful as {player_roll} >= {difficulty}. ")
else: 
    print("The player was not successful as {player_roll} < {difficulty}. ")