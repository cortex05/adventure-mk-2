level_one_grid = [
    [
        {
            'description': 'You pick up the key and turn back towards the corridor you came from.\n',
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
        },
        {
            'description': "To the East is a dark room.\nTo the East is another dark room.\nBack south is the large open area you came from.\n",
            'random_battle': True,
            'battle_chance': 2,
            'enemy_options': [2],
            'options': [0, 2, 3],
            'unlock_value': None
        },
        {
            'description': "The dark room is a dead end...\nYou can only go back West.\n",
            'random_battle': False,
            'options': [0],
            'unlock_value': None
        },
        {
            'description': "HOLDER",
            'options': []
        },
        {
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
        },
        {
            'description': "To the West you see a room with a glowing light.\nBack East, you hear another critter waiting for you...",
            'random_battle': True,
            'battle_chance': 1,
            'enemy_options': [2],
            'options': [0, 3],
            'unlock_value': None
        },
        {
            'description': "To the West you see a faint glow in the distance\n But you hear some nasty noises in front of it.\nBack South is the dark room you were attacked in...",
            'random_battle': True,
            'battle_chance': 1,
            'enemy_options': [2],
            'options': [0, 2],
            'unlock_value': None
        }
    ],
    [
        {
            'description': "HOLDER",
            'options': [],
            'unlock_value': 'GO_UPSTAIRS'
        },
        {
            'description': "To the North is a dark Hallway.\nBack South is heads towards the start of a staircase or the entrance.\n",
            'random_battle':  False,
            'options': [1, 2],
            'unlock_value': None
        },
        {
            'description': "HOLDER",
            'options': []
        },
        {
            'description': "HOLDER",
            'options': []
        },
        {
            'description': "HOLDER",
            'options': [],
            'unlock_value': 'GO_UPSTAIRS'
        },
        {
            'description': "The South eventually gives access to some stairs.\nTo the East is a dark corridor perfect for ambushes...\n",
            'random_battle':  False,
            'options': [2, 3],
            'unlock_value': None
        },
        {
            'description': "The corridor continues North. Still perfect for an ambush...\nTo the West is the clearing you first came through.\n",
            'random_battle': True,
            'battle_chance': 1,
            'enemy_options': [2],
            'options': [0, 1],
            'unlock_value': None
        }
    ],
    [
        {
            'description': 'To the north you see stairs to go up, but an iron gate blocks your way.\n You see a slot for a key, but you don\'t have the right one.\nIs this the only way up?\nDown South appears to be a basement.\nBack East is where you came from.\nWhat will you do?',
            'random_battle': False,
            'options': [2, 3],
            'unlock_value': None,
            'block_value': 'STAIR_KEY',
            'alt_pathway': {
                'alt_description': 'You insert your jeweled key and step back\nThe iron gate lowers, revealing the stairs to the next level!\n',
                'description': 'The stairway is open!\nYou can go North to the next level\nOr you can go South to what looks like a basement.\nOr you can head East back towards a fork in the path.',
                'random_battle': False,
                'unlock_value': None,
                'options': [1, 2, 3],
                'first_unlock': 'GO_UPSTAIRS',
            }
        },
        {
            'description': "To the West is the entrance to a staircase.\nTo the North, you can a room in the distance.\nEast heads towards the winding hallway from the entrance.\n",
            'random_battle': True,
            'battle_chance': 1,
            'enemy_options': [2],
            'options': [0, 1, 3],
            'unlock_value': None
        },
        {
            'description': "West leads to a large open area that branches in two directions.\nSouth leads to a corner in the path.\n",
            'random_battle':  False,
            'options': [0, 2],
            'unlock_value': None
        },
        {
            'description': "South leads back to the entrance. West leads to a staircase!.\n",
            'random_battle':  False,
            'options': [2, 3],
            'unlock_value': None
        },
        {
            'description': 'To the north you see stairs to go up, but an iron gate blocks your way.\n You see a slot for a key, but you don\'t have the right one.\nIs this the only way up?\nBack West leads towards the entrance.\nEast leads to a corner of this open area.\nWhat will you do?',
            'random_battle': False,
            'options': [0, 3],
            'unlock_value': None,
            'block_value': 'SECOND_STAIR_KEY',
            'alt_pathway': {
                'alt_description': 'You insert your jeweled key and step back\nThe iron gate lowers, revealing the stairs to the next level!\n',
                'description': 'The stairway is open!\nYou can go North to the next level\nOr you can go West towards the entrance.\nEast leads to a corner of this open area.\n',
                'random_battle': False,
                'unlock_value': None,
                'options': [0, 1, 3],
                'first_unlock': 'SECOND_UPSTAIRS',
            }
        },
        {
            'description': "Back West leads to a staircase.\nNorth leads to a corner of the large area you are in.\n",
            'random_battle': True,
            'battle_chance': 1,
            'enemy_options': [2],
            'options': [0, 1],
            'unlock_value': None
        },
        {
            'description': "HOLDER",
            'options': []
        }
    ],
    [
        {
            'description': "You have a great helmet.\nTime to find your way upstairs.",
            'random_battle': True,
            'battle_chance': 1,
            'enemy_options': [4],
            'options': [1],
            'block_value': 'LEVEL_TWO_HELMET_ARMOR',
            'unlock_value': {
                'value': 'LEVEL_TWO_HELMET_ARMOR',
                'display': False
            },
            'alt_pathway': {
                'alt_description': '',
                'description': 'You already picked up the helmet resting here.Go find a way upstairs.\n',
                'random_battle': False,
                'options': [3],
                'first_unlock': 'LEVEL_TWO_HELMET_ARMOR',
                'block_value': 'LEVEL_TWO_HELMET_ARMOR',
                'unlock_value': None
            }
        },
        {
            'description': "HOLDER",
            'options': []
        },
        {
            'description': "North leads to a corner of the hallway you are in.\nBack East is the Castle Entrance.\n",
            'random_battle': True,
            'battle_chance': 2,
            'enemy_options': [2],
            'options': [1, 3],
            'unlock_value': None
        },
        {
            'description': "West leads to a turn.\nNorth leads to another turn.\nEast leads to a long hallway with multiple enemies in the way...\n",
            'random_battle': False,
            'options': [0, 1, 3],
            'unlock_value': None
        },
        {
            'description': "You dust yoursef off.\nBack West is the Castle entrance.\nEast leads to more enemies, but maybe there's something beyond...\n",
            'random_battle': True,
            'battle_chance': 1,
            'enemy_options': [2],
            'options': [0, 3],
            'unlock_value': None
        },
        {
            'description': "You dust yoursef off.\nBack West is the Castle entrance, but there's something creepy in the way.\nYou can hear something up ahead to the East.\n",
            'random_battle': True,
            'battle_chance': 1,
            'enemy_options': [11],
            'options': [0, 3],
            'unlock_value': None
        },
        {
            'description': 'You\'ve got your super potions filled up. You can only head back through the Hallway onslaught\n',
            'random_battle': False,
            'options': [0],
            'unlock_value': None,
            'dispenser': {
                'item_type': 'super_potions'
            }
        }
    ],
    [
        {
            'description': "HOLDER",
            'options': []
        },
        {
            'description': "HOLDER",
            'options': []
        },
        {
            'description': "HOLDER",
            'options': []
        },
        {
        'description': "HOLDER",
        'options': [],
        'unlock_value': 'BACK_TO_BRIDGE'
    },
	{
            'description': "HOLDER",
            'options': []
        },
        {
            'description': "HOLDER",
            'options': []
        },
        {
            'description': "HOLDER",
            'options': []
        }
    ]
]
