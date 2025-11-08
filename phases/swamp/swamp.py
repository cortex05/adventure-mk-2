

import os
from characters.Player import Player
from directions import nav_options
from phases.swamp import swamp_coordinates
from utility.battle_functions import battle_launch
from utility.nav_functions import compass_display, navigation_options, reverse_step


def swamp_loop(player: Player):
	is_running = True
	location_coords = [3, 2]
	last_command = None

	# unlock values
	bridge_unlock = False
	first_unlock = True

	# A loop to read a coordinate's description, options for movement
	while is_running:
		os.system('cls')
		print(f'Last command: {last_command}')
		print(f'Moving coords: {location_coords}')

		# Step 1 get the location with the moving coordinates
		holder = swamp_coordinates.swamp_grid[location_coords[0]][location_coords[1]]

		if 'alt_pathway' in holder and holder['alt_pathway'] and player.inventory["key_items"] and 'CASTLE_GATE' in player.inventory["key_items"]:
            # condition check for if text has gone?
			location = swamp_coordinates.swamp_grid[location_coords[0]][location_coords[1]]['alt_pathway']
			bridge_unlock = True
		else:
			location = swamp_coordinates.swamp_grid[location_coords[0]][location_coords[1]]

		# 2. Check if location is victory location 
		if location['unlock_value'] == 'VICTORY':
			print(location['description'])
			print('Thank you for playing!')
			break

		# 3. Handle random battle
		if location['random_battle']:
			result = battle_launch(player, location['unlock_value'], [4])
			if result == 'LOSE':
				is_running: False
				break
			elif result == 'RETREAT':
				reverse_step(last_command, location_coords)
				continue

		# Special case for the button unlock?
		if bridge_unlock and first_unlock:
			print(location['alt_description'])
			first_unlock = False
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