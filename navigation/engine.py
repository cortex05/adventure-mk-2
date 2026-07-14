import os
import random
import time

from directions import nav_options
from utilities import check_key_items_unlock
from utility.battle_functions import battle_launch, handle_unlock
from utility.dispenser_functions import handle_dispenser
from utility.nav_functions import compass_display, show_stats, use_item_nav

# The player still types 1-4 for W/N/S/E; these map that to named exits and to
# the 0-indexed option values the existing compass/nav_options helpers expect.
NUM_TO_NAME = {1: 'west', 2: 'north', 3: 'south', 4: 'east'}
NAME_TO_OPT = {'west': 0, 'north': 1, 'south': 2, 'east': 3}


def _resolve(room, player, unlocked):
	"""Return the gate's alternate room if its requirement is met, else the room."""
	if room.gate is not None:
		if (check_key_items_unlock(player.inventory['key_items'], room.gate.needs)
				or check_key_items_unlock(unlocked, room.gate.needs)):
			return room.gate.opens_to
	return room


def explore(player, phase, unlocked) -> bool:
	"""Generic graph-walk driver. Returns True on phase victory, False on death.
	Replaces the per-phase *_loop functions for the swamp prototype."""
	location = phase.entry
	previous = None

	while True:
		os.system('cls')
		room = _resolve(phase.rooms[location], player, unlocked)

		# Dispensers fire on every visit, matching the grid behaviour.
		if room.dispenser is not None:
			handle_dispenser(player, room.dispenser)

		if room.transition == 'VICTORY':
			print('You\'re out of the Swamp! Now about this large moat...\n')
			time.sleep(2)
			return True

		# Encounter, then any location unlock (fires post-fight, like the grid).
		if room.encounter is not None:
			roll = random.randint(1, room.encounter.battle_chance)
			if roll == room.encounter.battle_chance:
				result = battle_launch(player, room.encounter.enemies)
				if result == 'LOSE':
					return False
				if result == 'RETREAT':
					if previous is not None:
						location = previous
					continue
			if room.unlock is not None:
				handle_unlock(room.unlock, player, unlocked)

		# Selection loop: render, take an action, move.
		moved = False
		while not moved:
			if room.first_token is not None and room.first_token not in unlocked:
				for line in room.on_first_enter:
					print(line)
					time.sleep(1)
				unlocked.append(room.first_token)
			else:
				for line in room.description:
					print(line)
					time.sleep(1)

			choice_options = sorted(NAME_TO_OPT[name] for name in room.exits)
			text = ''
			for opt in choice_options:
				text += nav_options.nav_options[opt]
			text += '5 - Check items\n'
			text += '6 - Check stats\n\n'
			text += compass_display(choice_options)

			choice = input(text)
			if not choice.strip().isdigit():
				print('Enter a valid option')
				time.sleep(1)
				os.system('cls')
				continue

			number = int(choice)
			if number == 5:
				use_item_nav(player)
				os.system('cls')
				continue
			if number == 6:
				os.system('cls')
				show_stats(player)
				continue

			name = NUM_TO_NAME.get(number)
			if name is not None and NAME_TO_OPT[name] in choice_options:
				previous = location
				location = room.exits[name]
				moved = True
			else:
				print('Please pick a valid option.')
				time.sleep(1)
				os.system('cls')
