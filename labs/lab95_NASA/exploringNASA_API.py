#!/usr/bin/env python3
"""
Joe | joe.lee@tlgcohort.com
Exploring NASA API Key
"""

#importing library for working with HTTP
import urllib.request

#importing pretty print to make json more readable
import pprint

#defining NASA URL
NASA_URL = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

def main():
    """runtime"""
    apodurlobj = urllib.request.urlopen(NASA_URL)

    #Discover the names in the response object.
    dir(apodurlobj)

    #Show the response code attribute that is contained within our object.
    apodurlobj.code

    #Show the response HTTP message attribute that is contained within our object.
    apodurlobj.msg

    #Show the length (octets) contained within the response HTTP message.
    apodurlobj.length

    #displaying the attached json().
    apod = apodurlobj.read().decode("utf-8")

    #pretty print the data structure.
    pprint.pprint(apod)

if __name__ == "__main__":
    main()
