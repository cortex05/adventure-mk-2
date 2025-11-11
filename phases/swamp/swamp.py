

import os
from characters.Player import Player
from directions import nav_options
from phases.swamp import swamp_coordinates
from utilities import check_key_items_unlock
from utility.battle_functions import battle_launch, handle_unlock
from utility.nav_functions import compass_display, navigation_options, reverse_step


def swamp_loop(player: Player):
	is_running = True
	location_coords = [3, 2]
	last_command = None
	unlocked_values = []

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
		else:
			location = holder

		# 2. Check if location is victory location
		if 'unlock_value' in location and location['unlock_value'] == 'VICTORY':
			print(location['description'])
			print('Thank you for playing!')
			break

		# 3. Handle random battle
		if location['random_battle']:
			result = battle_launch(player, [4])
			if result == 'LOSE':
				is_running: False
				break
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

		text_options = text_options + compass_display(choice_options)
		print(f'Options: {choice_options}')
		choice = input(text_options)

		if choice:
			if int(choice):
				int_choice = int(choice)
			else:
				print('Enter a valid option')
				continue

		else:
			print('Enter a valid option')
			# Need validation for bad input to NOT do random encounter again.
			continue

		last_command = navigation_options(int_choice, choice_options, location_coords)