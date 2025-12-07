import time
from characters.Player import Player
from items.health.potion import Potion
from items.health.super_potion import SuperPotion


def handle_dispenser(player: Player, item_type: str):
    if item_type == 'potions':
        print('You see a witch with a carriage full of potions!.\n')
        
        if "potions" not in player.inventory["consumables"]:
            player.inventory["consumables"]["potions"] = []
            
        potion_difference = 3 - len(player.inventory['consumables']['potions'])
        if potion_difference == 0:
            print('The witch tells you that your potions are full and you cannot carry more.\n')
        else:
            i = 1
            while i <= potion_difference: 
                new_potion = Potion()
                player.inventory["consumables"]["potions"].append(new_potion)
                i += 1
            print(f'She takes pity on you and gives you {potion_difference} potion{"s" if potion_difference > 1 else ""}!\n')
    if item_type == 'super_potions':
        print('You see a hole in the wall\nBehind it are a bunch or prisoners who want to help!\n')
        time.sleep(2)
        
        if "super_potions" not in player.inventory["consumables"]:
            player.inventory["consumables"]["super_potions"] = []
            
        potion_difference = 3 - len(player.inventory['consumables']['super_potions'])
        if potion_difference == 0:
            print('They tell you that your super potions are full and you cannot carry more.\n')
        else:
            i = 1
            while i <= potion_difference: 
                new_potion = SuperPotion()
                player.inventory["consumables"]["super_potions"].append(new_potion)
                i += 1
            print(f'They give you {potion_difference} super potion{"s" if potion_difference > 1 else ""} to help you!\n')
            time.sleep(1)
            print('You thank them and let them know you\'ll free them when the Dragon is slain.\n')