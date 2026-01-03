import os
import time
from characters.Player import Player
from directions import nav_options
from phases.castle.second import level_two_coordinates
from utilities import check_key_items_unlock
from utility.battle_functions import handle_unlock
from utility.dispenser_functions import handle_dispenser
from utility.nav_functions import compass_display, dragon_warning, navigation_options, reverse_step, show_stats, use_item_nav


def level_two_loop(player: Player, unlocked_values: list[str], entrance_side: str, is_running: bool) -> str:
	print('Level two of castle reached.')
	last_command = None
	location_coords = [1, 0] if entrance_side == 'WEST' else [0, 4]

	while is_running:
		os.system('cls')
		# print(f'Last command: {last_command}')
		# print(f'Moving coords: {location_coords}')

		holder = level_two_coordinates.level_two_grid[location_coords[0]][location_coords[1]]

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

		if 'unlock_value' in location and location['unlock_value'] == 'TO_WEST_STAIRS_ENTRANCE':
			print('You head downstairs\n')
			time.sleep(2)
			return 'WEST_STAIRS'
		elif 'unlock_value' in location and location['unlock_value'] == 'TO_EAST_STAIRS_ENTRANCE':
			print('You head downstairs\n')
			time.sleep(2)
			return 'EAST_STAIRS'
		elif 'unlock_value' in location and location['unlock_value'] == 'TO_DRAGON':
			reverse_step(last_command, location_coords)
			print('You head up the stairs to the Dragon. Let\'s go!\n')
			time.sleep(2)
			return 'DRAGON'
		
		# Special case for the button unlock?
		if location['unlock_value'] != None:
			handle_unlock(location['unlock_value'], player, unlocked_values)

		# function to unlock values
		if 'first_unlock' in location and location['first_unlock'] not in unlocked_values:
			print(location['alt_description'])
			unlocked_values.append(location['first_unlock'])
			print(f'Unlocked values: {unlocked_values}')
		else:
			# HANDLE WARNING CHECK HERE
			if 'warning_trigger' in location and location['warning_trigger'] is True:
				dragon_warning(player)
			print(location['description'])


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