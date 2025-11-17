from phases.moat.moat import moat_loop
from phases.start import  setPlayerName, introScroll, initialiationLoop
from phases.swamp.swamp import swamp_loop

def main():
	name = setPlayerName()
	player = initialiationLoop(name)
	introScroll(player.name, player)
	# swamp
	swamp_unlocked_values = []
	swamp_location_coords = [3, 2]

	# moat
	moat_unlocked_values = []
	moat_location_coords = [0, 0]
	is_running = True

	swamp_result = swamp_loop(player, swamp_unlocked_values, swamp_location_coords, is_running)
	if swamp_result is False:
		return
	# Moat loop and check
	moat_result = moat_loop(player, moat_unlocked_values, moat_location_coords, is_running)
	if moat_result is False:
		return
	# Castle loop and check
