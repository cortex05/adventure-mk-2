import os
from characters.Player import Player
from directions import nav_options
from phases.moat import moat_coordinates
from utilities import check_key_items_unlock
from utility.battle_functions import battle_launch, handle_unlock
from utility.dispenser_functions import handle_dispenser
from utility.nav_functions import compass_display, navigation_options, reverse_step


def moat_loop(player: Player, unlocked_values: list[int], location_coords: list[int], is_running: bool) -> bool:
	os.system('cls')
	print("Welcome to the Moat")
	print("This is where you will face your first boss")
	pass