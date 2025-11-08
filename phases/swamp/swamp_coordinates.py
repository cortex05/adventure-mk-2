swamp_grid = [
    [
		{
            'description': 'Can only go south\n',
            'random_battle': True,
            'options': [2],
            'unlock_value': 'CASTLE_GATE'
        },{
            'description': "HOLDER",
            'options': []
        },{
            'description': '\n\nThis is the castle! You win!\n',
            'random_battle': False,
            'options': [],
            'unlock_value': 'VICTORY'
        },{
            'description': "HOLDER",
            'options': []
        },{
            'description': 'HERE is where we have the potion dispenser. Figure it out\nCan only go south\n',
            'random_battle': False,
            'options': [2],
            'unlock_value': 'CASTLE_GATE'
        }
    ],
    [
    	{
            'description': "Can only go north or east",
            'random_battle': True,
            'options': [1, 3],
            'unlock_value': None
        },{
            'description': "Options west, south and east",
            'random_battle': False,
            'options': [0, 2, 3],
            'unlock_value': None
        },{
            'description': 'To the north you see a castle, but the bridge to cross the moat is raised.\n You see a slot for a key, but you have none.\nTo the Northwest you see a shed, to the west you see something shiny and to the south you see the marsh you fought a Wharg in. Where will you go?\n',
            'random_battle': False,
            'options': [0, 2, 3],
            'unlock_value': None,
            'block_value': 'CASTLE_GATE',
            'alt_pathway': {
              'alt_description': 'As you insert and twist your key into the slot, the earth rumbles \n You step back as the bridge comes crashing down. You now have a way to cross the bridge! What will you do?\n',
              'description': 'You now have a way to cross the bridge! What will you do?\n',
              'random_battle': False,
              'options': [0, 1, 2, 3],
              'unlock_value': None,
            }
        },{
            'description': "Options west, and east",
            'random_battle': True,
            'options': [0, 3],
            'unlock_value': None
        },{
            'description': "Options west, North, and south",
            'random_battle': False,
            'options': [0, 1, 2],
            'unlock_value': None
        }
    ],
    [
		{
            'description': "Dead end. Can only go East",
            'random_battle': True,
            'options': [3],
            'unlock_value': None
        },{
            'description': "West or north",
            'random_battle': True,
            'options': [0, 1],
            'unlock_value': None
        },{
            'description': "North or east",
            'random_battle': True,
            'options': [1, 3],
            'unlock_value': None
        },{
            'description': "Dead end, west only",
            'random_battle': False,
            'options': [0],
            'unlock_value': None
        },{
            'description': "UNLOCK sword or new weapon here. North only",
            'random_battle': True,
            'options': [1],
            'unlock_value': None
        }
    ],
    [
		{
            'description': "HOLDER",
            'options': []
        },{
            'description': "HOLDER",
            'options': []
        },{
            'description': 'You stand before a forest. The only way is through. What do you do?\n',
            'random_battle': False,
            'options': [1],
            'unlock_value': None
        },{
            'description': "HOLDER",
            'options': []
        },{
            'description': "HOLDER",
            'options': []
        }
    ]
]
