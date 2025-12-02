import os
import time
from typing import List

from characters.Player import Player


def navigation_options(target: int, actual_options: list, moving_coords: list):
    choice = target - 1
    print(f'Modded :{choice}')

    if choice in actual_options:
        if target == 1:
            # West
            moving_coords[1] = moving_coords[1] - 1
        elif target == 2:
            # North
            moving_coords[0] = moving_coords[0] - 1
        elif target == 3:
            # South
            moving_coords[0] = moving_coords[0] + 1
        elif target == 4:
            # East
            moving_coords[1] = moving_coords[1] + 1
        return target
    else:
        input("Please pick a valid option. Press enter to continue")


def reverse_step(last_command, moving_coords):
    if last_command == 1:
        # Came  west, move east
        moving_coords[1] = moving_coords[1] + 1

    elif last_command == 2:
        # Came north, move south
        moving_coords[0] = moving_coords[0] + 1
    elif last_command == 3:
        # was Came south, head north
        moving_coords[0] = moving_coords[0] - 1
    elif last_command == 4:
        # Came east, move west
        moving_coords[1] = moving_coords[1] - 1

def compass_display(options: List[int]):
    one = '1' if 0 in options else ' '
    two = '2' if 1 in options else ' '
    three = '3' if 2 in options else ' '
    four = '4' if 3 in options else ' '
    holder = f'      {two}    \n' + f'      |     \n' + f' {one} ──   ── {four} \n' + f'      {'|'}     \n' + f'      {three}    \n'

    return holder

def dragon_warning(player: Player):
    os.system('cls')

    good_armor = []
    maxed_out = 0
    for part in player.gear['armor'].values():
        if part["level"] == 2:
            good_armor.append(part["name"])

    print('To the North is a staiway up to an intense heat.\n')
    time.sleep(2)
    print('It must be the Dragon...\n')
    time.sleep(3)
    print('Are you ready for this?\n')
    time.sleep(1)
    
    # Armor check
    print('You check your armor.\n')
    time.sleep(2)
    if len(good_armor) == 0:
        print('You are only wearing the most basic armor.')
        print('Do you really want to take on a Dragon like this?\n')
        time.sleep(2)
    elif len(good_armor) == 3:
        print('You have the best armor you can get.')
        maxed_out += 1
        time.sleep(2)
    else:
        print(f'You have:')
        for index, armor in good_armor:
            if index + 1 == len(good_armor):
                print(f' and {armor}.\n')
            else: 
                print(f'{ armor},')
        time.sleep(1)
        print('Which is alright. But there\'s room for improvement.\n')
        time.sleep(2)

    # Weapon check
    print(f'You check your {player.gear["weapons"]["main"]["name"]}.\n')
    if player.gear["weapons"]["main"]['level'] < 3:
        print('It works, but you could do better.\n')
        time.sleep(2)
    else:
        print('This weapon is as good as it gets!\n')
        maxed_out += 1
    time.sleep(2)
    
    # final message
    if maxed_out == 2:
        print('You have the best gear you can get.\n')
        print('You ready for this?\n')
    else:
        print('There\'s still time to get better gear...\n')

    time.sleep(2)
    os.system('cls')
    return
    
