from characters.Player import Player
from items.health.potion import Potion


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
                print(f'She takes pity on you and gives you {potion_difference} potions!\n')