#!/usr/bin/env python3
""" Joe | joe.lee@tlgcohort.com
Lab 48: MINI Project #1: If-Logic-Script
Random Number Guessing Game"""

import random

def main():
    """runtime"""
    
    print("Guess the random Number!\n")
    
    #when the game is ON
    play = True

    # while play is true
    while play:
        try:
            
            print("Generating a random Number, Good luck!\n")
        
            # random number between 1 to 100
            number= random.randint(1,100)

            #how many times it takes the user to guess correctly 
            count= 1
        
            # asking user for a random number
            user_guess= int(input("Choose a number between 1 to 100\n"))
        except ValueError:
            print("Out of bounds. Please choose a number between 1 to 100\n")
            continue
        if user_guess > 100 and user_guess < 1:
            print("Invalid: Choose a number between 1 to 100\n")
            
        #loops until the number is correct
        while user_guess !=number:
      
            count+=1

            #checking if the guess number is equal to the generate number
            if user_guess > (number + 10):
                print("Too High!\n")
        
            elif user_guess < (number - 10):
                print("Too low!\n")

            elif user_guess > number:
                print("Hotness!! -->  but still high!\n")
    
            elif user_guess < number:
                print("Close but --> but still low!\n")

            #asking the user a new put when it's incorrect
            user_guess = int(input("Try again \n"))
    
            #if answere correctly
            if user_guess == number:
                print("You rock! You guessed the number in" , count , "tries!\n")
                

        #count comes to 1 again since it will be a new game
        count=1
        #asking the user if wants to play again or not
        play_again= str(input("Do you want to play again, (Yes/No)\n").lower())
    
        if play_again == "no":

            #if false then loops stop, if true start the game again.
            play = False

if __name__ == "__main__":
    main()
