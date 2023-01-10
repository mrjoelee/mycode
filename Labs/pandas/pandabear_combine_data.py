#!/usr/bin/python3
"""
Joe | joe.lee@tlgcohort.com
Combining JSON File and CSV File into single dataframe using pandas
"""

import pandas as pd

def main():
    #storing the files into variables
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata2.json")

    # display first 5 entries of the ciscocsv dataframe
    print(ciscocsv.head())

    # display first 5 entries of the ciscojson dataframe
    print(ciscojson.head())

    #concatation of both files into 1 by storing into a single variable
    ciscodf = pd.concat([ciscocsv, ciscojson])
    # uncomment the line below to "fix" the index issue
    # ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)

    print(ciscodf)

if __name__ == "__main__":
    main()

