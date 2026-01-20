swamp_grid = [
    [
		{
            'description': ['Go back and find the entrance!\n'],
            'random_battle': True,
            'battle_chance': 1,
            'enemy_options': [2],
            'options': [2],
            'block_value': 'KEY_SHED',
            'unlock_value': {
                'value': 'CASTLE_KEY',
                'display': False
            },
            'alt_pathway': {
              'alt_description': '',
              'description': ['The shed only has the goblin you slayed. I guess you can only go back now.\n'],
              'random_battle': False,
              'options': [2],
              'first_unlock': 'KEY_SHED',
              'unlock_value': None
            }
        },{
            'description': "HOLDER",
            'options': []
        },{
            'description': ['\n\nThis is the entrance to the moat.\n'],
            'random_battle': False,
            'options': [],
            'unlock_value': 'VICTORY'
        },{
            'description': ["HOLDER"],
            'options': []
        },{
            'description': ['You\'ve got your potions filled up. You can only head south...\n'],
            'random_battle': False,
            'options': [2],
            'unlock_value': None,
            'dispenser': {
              'item_type': 'potions' 
            }
        }
    ],
    [
    	{
            'description': ["You see a shed to the north and the clearing to the east that you just came from.\n"],
            'random_battle': True,
            'battle_chance': 2,
            'enemy_options': [1],
            'options': [1, 3],
            'unlock_value': None
        },{
            'description': ["You're in a clearing.\n","To the northwest you see a shed, but your only way to it is west through a suspicious marsh.\n","To the south is a field of long grass.\n","To the east is the moat entrance."],
            'random_battle': False,
            'options': [0, 2, 3],
            'unlock_value': None
        },{
            'description': [
              "To the north you see a castle, but the bridge to cross the moat is raised.\n",
              "You see a slot for a key, but you have none.\n",
              "To the North by Northwest you see a shed, but west is your only way there.\n",
              "To the south you see the Wharg-ridden entrance. \n",
              "Off to the east, you see various structures.\n",
              "What will you do?\n"],
            'random_battle': False,
            'options': [0, 2, 3],
            'unlock_value': None,
            'block_value': 'CASTLE_KEY',
            'alt_pathway': {
              'alt_description': [
                'As you insert and twist your key into the slot, the earth rumbles\n',
                'You step back as the bridge comes crashing down.\n',
                'You now have a way to cross the bridge!\n',
                'What will you do?\n'],
              'description': ['You now have a way to cross the bridge! Where will you go?\n'],
              'random_battle': False,
              'unlock_value': None,
              'options': [0, 1, 2, 3],
              'first_unlock': 'CASTLE_UNLOCK',
            }
        },{
            'description': [
              'To the west is the moat entrance.\n',
              'To the Northeast and Southeast are structures.\n',
              'Where will you go?\n'
              ],
            'random_battle': True,
            'battle_chance': 2,
            'enemy_options': [1],
            'options': [0, 3],
            'unlock_value': None
        },{
            'description': [
              'Back west is the suspicious field and beyond is the moat entrance.\n',
              'To the North you see a carriage.\n',
              'To the south, there appears to be a large chest...\n'
            ],
            'random_battle': False,
            'options': [0, 1, 2],
            'unlock_value': None
        }
    ],
    [
		{
            'description': [
              'The cave is a dead end. You can only go East towards the long grass...\n'
            ],
            'random_battle': True,
            'battle_chance': 2,
            'enemy_options': [1],
            'options': [3],
            'unlock_value': None
        },{
            'description': [
              'To the west is a mysterious cave.\n',
              'To the north is a clearing\n'
            ],
            'random_battle': True,
            'battle_chance': 2,
            'enemy_options': [1],
            'options': [0, 1],
            'unlock_value': None
        },{
            'description': [
              'To the north is a castle.\n',
              'To the east is a small batch of trees.\n',
              'What will you do?\n'
            ],
            'random_battle': True,
            'battle_chance': 2,
            'enemy_options': [1],
            'options': [1, 3],
            'unlock_value': None
        },{
            'description': ['The trees are a dead end. You can only go west to the swamp entrance.\n'],
            'random_battle': False,
            'options': [0],
            'unlock_value': None
        },{
            'description': ['The chest is empty. Only makes sense to head back north\n'],
            'random_battle': True,
            'battle_chance': 1,
            'enemy_options': [11],
            'options': [1],
            'block_value': 'NEW_WEAPON',
            'unlock_value': {
                'value': 'NEW_WEAPON',
                'display': False
            },
            'alt_pathway': {
              'alt_description': [''],
              'description': ['The shed only has the Giant Wharg you slayed. I guess you can only go back now.\n'],
              'random_battle': False,
              'options': [1],
              'first_unlock': 'NEW_WEAPON',
              'block_value': 'NEW_WEAPON',
              'unlock_value': None
            }
        }
    ],
    [
		{
            'description': ["HOLDER"],
            'options': []
        },{
            'description': ["HOLDER"],
            'options': []
        },{
            'description': [
              'You stand before a large swamp.\n',
              'Once you jump in, the only way out is through.\n',
              'What do you do?\n'
            ],
            'random_battle': False,
            'options': [1],
            'unlock_value': None
        },{
            'description': ["HOLDER"],
            'options': []
        },{
            'description': ["HOLDER"],
            'options': []
        }
    ]
]
