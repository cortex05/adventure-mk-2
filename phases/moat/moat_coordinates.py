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
  ],
  [
    {
        'description': "HOLDER",
        'options': []
    },{
        'description': "HOLDER",
        'options': []
    },{
        'description': "To the North is the castle entrance. To the South is the path to the swamp.",
        'random_battle': True,
        'battle_chance': 2,
        'enemy_options': [4],
        'options': [1, 2],
        'unlock_value': None
    },{
        'description': 'Now that you got the armor, you might as well head back to the bridge.\n',
        'random_battle': True,
        'battle_chance': 1,
        'enemy_options': [5],
        'options': [2],
        'block_value': 'LEVEL_TWO_ARMOR',
        'unlock_value': {
            'value': 'LEVEL_TWO_ARMOR',
            'display': False
        },
        'alt_pathway': {
        	'alt_description': '',
        	'description': 'You already plundered the armor. You can only head back to the bridge.\n',
        	'random_battle': False,
            'options': [2],
            'first_unlock': 'LEVEL_TWO_ARMOR',
            'unlock_value': None
        }
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
        'description': "The castle is just a little further north.\nTo the east is a perfectly placed series of small islands.\nSouth heads backtracks to the swamp.",
        'random_battle': False,
        'options': [1, 2, 3],
        'unlock_value': None
    },{
        'description': "You step onto a small island, to the north is another Island with a small building.\nBack West is the bridge to the swamp.",
        'random_battle': False,
        'options': [0,1],
        'unlock_value': None
    }
  ],
  [
    {
        'description': "Aaaaand it's a dead end. You can only go East over a treacherous path to the bridge.",
        'random_battle': True,
        'battle_chance': 1,
        'enemy_options': [4],
        'options': [3],
        'unlock_value': None
    },{
        'description': "The shed is one trek to the West away.\nEast is back to the bridge.",
        'random_battle': True,
        'battle_chance': 2,
        'enemy_options': [4],
        'options': [0,3],
        'unlock_value': None
    },{
        'description': "To the West, in the distance, is a shed.\nTo the North is a long path to the Castle.\nThe South leads back to the Northern Swamp Entrance.",
        'random_battle': True,
        'battle_chance': 2,
        'enemy_options': [4],
        'options': [0,1,2],
        'unlock_value': None
    },{
        'description': "HOLDER",
        'options': []
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
        'description': 'You\'re on the bridge to cross the moat. The only way is through... Or you can go back to the swamp.\n What do you do?\n',
        'random_battle': False,
        'options': [1,2],
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
        'description': "HOLDER",
        'options': [],
        'unlock_value': 'BACK_TO_SWAMP'
    },{
      
	},{
        'description': "HOLDER",
        'options': []
    }
  ]

]