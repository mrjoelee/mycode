#!/usr/bin/env python3
"""
Joe | joe.lee@tlgcohort.com
Challenge Range Practice
"""

def main():
    
    while True:
        try:
            #asking user how many times 
            user = int(input("How many bottles of beer would you like to count down from? (Choose from 1 to 100)"))
            #if input is greater than 100 or less than 1 validation
            if(user > 100 or user <1):
                print("Invalid. Please choose from 1 to 100")
                continue
            #if input has characters or strings validation
        except ValueError:
            print("Invalid. No characters, numbers between 1 to 100")
            continue
        #loops - range(start, stop, step) e.g -1 will reverse start (from higher number) 
        for bottles in range(user,0,-1):

            print(f"{bottles} bottles of beer on the wall!")
        break

if __name__ == "__main__":
    main()
                
                    
