moat_grid = [
  [
    {
        'description': "HOLDER",
        'options': []
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
    }
  ],[
    {
        'description': "HOLDER",
        'options': []
    },{
        'description': "HOLDER",
        'options': []
    },{
        'description': "You dust yourself off. North or South.",
        'random_battle': True,
        'enemy_options': [4],
        'options': [1, 2],
        'unlock_value': None
    },{
        'description': 'You got the armor!!\n',
        'random_battle': True,
        'enemy_options': [5],
        'options': [2],
        'block_value': 'KEY_SHED',
        'unlock_value': {
            'value': 'CASTLE_KEY',
            'display': False
        },
        'alt_pathway': {
        	'alt_description': '',
        	'description': 'BOSS FOR ARMOR.\n',
        	'random_battle': False,
            'options': [2],
            'first_unlock': 'KEY_SHED',
            'unlock_value': None
        }
    }
  ],[
    {
        'description': "HOLDER",
        'options': []
    },{
        'description': "HOLDER",
        'options': []
    },{
        'description': "North to battle, east to side path, south to battle",
        'random_battle': False,
        'options': [1, 2, 3],
        'unlock_value': None
    },{
        'description': "North to big battle and armor.",
        'random_battle': False,
        'options': [0,1],
        'unlock_value': None
    }
  ],[
    {
        'description': "Aaaaand it's a dead end. You can only go East towards where you were previously attacked...",
        'random_battle': True,
        'enemy_options': [4],
        'options': [3],
        'unlock_value': None
    },{
        'description': "You dust yourself off. West toward battle or east toward battle.",
        'random_battle': True,
        'enemy_options': [4],
        'options': [3],
        'unlock_value': None
    },{
        'description': "You dust yourself off. West toward shed, north toward castle, south toward swamp",
        'random_battle': True,
        'enemy_options': [4],
        'options': [0,1,2],
        'unlock_value': None
    },{
        'description': "HOLDER",
        'options': []
    }
  ],[
    {
        'description': "HOLDER",
        'options': []
    },{
        'description': "HOLDER",
        'options': []
    },{
        'description': 'You\'re on the moat. The only way is through... Or you can go back to the swamp.\n What do you do?\n',
        'random_battle': False,
        'options': [1,2],
        'unlock_value': None
    },{
        'description': "HOLDER",
        'options': []
    }
  ]
]