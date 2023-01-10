#!/usr/bin/env python3
"""
Joe | joe.lee@tlgcohort.com
using first_module.py """

#importing first_module - should print from first_module
#the name of the import matches the file name (minus the .py)
# these two files MUST BE IN THE SAME DIRECTORY
import first_module

def main():
    first_module.main() # ADD THIS LINE
    
    print("Module #2 Name=", __name__)

if __name__ == "__main__":
    main()

