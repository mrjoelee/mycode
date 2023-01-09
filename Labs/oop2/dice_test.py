#!/usr/bin/python3
"""Joe | joe.lee@tlgcohort.com
Using the class created from cheatdice.py (class, subclass)
"""


# imports from cheadice.py (this is in the local directory)
from cheatdice import Player #class
from cheatdice import Cheat_Swapper #subclass
from cheatdice import Cheat_Loaded_Dice #subclass
from cheatdice import Mulligan #subclass

def main():
    """run-time code"""

    # create two cheater objects
    cheater1 = Cheat_Swapper() # ability is to change 3rd dice roll to 6
    cheater2 = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6
    cheater3 = Mulligan() # re-rolls if the sum is equal or less than 9

    # both players take turns
    cheater1.roll()
    cheater2.roll()
    cheater3.roll()

    # both players use their cheat methods
    cheater1.cheat()
    cheater2.cheat()
    cheater3.cheat()
    #both players use their Mulligan methods



    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")
    print(f"Cheater 3 rolled {cheater3.get_dice()}")

    #total sum of each cheater's dices
    sum_cheater1 = sum(cheater1.get_dice())
    sum_cheater2 = sum(cheater2.get_dice())
    sum_cheater3 = sum(cheater3.get_dice())

    if sum_cheater1 == sum_cheater2 and sum_cheater1 == sum_cheater3 and sum_cheater2 == sum_cheater3 :
        print("Draw!")
    elif sum_cheater1 > sum_cheater2 and sum_cheater1 > sum_cheater3:
        print("Cheater 1 wins!")
    elif sum_cheater2 > sum_cheater1 and sum_cheater2 > sum_cheater3:
        print ("Cheater 2 wins!")
    else:
        print("Cheater 3 wins!")

   # if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
   #     print("Draw!")

   # elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()) and sum( :
   #     print("Cheater 1 wins!")
   # else:
   #     print("Cheater 2 wins!")

if __name__ == "__main__":
    main()

