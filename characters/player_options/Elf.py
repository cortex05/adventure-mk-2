# ELF
from characters.Player import Player
import os

from items.health.potion import Potion
from items.weapons.starting_weapons import elf_start

class Elf(Player):
    player_class = "Elf"
    standard_attack = "Swipes"
    special_attack = "Precision Arrow"
    heavy_attack = "Drop Kick"
    description = '''a well balanced fighter.'''

    health = 90
    base_health = 90
    strength = 18
    defense = 18
    agility = 40
    agility_bonus = 3

    def __init__(self, name):
        self.name = name
        os.system('cls')

        self.gear["weapons"]["main"] = elf_start
        i = 0
        while i < 3:
            new_potion = Potion()
            if "potions" in self.inventory["consumables"]:
                self.inventory["consumables"]["potions"].append(new_potion)
            else:
                self.inventory["consumables"]["potions"] = [new_potion]
            i += 1

        input(
            f"\nElf Selected! Quick and nimble is the way. Congrats {name}!\nPress any key to continue\n\n")
