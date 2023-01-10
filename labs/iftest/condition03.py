#!/usr/bin/env python3

"""
if else 
"""
def main():
    
    #asking for hostname
    hostname = input("What value should we set for hostname?")
    ## Notice how the next line has changed
    ## here we use the str.lower() method to return a lowercase string
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print("hostname matches config")

    print("Exiting the script")
if __name__ == "__main__":
    main()
