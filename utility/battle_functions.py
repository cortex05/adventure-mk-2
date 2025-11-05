import os
import random
from characters.Enemy import Enemy
from characters.Player import Player
from characters.enemy_options import Duke, Dragon, Sorcerer, Wharg


def random_enemy():
    enemy_selector = random.randint(1, 4)
    enemy = None

    if enemy_selector == 1:
        enemy = Duke.Duke()
    elif enemy_selector == 2:
        enemy = Dragon.Dragon()
    elif enemy_selector == 3:
        enemy = Sorcerer.Sorcerer()
    elif enemy_selector == 4:
        enemy = Wharg.Wharg()

    return enemy

def battle_loop(player: Player, enemy: Enemy):
    while True:
        print(f'What will {player.name} do?\n')
        # print(f'Coordinates: {swamp_coordinates.grid[0][0]}')
        selection = int(input(
            '''1 - Attack!\n2 - Check stats\n3 - Go Back\n4 - Quit\n'''))

        if selection == 1:
            damage_dealt = player.strength
            print(f'{player.name} attacks for {damage_dealt}!\n\n')
            if enemy.max_enemy_health - damage_dealt > 0:
                enemy.max_enemy_health = enemy.max_enemy_health - damage_dealt

                enemy_damage = enemy.enemy_attack_damage
                print(f'The {enemy.name} stands strong!\n\n The {enemy.name} attacks for {enemy_damage} damage!\n\n')

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

                # LLevel up here? YES
                return "WIN", player
        elif selection == 2:
            os.system('cls')
            print('Here are the stats:\n\n')
            print(f'You:              {enemy.name}\n\nHealth: {player.health}       {enemy.max_enemy_health}')
            input("\n\nClose?")
            os.system('cls')
        elif selection == 3:
            os.system('cls')
            print('You retreat!')
            return "RETREAT", player    
        elif selection == 4:
            print('Bye\n')
            break
        else:
            print('')
 

def battle_launch(player, unlock_value):
    enemy = random_enemy()
    print(f'{enemy.name_tense} appeared!\n')

    result, player = battle_loop(player, enemy) 

    if result == 'WIN':
        print('You won!\n\n')
        print(f'Your health is {player.health}')

        if unlock_value != None:
            print(f'The {enemy.name} was the guard to the castle gate!\n\n')
            print(f'{enemy.name_tense} dropped a key to the drawbridge!\n')
            print(f'Go back and find the entrance!\n')
            player.inventory["key_items"].append(unlock_value)

        input('Press anything to continue')
        os.system('cls')
        return 'WIN'
    elif result == 'RETREAT':
        # if they retreat,
        print("in the retreat")
        return 'RETREAT'
    elif result == 'LOSE':
        return 'LOSE'
    