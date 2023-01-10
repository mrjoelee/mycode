#!/usr/bin/env pyhon3
"""
Joe | joe.lee@tlgcohort.com
Scripting Commands with Python
"""

#importing additional to complete labs

from subprocess import call

def main():
    """runtime"""   
    # using call, it is possible due to the import from above 
    call(["ip","link","show","up"])

    #simple print function
    print("This program will check your interfaces.")
    
    #prompt the user for an interface
    interface = input("Enter an interface, like, ens3: ")
    
    #using the user input to issue ip addr show dev
    call(["ip", "addr", "show", "dev", interface])

    #using the user input to issue ip route show dev
    call(["ip", "route", "show", "dev", interface])

if __name__=="__main__":
    main()
