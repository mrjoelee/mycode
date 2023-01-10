#!/usr/bin/env python3
"""
Joe | joe.lee@tlgcohort.com
Read From Files
"""

def main():
    """runtime"""
    ######## EXPLORE READ ##########
    ## create file object in "r"ead mode
    configfile = open("vlanconfig.cfg", "r")
    
    ## display file to the screen - .read()
    print(configfile.read())
    
    ## close file
    configfile.close()
    
    ######## EXPLORE READLINES ##########
    ## re-create file object to explore new method
    configfile = open("vlanconfig.cfg", "r")
    
    ## make a list of file lines - .readlines()
    configlist = configfile.readlines()
    print(configlist)
    
    ## Iterate through configlist
    #for x in configlist:
        #print(x, end="") # by default, print() ends in a new line
                         # by passing end = "" print will not "add a second"
                         # newline character

    for x in configlist:
        print(x.strip())   # by default, .strip will remove any whitespace or newline characters
                           # therefore we no longer want to change "end=" from its default setting of
                           # a newline character
    
    ## Always close your file
    configfile.close()

if __name__ == "__main__":
    main()
