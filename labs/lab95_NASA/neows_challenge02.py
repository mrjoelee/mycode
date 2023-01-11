#!/usr/bin/python3
"""
Challenge 02 - Try reading the key from an environment variable
"""

import os
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it has been UPDATED to look for the value assigned to the  ENV VAR "NASAKEY"
# if it cannot be found, it will use the value "DEMO_KEY"
def returncreds():
    nasacred = os.getenv("NASAKEY", default="DEMO_KEY")
    nasacred= "api_key=" + nasacred
    return nasacred


# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    #startdate = "start_date=2019-11-11"
    #stardate = input("Please enter a date: format YYYY-MM-DD\n")
    #stardate.strip("\n")

    startdate = ""
    while startdate == "":
       startdate = input("Please enter a date: format YYYY-MM-DD\n")

    startdate = " start_date" + startdate

    enddate = input("What is the end date? YYYY-MM-DD? (press Enter to skip?")
    if enddate:
        enddate = "end_date" + enddate

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    #must have this stuff to make a lookup (at least)
    urltolookup = f'{NEOURL}{startdate}&{nasacreds}'
    #if a enddate was passed in, add it to the url
    if enddate:
        urltolookup = f'{urltolookup}&{enddate}'

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()

