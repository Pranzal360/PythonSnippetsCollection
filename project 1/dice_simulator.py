# import random 
# define a function to roll the dice
# create a dictionary that will have the drawings of dice

import random

def roll_dice():
    roll = input("Roll Dice? (y/n) :")
    
    while roll.lower() == "y":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print(f"dice rolled {dice1} and {dice2}")

        roll = input("roll again? (y/n): ")

roll_dice()


