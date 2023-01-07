#!/usr/bin/env python3
"""
Joe | joe.lee@tlgcohort.com
"Looping with for" Challenge (Farm Loops)"""

def main():
    """runtime"""
    #creating a list of farms
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
    
    #bonus part
    #farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
        # {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
        # {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
        # {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


    #storing animals from NE Farm
    NE_animals = farms[0]["agriculture"]

    #displaying all the animals from NE Farm
    for animal in NE_animals:
        print(f"{animal}")
    
    #asking user to choose a farm
    choose = input(f"What farm would like to choose ({farms[0]['name']},{farms[1]['name']},{farms[2]['name']})\n").lower()

    for farm in farms:
        #if the choose is equal to the farm name
        if farm["name"].lower() == choose:
            #print(f"{farm['agriculture']}")

            #storing farm agriculture of the choose input
            agriculture = farm['agriculture']
            
            #looping each agriculture to check if there is a plant
            for item in agriculture:
                if item == "celery" or item == "carrots":
                    continue
                else:
                    #will only print animals
                    print(item)

if __name__ == "__main__":
    main()
