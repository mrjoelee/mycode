#!/usr/bin/python3
"""
Joe | joe.lee@tlgcohort.com
Using with to open file (reading) 
"""
def main():
    """runtime"""
    # parse keystone.common.wsgi and return number of failed login attempts
    loginfail = 0 # counter for fails
    successful = 0 # counter for successful

    # open the file for reading
    with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

        # loop over the file
        for line in kfile:
            # if this 'fail pattern' appears in the line...
            if "- - - - -] Authorization failed" in line:
                loginfail += 1 # this is the same as loginfail = loginfail + 1
            elif "-] Authorization failed": #can only be true if the "if" is false
                successful += 1 # this is the same as succesful = succesful +1

    #Number of failed log in
    print("The number of failed log in attempts is", loginfail)

    #Number of successful log in
    print("The number of successful log in attempts is", successful)           

if __name__=="__main__":
    main()
