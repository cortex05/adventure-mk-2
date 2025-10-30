
import os
import time
from utilities import get_yes_no
from characters.Player import Player
from characters.player_options.Elf import Elf
from characters.player_options.Dwarf import Dwarf
from characters.player_options.Swordsman import Swordsman

descriptions = [
    {
        "name": "Elf",
        "description": '''a woodland sprite who moves fast and uses magic.'''
    },
    {
        "name": "Dwarf",
        "description": '''a sturdy, slow-moving tank.'''
    },
    {
        "name": "Swordsman",
        "description": '''a well balanced fighter.'''
    },
]



def initialiationLoop(name: str) -> Player:
    while True:
        try:
            character_choice = int(input('''
        Please Select your class
        1) Elf
        2) Dwarf
        3) Swordsman
        4) Quit
      \n'''))

            if character_choice in [1, 2, 3]:
                proto_selection = descriptions[character_choice - 1]
                selection = input(
                    f"""
You choose {proto_selection['name']}.

{proto_selection['name']} is {proto_selection['description']}.

Do you wish this to be your character? Y/N 
""")
                if selection.strip().lower() == 'y':
                    if character_choice == 1:
                        return Elf(name)
                    elif character_choice == 2:
                        return Dwarf(name)
                    elif character_choice == 3:
                        return Swordsman(name)
                else:
                    os.system('cls')
                    continue
            elif character_choice == 4:
                print("Goodbye")
                return None
            else:
                os.system('cls')
                print("Please enter a whole number between 1 and 4\n")
                continue
        except ValueError:
            os.system('cls')
            print("Please enter a number")
        continue

    # Should never reach here
    return None


def setPlayerName():
    os.system('cls')
    player_name = input('Please enter your name:\n')

    os.system('cls')
    answer = get_yes_no(f'{player_name}. Is that correct?')
    if answer == 'y':
        print(f'Thank you {player_name}.')
        time.sleep(2)
        return player_name
    if answer == 'n':
        return setPlayerName()


def introScroll(name: str):
    introScrollText = [
        f'Hello {name}. this is the intro scroll.',
        'You are starting on an adventure.',
        'You have to fight through a swamp, cross a moat and enter a castle.',
        'After that, you must find the princess somewhere in the castle.',
        'Take heart, do not despair and step out with determination!'
    ]
    os.system('cls')
    for text in introScrollText:
        print(f'{text} \n')
        time.sleep(2)
    input('Press any button to continue')
    os.system('cls')
