from characters.Player import Player
import os

from items.health.potion import Potion
from items.weapons.starting_weapons import elf_start
from utility.texts import press_any_to_continue

class Elf(Player):
    player_class = "Elf"
    standard_attack = "Swipes"
    special_attack = "Precision Arrow"
    heavy_attack = "Drop Kick"
    description = 'An Elf is quick and nimble.\n\nThey will dodge attacks and land critical hits more often than others.\nThe downside is they are a bit frail and do the least base damage.\nYou will struggle at first, but a veteran Elf is a force to be reckoned with.\n\nRecommended for advanced players.'

    health = 90
    base_health = 90
    strength = 18
    defense = 18
    agility = 40
    agility_bonus = 3
    attack_variable = 8

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
            f"Elf Selected! Quick and nimble is the way. Congrats {name}!\n{press_any_to_continue}")
