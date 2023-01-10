#!/usr/bin/python3
"""Joe | joe.lee@tlgcohort.com
   Challenge Solution 01 - JSON to CSV, CSV to EXCEL, JSON to EXCEL"""

import pandas

# FROM JSON TO CSV
def main():

    # create a dataframe from json
    df = pandas.read_json("5movies.json")

    # writeout dataframe to CSV
    df.to_csv("5movies-translated-from-json.csv")

if __name__ == "__main__":
    main()
"""
#From CSV to EXCEL
def main():

    # create a dataframe from csv
    df = pandas.read_csv("5movies.csv")

    # writeout dataframe to excel
    df.to_excel("5movies-translated-from-json.xlsx")

# FROM JSON TO EXCEL
def main():

    # create a dataframe from json
    df = pandas.read_json("5movies.json")

    # writeout dataframe to excel
    df.to_excel("5movies-translated-from-json.xlsx")
"""

