

import os
from characters.Player import Player
from phases.swamp import swamp_coordinates

def swamp_loop(player: Player):
	is_running = True
	moving_coords = [2, 1]
	last_command = None

	# These were for getting access to the new and unlockable areas
	bridge_unlock = False
	first_unlock = True

	# A loop was used movement and locations
	# random encounters were hard wired to the locations
	while is_running:
		os.system('cls')

		# Step 1 get the location with the moving coordinates
		holder = swamp_coordinates.swamp_grid[moving_coords[0]][moving_coords[1]]
