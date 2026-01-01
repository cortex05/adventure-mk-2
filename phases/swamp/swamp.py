import os
import random
import time
from characters.Player import Player
from directions import nav_options
from phases.swamp import swamp_coordinates
from utilities import check_key_items_unlock, get_yes_no
from utility.battle_functions import battle_launch, handle_unlock, use_item
from utility.dispenser_functions import handle_dispenser
from utility.nav_functions import compass_display, navigation_options, reverse_step

def swamp_loop(player: Player, unlocked_values: list[int], location_coords: list[int], is_running: bool) -> bool:
	last_command = None

	# A loop to read a coordinate's description, options for movement
	while is_running:
		os.system('cls')
		print(f'Last command: {last_command}')
		print(f'Moving coords: {location_coords}')

		# Step 1 get the location with the moving coordinates
		holder = swamp_coordinates.swamp_grid[location_coords[0]][location_coords[1]]

		if 'alt_pathway' in holder and holder['alt_pathway']:
			# condition check for if text has gone?
			if check_key_items_unlock(player.inventory["key_items"], holder['block_value']) is True:
				location = holder['alt_pathway']
			elif check_key_items_unlock(unlocked_values, holder['block_value']) is True:
				location = holder['alt_pathway']
			else:
				location = holder
		elif 'dispenser' in holder and holder['dispenser']:
			handle_dispenser(player, holder['dispenser']['item_type'])
			location = holder
		else:
			location = holder

		# 2. Check if location is victory location
		if 'unlock_value' in location and location['unlock_value'] == 'VICTORY':
			reverse_step(last_command, location_coords)
			print('You\'re out of the Swamp! Now about this large moat...\n')
			time.sleep(2)
			return True

		# 3. Handle random battle
		if location['random_battle']:
			fight_roll = random.randint(1, location['battle_chance'])
			if fight_roll == location['battle_chance']:
				result = battle_launch(player, location['enemy_options'])
				if result == 'LOSE':
					is_running = False
					return False
				elif result == 'RETREAT':
					reverse_step(last_command, location_coords)
					continue

		# Special case for the button unlock?
		if location['unlock_value'] != None:
			handle_unlock(location['unlock_value'], player, unlocked_values)

		# function to unlock values
		if 'first_unlock' in location and location['first_unlock'] not in unlocked_values:
			print(location['alt_description'])
			unlocked_values.append(location['first_unlock'])
			print(f'Unlocked values: {unlocked_values}')
		else:
			print(location['description'])

		 # Get the options to display
		text_options = ''
		choice_options = []
		for option in location["options"]:
			text_options = text_options + nav_options.nav_options[option]
			choice_options.append(option)

		items_option = '5 - Check items\n'
		exit_option = '6 - Exit\n'
		# inventory_option = '6 - Check inventory\n'
		# exit_option = '7 - Exit\n'
		text_options = text_options + items_option + exit_option + compass_display(choice_options)
		print(f'Options: {choice_options}')
		choice = input(text_options)

		if choice:
			if int(choice):
				int_choice = int(choice)
				if int_choice == 5:
					# Start
					os.system('cls')
					print('Here are your items:\n')
            
					key_list = list(player.inventory['consumables'].keys())
					for index, (key, value) in enumerate(player.inventory['consumables'].items()):
						print(f'{index + 1}. {key} - {len(value)}')

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
						# # print(f'You picked {target.name}\n')
						
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
					#End
				if int_choice == 6:
					os.system('cls')
					print(f'Your stats:\nHealth: {player.health}\nAttack: {player.strength}\nDefense: {player.defense}\n')
					input('Press any button to continue')
					continue
				elif int_choice in choice_options:
					pass
			else:
				print('Enter a valid option')
				continue

		else:
			print('Enter a valid option')
			# Need validation for bad input to NOT do random encounter again.
			continue

		last_command = navigation_options(int_choice, choice_options, location_coords)