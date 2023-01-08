#!/usr/env python3
"""
Joe | joe.lee@tlgcohort.com
Challenge: More Troubleshooting
"""

def main():

    words= {1: "great",
            2: "fabulous",
            3: "super"}

    while True:
        name= input("What is your name?\n>").capitalize()
        num= int(input("Pick a number between 1 and 3: "))

        if name and num in words.keys():
            # Hi <name>! Welcome to Day 2 of Python Training!
            print("Hi " + name + "! Have a " + words[num] + " day!")
            break
        else:
            print("Come on, follow directions. Try again.")
            continue
          # the continue keyword skips over any remaining code and goes back to
          # the beginning of the while loop!

if __name__== "__main__":
    main()
