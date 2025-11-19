level_one_grid = [
  [
    {
        'description': 'Go back and find a stairway!\n',
        'random_battle': True,
        'battle_chance': 1,
        'enemy_options': [4],
        'options': [3],
        'block_value': 'STAIR_KEY',
        'unlock_value': {
            'value': 'STAIR_KEY',
            'display': False
        },
        'alt_pathway': {
        	'alt_description': '',
            'description': 'You already picked up the stair key. Go find some a stairway up.\n',
            'random_battle': False,
            'options': [3],
            'first_unlock': 'STAIR_KEY',
            'unlock_value': None
        }
    },{
        'description': "To the East is a dark room.\nTo the East is another dark room.\nBack south is the large open area you came from.\n",
        'random_battle': True,
        'battle_chance': 2,
        'enemy_options': [2, 11],
        'options': [0, 3],
        'unlock_value': None
    },{
        'description': "The dark room is a dead end...\nYou can only go back West.\n",
        'random_battle': False,
        'options': [0]
    },{
        'description': "HOLDER",
        'options': []
    },{
        'description': "You have the best weapon you can get.\nGo find your way upstairs.",
        'random_battle': True,
        'battle_chance': 1,
        'enemy_options': [4],
        'options': [3],
        'block_value': 'MASTER_WEAPON',
        'unlock_value': {
            'value': 'MASTER_WEAPON',
            'display': False
        },
        'alt_pathway': {
        	'alt_description': '',
            'description': 'You already picked up the master weapon. And there\'s no way to turn off the light.\nGo find a way upstairs.\n',
            'random_battle': False,
            'options': [3],
            'first_unlock': 'MASTER_WEAPON',
            'block_value': 'MASTER_WEAPON',
            'unlock_value': None
        }
    },{
        'description': "To the West you see a room with a glowing light.\nBack East, you hear another critter waiting for you...",
        'random_battle': True,
        'battle_chance': 1,
        'enemy_options': [2, 11],
        'options': [0, 3],
        'unlock_value': None
    },{
        'description': "To the West you see a faint glow in the distance\n But you hear some nasty noises in front of it.\nBack South is the dark room you were attacked in...",
        'random_battle': True,
        'battle_chance': 1,
        'enemy_options': [2, 11],
        'options': [0, 2],
        'unlock_value': None
    }
  ],
]