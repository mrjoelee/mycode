#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | joe.lee@tlgcohort.com"""

import json
import random
import time
import sys

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

#json file for rooms
def rooms():
    #opens the file and read and loads the rooms
    with open("room.json", "r") as load_room:
        return json.load(load_room)

def attack_damage():
    return random.randint(4,25)

# an inventory, which is initially empty
inventory = []


## A dictionary linking a room to other rooms, coming from room.json file.
rooms = rooms()

#rooms = {
#
#         'Hall' : {
#             'south' : 'Kitchen',
#             'east'  : 'Dining Room',
#             'item'  : 'key'
#             },
#
#         'Kitchen' : {
#             'north' : 'Hall',
#             'item'  : 'monster',
#             },
#         'Dining Room' : {
#             'west' : 'Hall',
#             'south': 'Garden',
#             'item' : 'potion'
#             },
#         'Garden' : {
#             'north' : 'Dining Room'
#             }
#         }


# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over

while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
    # if they aren't allowed to go that way:
    else:
        print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    player = 100
    monster = 100
    win = False
    ## If a player enters a room with a monster
    # if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    if rooms.get(currentRoom).get('item') == 'monster':
        print('Monster Alert! Get Ready for BATTLE!!!\n')
        #loops through until player is less than 0
        while player > 0 and monster > 0:
            print("You attack the monster\n")
            #monster attack using the attack_damage() function
            monster -= attack_damage()
            #delay 1.5  secs
            time.sleep(1.5)
            print(f'Monster health: {monster}')
            if monster <= 1:
                #setting the win as True
                win = True
                print('You defeated the Monster!! \n')
                #deletes the item monster
                del rooms[currentRoom]['item']
                break
            print("Monster attacks you!\n")
            #player attacks using the attack_damage() function
            player -= attack_damage()
            #delay 1.5 secs
            time.sleep(1.5)
            print(f'Player health: {player}\n')
            if player <= 1:
                #setting the win as False
                win = False
                print('Weakling...Monster has eaten you!\n')
                #deletes the item monster
                del rooms[currentRoom]['item']
                break
        if win == False:
            print('Monster got you, go train more and come back!')
            break
        elif win == True:
            print("After defeating the monster, you have sucessfully escaped the house...You WIN!")
            break

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
