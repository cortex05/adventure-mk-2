# ELF
from characters.Player import Player
import os


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
        input(
            f"\n Elf Selected! Quick and nimble is the way. Congrats {name}!\n Press any key to continue\n\n")
