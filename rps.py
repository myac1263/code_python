# Create a program that takes one inputs of Rock, Paper, or Scissors to simulate a 1 v AI rock paper scissors game between two people.

from random import choice

invalid = True
player = "" # variable initialization

while invalid:
    # code block for the while loop starts here
    player = input("Enter a choice of (rock, paper, or scissors): ")

    if player in {'rock', 'paper', 'scissors'}:
        #using in operators with sets because faster execution speed
        invalid = False

cpu = choice(['rock', 'paper', 'scissors'])
print(f"The CPU chose {cpu}.")

if player == cpu:
    print("Tie game")
else:
    if player == 'rock':
        if cpu == 'paper':
            print("CPU has won the game.")
        else:
            print("Player has won the game.")
    elif player == 'paper':
        if cpu == 'scissors':
            print("CPU has won the game.")
        else:
            print("Player has won the game.")
    else: #player chose scissors
        if cpu == 'rock':
            print("CPU has won the game.")
        else:
            print("Player has won the game.")


