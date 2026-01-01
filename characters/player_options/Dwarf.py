import os
from characters.Player import Player
from items.health.potion import Potion
from items.weapons.starting_weapons import dwarf_start

class Dwarf(Player):
    player_class = "Dwarf"
    standard_attack = "Slash"
    special_attack = "Earth shaker"
    heavy_attack = "Guillotine"
    description = 'A Dwarf is a tank.\n\nNot very agile, but they can eat whatever hits they take and dish it out in kind.\nThey will crush enemies at first, but the tougher ones might be an issue...\n\n'

    health = 120
    base_health = 120
    strength = 50
    defense = 30
    agility = 15
    agility_bonus = 1

    def __init__(self, name):
        self.name = name
        os.system('cls')

        self.gear["weapons"]["main"] = dwarf_start
        i = 0
        while i < 3:
            new_potion = Potion()
            if "Potions" in self.inventory["consumables"]:
                self.inventory["consumables"]["Potions"].append(new_potion)
            else:
                self.inventory["consumables"]["Potions"] = [new_potion]
            i += 1

        input(
            f"\nDwarf Selected! Heavy hitter I see. Congrats {name}!\nPress any key to continue\n\n")