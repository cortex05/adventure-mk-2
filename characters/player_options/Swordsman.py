# swordsman
import os
from characters.Player import Player
from items.health.potion import Potion

from items.weapons.starting_weapons import swordsman_start

class Swordsman(Player):
    player_class = "Swordsman"
    standard_attack = "Slash"
    special_attack = "Overhead Smash"
    heavy_attack = "Thrust"
    description = '''a well balanced fighter.'''

    health = 100
    baseHealth = 100
    strength = 30
    defense = 25
    agility = 20

    def __init__(self, name):
        self.name = name
        os.system('cls')

        self.gear["weapons"]["main"] = swordsman_start
        i = 0
        while i < 3:
            new_potion = Potion()
            self.inventory["consumables"]["potions"].append(new_potion)
            i += 1
        input(
            f"\nSwordsman Selected! Hack and slash it is. Congrats {name}!\nPress any key to continue\n\n")
