# ELF
from characters.Player import Player
import os

from items.health.potion import Potion


class Elf(Player):
    player_class = "Elf"
    standard_attack = "Swipes"
    special_attack = "Precision Arrow"
    heavy_attack = "Drop Kick"
    description = '''a well balanced fighter.'''

    health = 70
    baseHealth = 70
    strength = 18
    defense = 18
    agility = 40

    def __init__(self, name):
        self.name = name
        os.system('cls')

        i = 0
        while i < 3:
            new_potion = Potion()
            self.inventory["consumables"]["potions"].append(new_potion)
            i += 1

        input(
            f"\nElf Selected! Quick and nimble is the way. Congrats {name}!\nPress any key to continue\n\n")
