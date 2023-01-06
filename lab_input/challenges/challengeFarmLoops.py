#!/usr/bin/env python3
"""
Joe | joe.lee@tlgcohort.com
"Looping with for" Challenge (Farm Loops)"""

def main():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    NE_animals = farms[0]["agriculture"]
    SE_animals = farms[0]["agriculture"]
    W_animals = farms[0]["agriculture"]

    print("NE Farm")
    for farm in NE_animals:
        print(f"{farm}")

    for farm in farms:
        print("-", farm["name"])
        choose = input("Pick a farm!\n")
    
    if farm["name"].lower() == choose.lower():
        for farm in farms:
            print(f"farms[{choose}]['agriculture']")


if __name__ == "__main__":
    main()
