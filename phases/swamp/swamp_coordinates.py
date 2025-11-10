swamp_grid = [
    [
		{
            'description': 'Your only option is to head south. Towards a suspicious marsh...\n',
            'random_battle': True,
            'options': [2],
            'unlock_value': {
              'value': 'CASTLE_KEY',
              'unlocked': False
            }
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
            'description': 'HERE is where we have the potion dispenser. Figure it out\nYou\'ve got your potions set. You can only head south.\n',
            'random_battle': False,
            'options': [2],
            'unlock_value': 'CASTLE_KEY'
        }
    ],
    [
    	{
            'description': "You dust yourself off. You see a shed to the north and the clearing to the east that you just came from.",
            'random_battle': True,
            'options': [1, 3],
            'unlock_value': None
        },{
            'description': "You're in a clearing.\nTo the northwest you see a shed, but your only way to it is west through a suspicious marsh. To the south is a field of long grass. To the east is the moat entrance.",
            'random_battle': False,
            'options': [0, 2, 3],
            'unlock_value': None
        },{
            'description': 'To the north you see a castle, but the bridge to cross the moat is raised.\n You see a slot for a key, but you have none.\nTo the Northwest you see a shed, but west is your only way there.\nTo the south you see the forest you fought a Wharg in. Off to the east, you see various structures.\nWhat will you do?',
            'random_battle': False,
            'options': [0, 2, 3],
            'unlock_value': None,
            'block_value': 'CASTLE_KEY',
            'alt_pathway': {
              'alt_description': 'As you insert and twist your key into the slot, the earth rumbles \n You step back as the bridge comes crashing down. You now have a way to cross the bridge! What will you do?\n',
              'description': 'You now have a way to cross the bridge! Where will you go?\n',
              'random_battle': False,
              'options': [0, 1, 2, 3],
              'first_unlock': 'CASTLE_KEY',
            }
        },{
            'description': "You wipe off your weapon. To the west is the moat entrance. To the north and south east are structures. Where will you go?",
            'random_battle': True,
            'options': [0, 3],
            'unlock_value': None
        },{
            'description': "Back west is field you were attcked in and beyond is the moat. To the North you see a carriage. To the south, there appear to be a large chest...",
            'random_battle': False,
            'options': [0, 1, 2],
            'unlock_value': None
        }
    ],
    [
		{
            'description': "The cave is a dead end. You can only go East towards where you were previously attacked...",
            'random_battle': True,
            'options': [3],
            'unlock_value': None
        },{
            'description': "To the west is a mysterious cave. To the north is a clearing",
            'random_battle': True,
            'options': [0, 1],
            'unlock_value': None
        },{
            'description': "To the north is a castle. To the east is a small batch of trees.",
            'random_battle': True,
            'options': [1, 3],
            'unlock_value': None
        },{
            'description': "The trees are a dead end. You can only go west to the clearing",
            'random_battle': False,
            'options': [0],
            'unlock_value': None
        },{
            'description': "UNLOCK sword or new weapon here. You can only go back to the clearing.",
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
