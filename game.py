from phases.start import  setPlayerName, introScroll, initialiationLoop

def main():
	name = setPlayerName()
	player = initialiationLoop(name)
	introScroll(player.name)
	