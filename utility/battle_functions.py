import os
import random
import time
from typing import List
from characters.Enemy import Enemy
from characters.Player import Player
from characters.enemy_options import Duke, Dragon, GiantWharg, Sorcerer, Warlock, Wharg, Goblin, Guard
from items.armor.armor import leg_armor, helmet_armor, chest_armor
from items.Consumable import Consumable
from items.UnlockValue import UnlockValue
from items.key_items import castle_key, stairs_key
from items.weapons.swamp_upgrade import dwarf_swamp_weapon, elf_swamp_weapon, swordsman_swamp_weapon
from items.weapons.master_weapons import dwarf_master_weapon, elf_master_weapon, swordsman_master_weapon
from utilities import get_yes_no


def random_enemy(options: List[int]):
    # upper = len(options) - 1
    enemy_selector = random.choice(options)
    enemy = None

    if enemy_selector == 1:
        enemy = Wharg.Wharg()
    elif enemy_selector == 2:
        enemy = Goblin.Goblin()
    elif enemy_selector == 3:
        enemy = Duke.Duke()
    elif enemy_selector == 4:
        enemy = Guard.Guard()
    elif enemy_selector == 5:
        enemy = Sorcerer.Sorcerer() 
    elif enemy_selector == 6:
        enemy = Warlock.Warlock()
    elif enemy_selector == 7:
        enemy = Dragon.Dragon()
    #special cases
    if enemy_selector == 11:
        enemy = GiantWharg.GiantWharg()

    return enemy


def battle_loop(player: Player, enemy: Enemy, armor_bonus: int):
    buff_effect = {}
    agility = random.randint(player.agility_bonus - 1, player.agility_bonus)
    defense_drain = player.defense + armor_bonus + ((player.agility // 10) * agility)
    enemy_damage = enemy.enemy_attack_damage - defense_drain + random.randint(1, enemy.attack_variable)
    if enemy_damage <= 0:
        enemy_damage = 0
    while True:
        os.system('cls')
        print(f'What will {player.name} do?\n')
        # print(f'Coordinates: {swamp_coordinates.grid[0][0]}')
        try:
            selection = int(input(
                '''1 - Attack!\n2 - Check stats\n3 - Go Back\n4 - Item\n5 - Quit\n'''))
        except ValueError:
            print("Please enter a number between 1 and 5.")
            time.sleep(2)
            continue

        if selection == 1:
            base_damage = player.strength + player.gear['weapons']['main']['attack_boost']
            critical = True if random.randint(1, 100) <= player.agility + player.gear['weapons']['main']['critical_chance'] else False
            player_damage  = base_damage * 2 if critical else base_damage

            print(f'{player.name} attacks for {player_damage}!\n\n')
            if critical == True:
                time.sleep(1)
                print("Critical hit!\n")
            time.sleep(2)
            if enemy.enemy_health - player_damage > 0:
                enemy.enemy_health = enemy.enemy_health - player_damage

                print(
                    f'The {enemy.name} stands strong!\n')
                print(f'Agility random roll: {agility}\n')
                print(f'The {enemy.name} attacks for {enemy_damage} damage!\n')
                time.sleep(2)
                
                if random.randint(1, 100) <= player.agility:
                    print('You dodged the attack!\n')
                    time.sleep(2)
                else:
                    if player.health - enemy_damage > 0:
                        player.health = player.health - enemy_damage
                        # print('You stand strong.\n\n')
                        input('You stand strong \n')
                        os.system('cls')
                    else:
                        print('You are defeated!')
                        return 'LOSE', player

            else:
                os.system('cls')
                print(f'The {enemy.name} is defeated!\n')
                # print(f'Coordinates: {swamp_coordinates.grid[0][1]}')

                return "WIN", player
        elif selection == 2:
            os.system('cls')
            print('Here are the stats:\n\n')
            space_length = len(str(player.health)) + len(str(player.base_health))
            empty_space = 12 - space_length

            print(
                f'          | You          | {enemy.name}\n\nHealth:   | {player.health}/{player.base_health}{" " * empty_space}| {enemy.enemy_health}/{enemy.max_enemy_health}')
            input("\n\nClose?")
            os.system('cls')
        elif selection == 3:
            os.system('cls')
            print('You retreat!')
            return "RETREAT", player
        elif selection == 4:
            os.system('cls')
            print('Here are your items:\n\n')
            key_list = list(player.inventory['consumables'].keys())
            for index, (key, value) in enumerate(player.inventory['consumables'].items()):
                print(f'{index + 1}. {key}: {len(value)}')
            print(f'{len(key_list) + 1}. Nothing')

            print('What will you do?')
            item_choice = None
            
            while True:
                try:
                    item_choice = int(input("Enter an integer: "))
                    break
                except ValueError:
                    print("Please enter a valid integer.")

            if item_choice - 1 < len(key_list) and item_choice - 1 >= 0:
                print('Use item')
                target_key = key_list[item_choice - 1]
                target = player.inventory['consumables'][target_key]
                # Use a potion
                # print(f'You picked {target.name}\n')

                os.system('cls')
                print(f'You picked {target[0].item_name}\n')
                print(f'It {target[0].description}\n')
                answer = get_yes_no(f'Do you want to use it?')
                if answer == 'y':
                    use_item(player, target[0])
                    player.inventory['consumables'][target_key].pop()
                else:
                    os.system('cls')
                    continue

                if len(target) == 0:
                    del player.inventory['consumables'][target_key]
                    print(f'You have no {target_key} left\n')
                else:
                    print(f'You have {len(player.inventory["consumables"][target_key])} {target_key} left\n')
                
                time.sleep(2)
                print(
                    f'The {enemy.name} attacks for {enemy_damage} damage!\n\n')

                if player.health - enemy_damage > 0:
                    player.health = player.health - enemy_damage
                    # print('You stand strong.\n\n')
                    print('You stand strong \n')
                    time.sleep(2)
                    os.system('cls')
                else:
                    print('You are defeated!')
                    return 'LOSE', player

                os.system('cls')
                continue
            elif item_choice == len(key_list) + 1:
                print('No item')
                input("Press enter to continue...")
                os.system('cls')
                continue
            else:
                print('Invalid choice')
                input("Press any key to continue.")
                os.system('cls')
                continue

        elif selection == 5:
            print('Bye\n')
            break
        else:
            print('')


def battle_launch(player, enemies):
    enemy = random_enemy(enemies)
    print(f'{enemy.name_tense} appeared!\n')
    time.sleep(2)

    armor_bonus = player.gear['armor']['head'].defense_bonus + player.gear['armor']['chest'].defense_bonus + player.gear['armor']['legs'].defense_bonus

    result, player = battle_loop(player, enemy, armor_bonus)

    if result == 'WIN':
        print('You won!\n\n')

        # Here we can add level up logic
        range = [
            enemy.base_experience_yield - enemy.exp_range,
            enemy.base_experience_yield,
            enemy.base_experience_yield + enemy.exp_range
        ]
        yielded_amount = range[random.randint(1,3) - 1]
        print(f'Yield: {yielded_amount}')

        player = level_up(player, yielded_amount)
        print(f'To next level is: {player.to_next_level}')

        print(f'Your health is {player.health}')

        input('Press anything to continue')
        os.system('cls')
        return 'WIN'
    elif result == 'RETREAT':
        # if they retreat,
        print("in the retreat")
        return 'RETREAT'
    elif result == 'LOSE':
        return 'LOSE'


def level_up(player: Player, exp_yield: int):
    # exp_holder = player.to_next_level
    spillover = player.to_next_level - exp_yield

    if player.level == 15:
        print('You have reached the maximum level!\n')
        return player

    if spillover > 0:
        player.to_next_level = spillover
        player.total_experience += exp_yield
        # input("Inside spillover less than, should end")
        return player
    else:
        print('You leveled up!\n')
        # Adjust all attributes
        player.level += 1
        player = class_level_up(player)

        player.total_experience += player.to_next_level
        player.base_level += 10
        player.to_next_level = player.base_level

        if spillover == 0:
            # input("spillover 0 leveled up, should end")
            return player
        else:
            # input("spillover < 0, firing again")
            return level_up(player, abs(spillover))

def class_level_up(player: Player):
    # Elf
    if player.player_class == 'Elf':
        player.base_health = player.base_health + 20
        if player.level % 3 == 0:
            player.defense = player.defense + 5
            player.agility = player.agility + 10
        if player.level % 2 == 0:
            player.strength = player.strength + 4
        
        # Swordsman
    elif player.player_class == 'Swordsman':
        player.base_health = player.base_health + 15
        if player.level % 2 == 0:
            player.defense = player.defense + 5
            player.agility = player.agility + 3
            player.strength = player.strength + 7
        
        #Dwarf
    elif player.player_class == 'Dwarf':
        player.base_health = player.base_health + 10
        if player.level % 2 == 0:
            player.defense = player.defense + 8
            player.agility = player.agility + 3
            player.strength = player.strength + 10

    player.health = player.base_health
    return player

def handle_unlock(unlock_dict: UnlockValue, player: Player, unlocked_values: List[str]):
    # when you unlock something from a battle, you need to handle the location's first unlock here
    if unlock_dict['value'] is 'CASTLE_KEY':
        print('The Goblin was the guard to the castle gate!\n')
        print('The goblin dropped a key to the drawbridge!\n')
        player.inventory["key_items"].append(castle_key)
        unlocked_values.append('KEY_SHED')
        unlocked_values.append('CASTLE_KEY')
        # print(f'PLayer key items: {player.inventory['key_items'][0].name}')
    if unlock_dict['value'] is 'STAIR_KEY':
        print(f'As you wipe the blood off your {player.gear['weapons']['main']['name']}, you see a pedestal. And on it sits a golden, bejeweled key.\n')
        print('This must be for getting upstairs!\n')
        player.inventory["key_items"].append(stairs_key)
        unlocked_values.append('STAIR_KEY')
        unlocked_values.append('SECOND_STAIR_KEY')
    if unlock_dict['value'] is 'NEW_WEAPON':
        old_weapon = player.gear['weapons']['main']['name']
        new_weapon = get_new_weapon(player)
        print('You see a chest before you.')
        print(f'You open it and see a {new_weapon}!')
        print(f'You ditch your {old_weapon} and equip the {new_weapon}')
        print('Now you\'re ready for the big games')
        unlocked_values.append('NEW_WEAPON')
    if unlock_dict['value'] is 'MASTER_WEAPON':
        old_weapon = player.gear['weapons']['main']['name']
        new_weapon = get_master_weapon(player)
        print('The blinding light is coming from a statue.')
        print(f'You see in its outstretched hands is a {new_weapon}!')
        print(f'You ditch your {old_weapon} and equip the {new_weapon}')
        unlocked_values.append('MASTER_WEAPON')
    if unlock_dict['value'] is 'LEVEL_TWO_LEG_ARMOR':
        print('The Duke was guarding Steel Leg armor!\n')
        print('You put it on and are ready for bigger baddies!\n')
        # NEW ARMOR LOGIC HERE
        player.gear['armor']['legs'] = leg_armor
        # print(f'Your leg armor is now {player.gear["armor"]["legs"].name}!')
        # print(f'Your defense is now {player.current_armor + player.gear["armor"]["legs"].defense_bonus}!')
        # print('You can now head back to the bridge.\n')
        unlocked_values.append('LEVEL_TWO_LEG_ARMOR')
    if unlock_dict['value'] is 'LEVEL_TWO_HELMET_ARMOR':
        print('The Sorcerer was guarding Steel Helmet armor!\n')
        print('You dump your cheap helmet and put on the Steel one.\n')
        # NEW ARMOR LOGIC HERE
        player.gear['armor']['head'] = helmet_armor
        # print(f'Your leg armor is now {player.gear["armor"]["legs"].name}!')
        # print(f'Your defense is now {player.current_armor + player.gear["armor"]["legs"].defense_bonus}!')
        # print('You can now head back to the bridge.\n')
        unlocked_values.append('LEVEL_TWO_HELMET_ARMOR')
    if unlock_dict['value'] is 'LEVEL_TWO_CHEST_ARMOR':
        print('What luck?\n')
        print('You see an ornate Tempered Chestplate on a pedaestal before you.\n')
        print('No guards, no Whargs and no Sorcerers.')
        print('You dump your leather chestplate and strap on the tempered one.\n')
        # NEW ARMOR LOGIC HERE
        player.gear['armor']['chest'] = chest_armor
        # print(f'Your leg armor is now {player.gear["armor"]["legs"].name}!')
        # print(f'Your defense is now {player.current_armor + player.gear["armor"]["legs"].defense_bonus}!')
        # print('You can now head back to the bridge.\n')
        unlocked_values.append('LEVEL_TWO_CHEST_ARMOR')



def get_new_weapon(player: Player):
    player_type = player.player_class

    if player_type == 'Dwarf':
        player.gear["weapons"]["main"] = dwarf_swamp_weapon
    elif player_type == 'Elf':
        player.gear["weapons"]["main"] = elf_swamp_weapon
    elif player_type == 'Swordsman':
        player.gear["weapons"]["main"] = swordsman_swamp_weapon
    return player.gear["weapons"]["main"]['name']

def get_master_weapon(player: Player):
    player_type = player.player_class

    if player_type == 'Dwarf':
        player.gear["weapons"]["main"] = dwarf_master_weapon
    elif player_type == 'Elf':
        player.gear["weapons"]["main"] = elf_master_weapon
    elif player_type == 'Swordsman':
        player.gear["weapons"]["main"] = swordsman_master_weapon
    return player.gear["weapons"]["main"]['name']

def use_item(player: Player, item: Consumable):
    if item.type == 'HEALTH':
        health_difference = player.base_health - player.health
        if item.heal_value > health_difference:
            player.health = player.base_health
            print(f'You healed for {health_difference} health!\nYour health is now {player.health}')
        else:
            player.health += item.heal_value
            print(f'You healed for {item.heal_value} health!\nYour health is now {player.health}')
        return

        # player.health += item.heal_value
        # print(f'You used a {item.name} and healed for {item.heal_value} health!')