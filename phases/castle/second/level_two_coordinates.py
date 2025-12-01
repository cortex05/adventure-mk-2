level_one_grid = [
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
            'options': []
        },
        {
            'description': "You made it to the second floor!\nYou can head back South to the first floor.\nOr you can head East to the Eastern Hallway",
            'random_battle': False,
            'options': [2, 3],
            'unlock_value': None
        },
        {
            'description': "West heads to the stairs downward.\nSouth continues down a long Hallway.",
            'random_battle': False,
            'options': [0, 2],
            'unlock_value': None
        }
    ],
    [
        {
            'description': "You made it to the second floor!\nYou can head back South to the first floor.\nOr you can head East to along the Northern Hallway",
            'random_battle': False,
            'options': [2, 3],
            'unlock_value': None
        },
        {
            'description': "West heads to the stairs downward.\nEast continues down a long Hallway.",
            'random_battle': False,
            'options': [0, 4],
            'unlock_value': None
        },
        {
            'description': "West heads to the stairs downward.\nSouth leads to a turn in the path.",
            'random_battle': False,
            'options': [0, 2],
            'unlock_value': None
        },
        {
            'description': "HOLDER",
            'options': []
        },
        {
            'description': "HOLDER",
            'options': [],
            'unlock_value': 'TO_EAST_STAIRS_ENTRANCE'
        },
        {
            'description': "North heads to the stairs downward.\nSouth leads to a glowing room...",
            'random_battle': False,
            'options': [1, 2],
            'unlock_value': None
        }
    ],
    [
        {
            'description': "HOLDER",
            'options': [],
            'unlock_value': 'TO_WEST_STAIRS_ENTRANCE'
        },
        {
            'description': 'You\'ve got your super potions filled up.\nYou can head East towards a long trek downstairs.\nOr head South towards the Southern Hallway.',
            'random_battle': False,
            'options': [0],
            'unlock_value': None,
            'dispenser': {
                'item_type': 'super_potions'
            }
        },
        {
            'description': "West heads to a bend in the path with a shadowy outcrop.\nNorth leads back to the Northern Hallway..",
            'random_battle': False,
            'options': [0, 1],
            'unlock_value': None
        },
        {
            'description': "HOLDER",
            'options': [],
            'unlock_value': 'TO_DRAGON'
        },
        {
            'description': "South leads to the Southern Hallway.\nEast leads to the Eastern Hallway.",
            'random_battle': False,
            'options': [2, 3],
            'unlock_value': None
        },
        {
            'description': "You have the Tempered Chestplate.\nYou can head West towards a turn in the path.\nOr head North along the Eastern Hallway.",
            'random_battle': False,
            'options': [1],
            'block_value': 'LEVEL_TWO_CHEST_ARMOR',
            'unlock_value': {
                'value': 'LEVEL_TWO_CHEST_ARMOR',
                'display': False
            },
            'alt_pathway': {
                'alt_description': '',
                'description': 'You already picked up the Tempered Chestplate. resting here.\nYou can head West towards a turn in the path.\nOr head North along the Eastern Hallway.',
                'random_battle': False,
                'options': [1],
                'first_unlock': 'LEVEL_TWO_CHEST_ARMOR',
                'block_value': 'LEVEL_TWO_CHEST_ARMOR',
                'unlock_value': None
            }
        }
    ],
    [
        {
            'description': "HOLDER",
            'options': []
        },
        {
            'description': "North heads to a bend in the path with a shadowy outcrop.\nEast moves along the Southern Hallway.",
            'random_battle': False,
            'options': [1, 3],
            'unlock_value': None
        },
        {
            'description': "West heads to a turn in the Southern Hallway.\nEast moves towards a reddish light...",
            'random_battle': False,
            'options': [0, 3],
            'unlock_value': None
        },
        {
            'description': "West moves along the Southern Hallway.\nEast moves back towards a turn in the path.",
            'random_battle': False,
            'warning_trigger': True,
            'options': [0, 3],
            'unlock_value': None
        },
        {
            'description': "West moves towards a reddish light...\nNorth heads towards a turn in the path.",
            'random_battle': False,
            'options': [0, 1],
            'unlock_value': None
        }
    ]
]
