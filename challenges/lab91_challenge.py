#!/usr/bin/env python3
"""
Joe | joe.lee@tlgcohort.com
Lab 91 - Challenge: API Looping
"""
import requests

#import wget


def main():
    """runtime"""
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print(pokeapi)

    #part 1 challenge Slicing(No for loop!)
    print("Sprites - Front_Default")
    print(pokeapi["sprites"]["front_default"])

    #saving as a png
    #print("saving it as a image")
    #wget.download(pokeapi["sprites"]["front_default"], "/home/student/mycode/challenges/lab91_api_looping")


    #par 2 - Slicing with a for loop!
    print("Names of all selected Pokemon's moves")
    for item in pokeapi['moves']:
        print(f"{item['move']['name']}")

    #part 3 - Loop or not Loop

    #without loop
    print("printing how many games the selected Pokemon has been in without using a for loop")
    print(len(pokeapi["game_indices"]))

    #with loop
    #counter
    print("printing how many games the selected Pokemon has been with for loop")
    games = 0

    for game in pokeapi["game_indices"]:
        games += 1

    print(games)

if __name__ =="__main__":
    main()

