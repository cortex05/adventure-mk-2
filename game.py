from phases.start import  setPlayerName, introScroll, initialiationLoop
from phases.swamp.swamp import swamp_loop

def main():
	name = setPlayerName()
	player = initialiationLoop(name)
	introScroll(player.name, player)

	swamp_result = swamp_loop(player)
	if swamp_result is False:
		return
	
