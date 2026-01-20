import os
import time
from typing import List

from characters.Player import Player
from utilities import get_yes_no
from utility.battle_functions import use_item
from utility.texts import press_any_to_continue


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
        return target, True
    else:
        input(f"Please pick a valid option. {press_any_to_continue}")


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
        if part.level == 2:
            good_armor.append(part.name)

    print('To the North is a stariway up to an intense heat.\n')
    time.sleep(2)
    print('It must be the Dragon...\n')
    time.sleep(3)
    print('Are you ready for this?\n')
    time.sleep(1)
    
    # Armor check
    print('You check your armor.\n')
    time.sleep(2)
    if len(good_armor) == 0:
        print('You are only wearing the most basic armor.\n')
        print('Do you really want to take on a Dragon like this?\n')
        time.sleep(2)
    elif len(good_armor) == 3:
        print('You have the best armor you can get.')
        maxed_out += 1
        time.sleep(2)
    else:
        print(f'You have:')
        for index, armor in enumerate(good_armor):
            if len(good_armor) == 1:
                print(f'a {armor}.\n')
                continue
            elif index == 0:
                print(f'a {armor}.\n')
            elif index + 1 == len(good_armor):
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
    input(press_any_to_continue)
    os.system('cls')
    return
    
def use_item_nav(player: Player):
    os.system('cls')
    print('Here are your items:\n')
    
    key_list = list(player.inventory['consumables'].keys())
    for index, (key, value) in enumerate(player.inventory['consumables'].items()):
        print(f'{index + 1}. {key.capitalize()} - {len(value)}')

    print(f'{len(key_list) + 1}. Nothing\n')
    print('Select an item to inspect or \"Nothing\" to go back.')
    item_choice = None

    while True:
        try:
            item_choice = int(input("Enter an integer: "))
            break
        except ValueError:
            print("Please enter a valid integer.")
							
    if item_choice - 1 < len(key_list) and item_choice - 1 >= 0:
        print('Use item')
        target_key = key_list[item_choice - 1]
        target = player.inventory['consumables'][target_key]
		# Use a potion
		# # print(f'You picked {target.name}\n')
						
        os.system('cls')
        print(f'You picked {target[0].item_name}\n')
        print(f'It is {target[0].description}\n')
						
        answer = get_yes_no(f'Health: {player.health}/{player.base_health}\nDo you want to use it?')
        # print(f'Health: {player.health}/{player.max_health}\n')
        if answer == 'y':
            use_item(player, target[0])
            player.inventory['consumables'][target_key].pop()
        else:
            os.system('cls')
            return
						
        if len(target) == 0:
            del player.inventory['consumables'][target_key]
            print(f'You have no {target_key} left\n')
        else:
            print(f'You have {len(player.inventory["consumables"][target_key])} {target_key} left\n')
							
        time.sleep(2)
        os.system('cls')
        return

    elif item_choice == len(key_list) + 1:
        print('No item')
        input(press_any_to_continue)
        os.system('cls')
        return
    else:
        print('Invalid choice')
        input(press_any_to_continue)
        os.system('cls')
        return

def show_stats(player: Player):
    # stats
    print(f'Your stats:\nHealth: {player.health}/{player.base_health}\nAttack: {player.strength}\nDefense: {player.defense}\nAgility: {player.agility}\n')

    # Level
    print(f'Level: {player.level}\n')

    # Defense
    armor_bonus = player.gear['armor']['head'].defense_bonus + player.gear['armor']['chest'].defense_bonus + player.gear['armor']['legs'].defense_bonus
    defense_drain = player.defense + armor_bonus + ((player.agility // 10) * player.agility)
    print(f'Your total defense bonus is: {defense_drain}\n')

    # Key items
    key_items = player.inventory['key_items']
    print(f'Your Special items:')
    if len(key_items) > 0:
        for item in player.inventory['key_items']:
            print(f'- {item.name}')
    else:
        print('No key items yet...')

    # Armor
    head = player.gear["armor"]["head"]
    chest = player.gear["armor"]["chest"]
    legs = player.gear["armor"]["legs"]
    print(f'\nYour Armor:\n')
    
    print(f'Head: {head.name}\nDefense bonus: {head.defense_bonus}')
    print('--------------------')
    print(f'Chest: {chest.name}\nDefense bonus: {chest.defense_bonus}')
    print('--------------------')
    print(f'Chest: {legs.name}\nDefense bonus: {legs.defense_bonus}\n')

    input(press_any_to_continue)
    os.system('cls')
    return