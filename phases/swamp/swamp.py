import os
import random
import time
from characters.Player import Player
from directions import nav_options
from phases.swamp import swamp_coordinates
from utilities import check_key_items_unlock, get_yes_no
from utility.battle_functions import battle_launch, handle_unlock, use_item
from utility.dispenser_functions import handle_dispenser
from utility.nav_functions import compass_display, navigation_options, reverse_step, show_stats, use_item_nav

def swamp_loop(player: Player, unlocked_values: list[int], location_coords: list[int], is_running: bool) -> bool:
	last_command = None

	# A loop to read a coordinate's description, options for movement
	while is_running:
		os.system('cls')
		# print(f'Last command: {last_command}')
		# print(f'Moving coords: {location_coords}')

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
			for item in location['alt_description']:
				print(item)
				time.sleep(1)
			unlocked_values.append(location['first_unlock'])
			# print(f'Unlocked values: {unlocked_values}')
		else:
			for item in location['description']:
				print(item)
				time.sleep(1)
			# print('\n')

		 # Get the options to display
		text_options = ''
		choice_options = []
		for option in location["options"]:
			text_options = text_options + nav_options.nav_options[option]
			choice_options.append(option)

		items_option = '5 - Check items\n'
		stats_option = '6 - Check stats\n\n'
		text_options = text_options + items_option + stats_option + compass_display(choice_options)
		# print(f'Options: {choice_options}')
		choice = input(text_options)

		if choice:
			if int(choice):
				int_choice = int(choice)
				if int_choice == 5:
					use_item_nav(player)
					continue
				if int_choice == 6:
					os.system('cls')
					show_stats(player)
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