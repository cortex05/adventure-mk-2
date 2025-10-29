import os
import time

from utilities import get_yes_no

def setPlayerName():
	os.system('cls')
	player_name = input('Please enter your name:\n')

	os.system('cls')
	answer = get_yes_no(f'{player_name}. Is that correct?')
	if answer == 'y':
		print(f'Thank you {player_name}.')
		time.sleep(2)
		return player_name
	if answer == 'n':
		return setPlayerName()

def introScroll(name: str):
	introScrollText = [
        f'Hello {name}. this is the intro scroll.',
        'You are starting on an adventure.',
        'You have to fight through a swamp, cross a moat and enter a castle.',
        'After that, you must find the princess somewhere in the castle.',
        'Take heart, do not despair and step out with determination!'
    ]
	os.system('cls')
	for text in introScrollText:
		print(f'{text} \n')
		time.sleep(2)
	input('Press any button to continue')	
	os.system('cls')