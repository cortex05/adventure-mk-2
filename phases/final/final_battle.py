import os
from random import random
import time
from characters.Player import Player
from characters.enemy_options import Dragon
from utilities import get_yes_no
from utility.battle_functions import use_item
from utility.texts import press_any_to_continue


def final_battle(player: Player):
	os.system('cls')
	print('You\'ve stepped into the Dragon\'s Lair.\n')
	time.sleep(2)

	print('It towers above you. The yellow glow of its eyes narrow as it glares at you.\n')
	time.sleep(2)

	print('But fear not, you must defeat it or all is lost.\n')
	time.sleep(2)

	print('Let\'s do this!\n')
	time.sleep(2)

	battle = True
	dragon = Dragon.Dragon()
	armor_bonus = player.gear['armor']['head'].defense_bonus + player.gear['armor']['chest'].defense_bonus + player.gear['armor']['legs'].defense_bonus

	
	while battle:
		# Have options for different descriptions based on health.
		print('The dragon stands before you.\n')
		print('What will you do?\n\n')
		agility = random.randint(player.agility_bonus - 1, player.agility_bonus)
		defense_drain = player.defense + armor_bonus + ((player.agility // 10) * agility)
		
		enemy_damage = dragon.enemy_attack_damage - defense_drain + random.randint(1, dragon.attack_variable)
		if enemy_damage <= 0:
			enemy_damage = random.randint(1, dragon.attack_variable)
		try:
			selection = int(input(
                '''1 - Attack!\n2 - Check stats\n3 - Item\n4 - Quit\n'''))
		except ValueError:
			print("Please enter a number between 1 and 4.")
			time.sleep(2)
			continue
		
		if selection == 1:
			base_damage = player.strength + player.gear['weapons']['main']['attack_boost']
			critical = True if random.randint(1, 100) <= player.agility + player.gear['weapons']['main']['critical_chance'] else False
			damage_dealt  = base_damage * 2 if critical else base_damage

			print(f'{player.name} attacks for {damage_dealt}!\n\n')
			time.sleep(2)

			if dragon.enemy_health - damage_dealt > 0:
				dragon.enemy_health = dragon.enemy_health - damage_dealt
				print(f'The {dragon.name} stands strong!\n\n The {dragon.name} attacks for {enemy_damage} damage!\n\n')
				time.sleep(2)

				if player.health - enemy_damage > 0:
					player.health = player.health - enemy_damage
					input('You stand strong \n')
					input(press_any_to_continue)
					time.sleep(2)
					os.system('cls')
				else:
					print('You are defeated!')
					time.sleep(2)
					return False
			else:
				os.system('cls')
				print(f'The Dragon is defeated!\n')
				time.sleep(2)
				return True
		elif selection == 2:
			os.system('cls')
			print('Here are the stats:\n\n')

			space_length = len(str(player.health)) + len(str(player.base_health))
			empty_space = 12 - space_length
			
			print(
                f'          | You          | {dragon.name}\n\nHealth:   | {player.health}/{player.base_health}{" " * empty_space}| {dragon.enemy_health}/{dragon.max_enemy_health}')
            

			# print(
            #     f'You:              {dragon.name}\n\nHealth: {player.health}       {dragon.max_enemy_health}')
			input("\n\nClose?")
			os.system('cls')
		elif selection == 3:
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

				os.system('cls')
				print(f'You picked {target_key}\n')
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
                    f'The Dragon attacks for {enemy_damage} damage!\n\n')
				
				if player.health - enemy_damage > 0:
					player.health = player.health - enemy_damage
					print('You stand strong \n')
					input(press_any_to_continue)
					time.sleep(2)
					os.system('cls')
				else:
					print('You are defeated!')
					return False
				
				os.system('cls')
				continue
			elif item_choice == len(key_list) + 1:
				print('No item')
				input(press_any_to_continue)
				os.system('cls')
				continue
			else:
				print('Invalid choice')
				input(press_any_to_continue)
				os.system('cls')
				continue

		elif selection == 4:
			print('Bye\n')
			break