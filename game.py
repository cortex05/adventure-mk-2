import time
from phases.castle.first.level_one import castle_loop
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
	moat_location_coords = [4, 2]

	#castle

	is_running = True

	swamp_result = swamp_loop(player, swamp_unlocked_values, swamp_location_coords, is_running)
	if swamp_result is False:
		print('You have died in the swamp. Game over.')
		time.sleep(2)
		return

	# Moat loop and check
	moat_result = moat_loop(player, moat_unlocked_values, moat_location_coords, is_running, swamp_unlocked_values, swamp_location_coords)
	if moat_result == False:
		print('You have died in the moat. Game over.')
		time.sleep(2)
		return
	
	castle_result = castle_loop(player, is_running, moat_unlocked_values, moat_location_coords, swamp_unlocked_values, swamp_location_coords)
	if castle_result == False:
		print('You have died in the castle. Game over.')
		time.sleep(2)
		return
	else:
		print('Ready for the Dragon!!!!!!!!!')
		time.sleep(2)
	
	# Castle loop and check
