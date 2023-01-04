#!/usr/bin/python3

"""
Challenge 18 
"""
def main():
        
        ##Ask user's name
        user_name = input("what's your name?\n")

        ##Ask the day of the week
        day_of_week = input("what day is it?\n")

        ##print statement
        print("Hello, " + user_name + "!" + " Happy " + day_of_week) 

# this condition is TRUE when someone calls the script direclty
# this condition is FALSE when someone imports the scrip

if __name__ == "__main__":
    main()

