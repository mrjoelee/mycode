#!/usr/bin/env python3
"""
Joe | joe.lee@tlgcohort.com
Challenge: Looping Vampires
"""

def main():
    """runtime"""
    
    #counter for word repition (e.g "vampire")
    count = 0

    #Read in content of the Dracula novel as a file object
    with open("dracula.txt","r") as draculaReader:
        #write in contect of vampytimes
        with open("vampytimes.txt", "a") as vampyReader:
        #read every line of the book
            for line in draculaReader:
                if "vampire" in line.lower(): #making sure it reads all vampire word
                    count+=1
                    
                    print(line, file=vampyReader)

                    #reads the line that consists "vampire" word
                    #print(line)
    print("the word vampire appears in 'Dracula.txt' :",count, "times")
    print("vampytimes.txt file created!")

if __name__ == "__main__":
    main()
