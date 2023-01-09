#!/usr/bin/python3
"""Joe | joe.lee@tlgcohort.com
Class Inheritance
"""

# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    def get_dice(self): # returns the dice rolls
        return self.dice

# allows user to turn their last roll into a 6
class Cheat_Swapper(Player):  # inheritance of Player
    def cheat(self):
        self.dice[-1] = 6

# allows user to increase all rolls if they were less than a 6
class Cheat_Loaded_Dice(Player): # inheritance of Player
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1

#take a mulligan (re-roll if total dice sum is less than 9)
class Mulligan(Player):
    def cheat(self):
        #if the sum of the (3) dices is less than or equal to 9, re-roll again
        if sum(self.dice) <= 9:
            #clears the current dice
            self.dice = []
            for i in range(3):
                self.dice.append(random.randint(1,6))

