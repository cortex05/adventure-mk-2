import os
from characters.Player import Player
from items.health.potion import Potion


class Dwarf(Player):
    player_class = "Dwarf"
    standard_attack = "Slash"
    special_attack = "Earth shaker"
    heavy_attack = "Guillotine"
    description = '''a well balanced fighter.'''

    health = 120
    baseHealth = 120
    strength = 50
    defense = 30
    agility = 15

    def __init__(self, name):
        self.name = name
        os.system('cls')

        i = 0
        while i < 3:
             new_potion = Potion()
             self.inventory["consumables"]["potions"].append(new_potion)
             i += 1

        input(
            f"\nDwarf Selected! Heavy hitter I see. Congrats {name}!\nPress any key to continue\n\n")