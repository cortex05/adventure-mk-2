swamp_grid = [
    [
        {
            'description': 'Can only go south\n',
            'random_battle': True,
            'options': [2],
            'unlock_value': 'CASTLE_GATE'
        }, {
            'description': '\n\nThis is the castle! You win!\n',
            'random_battle': False,
            'options': [0, 2],
            'unlock_value': 'VICTORY'
        }, {
            'description': "HOLDER",
            'options': []
        }],
    [
        {
            'description': "Can only go north or east",
            'random_battle': False,
            'options': [0, 1],
            'unlock_value': None
        }, {
            'description': 'To the north you see a castle, but the bridge to cross the moat is raised.\n You see a slot for a key, but you have none.\nTo the Northwest you see a shed, to the west you see something shiny. Where will you go?\n',
            'random_battle': True,
            'options': [1, 3],
            'unlock_value': None,
            'block_value': 'CASTLE_GATE',
            'alt_pathway': {
              'alt_description': 'As you insert and twist your key into the slot, the earth rumbles \n You step back as the bridge comes crashing down. You now have a way to cross the bridge! What will you do?\n',
              'description': 'You now have a way to cross the bridge! What will you do?\n',
              'random_battle': False,
              'options': [0, 1, 3],
              'unlock_value': None,
            }
        }, {
            'description': "Monster and a dead end",
            'random_battle': False,
            'options': [3],
            'unlock_value': None
        }],
    [
        {
            'description': "Null",
            'options': "Null"
        }, {
            'description': 'You stand before a forest. The only way is through. What do you do?\n',
            'random_battle': False,
            'options': [0],
            'unlock_value': None
        }, {
            'description': "Null",
            'options': "Null"
        }
    ]
]
