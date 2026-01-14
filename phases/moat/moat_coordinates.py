moat_grid = [
  [
    {
        'description': ['HOLDER'],
        'options': []
    },{
        'description': ['HOLDER'],
        'options': []
    },{
        'description': ['\n\nThis is the castle! You win!\n'],
        'random_battle': False,
        'options': [],
        'unlock_value': 'VICTORY'
    },{
        'description': ['HOLDER'],
        'options': []
    }
  ],
  [
    {
        'description': ['HOLDER'],
        'options': []
    },{
        'description': ['HOLDER'],
        'options': []
    },{
        'description': [
          'To the North is the castle entrance.\n',
          'To the South is the path to the swamp.\n',
          'What will you do?\n'
          ],
        'random_battle': True,
        'battle_chance': 2,
        'enemy_options': [1,2],
        'options': [1, 2],
        'unlock_value': None
    },{
        'description': ['Now that you got the new leg armor, you might as well head back to the bridge.\n'],
        'random_battle': True,
        'battle_chance': 1,
        'enemy_options': [3],
        'options': [2],
        'block_value': 'LEVEL_TWO_LEG_ARMOR',
        'unlock_value': {
            'value': 'LEVEL_TWO_LEG_ARMOR',
            'display': False
        },
        'alt_pathway': {
        	'alt_description': [''],
        	'description': ['You already plundered the leg armor. You can only head back to the bridge.\n'],
        	'random_battle': False,
            'options': [2],
            'first_unlock': 'LEVEL_TWO_LEG_ARMOR',
            'unlock_value': None
        }
    }
  ],
  [
    {
        'description': ['HOLDER'],
        'options': []
    },{
        'description': ['HOLDER'],
        'options': []
    },{
        'description': [
          'The castle is just a little further north.\n',
          'To the east is a perfectly placed series of small islands.\n',
          'South heads backtracks to the swamp.\n'
          ],
        'random_battle': False,
        'options': [1, 2, 3],
        'unlock_value': None
    },{
        'description': [
          'You step onto a small island, to the north is another Island with a small building.\n',
          'Back West is the bridge to the swamp.\n'
          ],
        'random_battle': False,
        'options': [0,1],
        'unlock_value': None
    }
  ],
  [
    {
        'description': [
          'Aaaaand it\'s a dead end.\n',
          'You can only go East over the broken structure to the bridge.\n',
          'What will you do?\n'
          ],
        'random_battle': True,
        'battle_chance': 1,
        'enemy_options': [2],
        'options': [3],
        'unlock_value': None
    },{
        'description': [
          'The shed is one trek to the West away.\n',
          'East is back to the bridge.'
          ],
        'random_battle': True,
        'battle_chance': 2,
        'enemy_options': [2],
        'options': [0,3],
        'unlock_value': None
    },{
        'description': [
          'To the West, in the distance, is a shed on a broken structure.\n',
          'To the North is a long path to the Castle.\n',
          'The South leads back to the Northern Swamp Entrance.\n',
          'What will you do?\n'
          ],
        'random_battle': True,
        'battle_chance': 2,
        'enemy_options': [1,2],
        'options': [0,1,2],
        'unlock_value': None
    },{
        'description': ['HOLDER'],
        'options': []
    }
  ],
  [
    {
        'description': ['HOLDER'],
        'options': []
    },{
        'description': ['HOLDER'],
        'options': []
    },{
        'description': [
          'You\'re on the bridge to cross the moat.\n',
          'The only way is through... Or you can go back to the swamp.\n',
          'What will you do?\n'
          ],
        'random_battle': False,
        'options': [1,2],
        'unlock_value': None
    },{
        'description': ['HOLDER'],
        'options': []
    }
  ],[
    {
        'description': ['HOLDER'],
        'options': []
    },{
        'description': ['HOLDER'],
        'options': []
    },{
        'description': ['HOLDER'],
        'options': [],
        'unlock_value': 'BACK_TO_SWAMP'
    },{
        'description': ['HOLDER'],
        'options': []
	},{
        'description': ['HOLDER'],
        'options': []
    }
  ]

]