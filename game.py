from phases.start import  setPlayerName, introScroll, initialiationLoop
from phases.swamp.swamp import swamp_loop

def main():
	name = setPlayerName()
	player = initialiationLoop(name)
	introScroll(player.name, player)
	swamp_unlocked_values = []
	swamp_location_coords = [3, 2]
	is_running = True

	swamp_result = swamp_loop(player, swamp_unlocked_values, swamp_location_coords, is_running)
	if swamp_result is False:
		return
	# Moat loop and check
	# Castle loop and check
