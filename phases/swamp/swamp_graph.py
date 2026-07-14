"""Swamp phase as a room graph (prototype of the Part 1 navigation proposal).

Transliterated from phases/swamp/swamp_coordinates.py: every reachable grid cell
becomes a Room, "HOLDER" filler cells are dropped, and [row][col] links become
named exits. Enemy ids and battle_chance values are preserved unchanged."""

from navigation.models import Encounter, Gate, Phase, Room

WHARG = [1]
GOBLIN = [2]
GIANT_WHARG = [11]


def build_swamp() -> Phase:
	# Gate variants (were the grid's alt_pathway blocks).
	shed_open = Room(
		id='shed_open',
		description=['The shed only has the goblin you slayed. I guess you can only go back now.\n'],
		exits={'south': 'marsh'},
		on_first_enter=[''],
		first_token='KEY_SHED',
	)
	keyslot_open = Room(
		id='keyslot_open',
		description=['You now have a way to cross the bridge! Where will you go?\n'],
		exits={'west': 'clearing', 'north': 'moat_entrance', 'south': 'trees_junction', 'east': 'structures'},
		on_first_enter=[
			'As you insert and twist your key into the slot, the earth rumbles.\n',
			'You step back as the bridge comes crashing down!\n',
			'You now have a way to cross the bridge!\n',
			'What will you do?\n',
		],
		first_token='CASTLE_UNLOCK',
	)
	chest_open = Room(
		id='chest_open',
		description=['The shed only has the Giant Wharg you slayed. I guess you can only go back now.\n'],
		exits={'north': 'east_structures'},
		on_first_enter=[''],
		first_token='NEW_WEAPON',
	)

	rooms = {
		'entrance': Room(
			id='entrance',
			description=[
				'You stand before a large swamp.\n',
				'Once you jump in, the only way out is through.\n',
				'What do you do?\n',
			],
			exits={'north': 'trees_junction'},
		),
		'trees_junction': Room(
			id='trees_junction',
			description=[
				'To the north is a castle.\n',
				'To the east is a small batch of trees.\n',
				'What will you do?\n',
			],
			exits={'north': 'keyslot', 'east': 'trees'},
			encounter=Encounter(WHARG, 2),
		),
		'trees': Room(
			id='trees',
			description=['The trees are a dead end. You can only go west to the swamp entrance.\n'],
			exits={'west': 'trees_junction'},
		),
		'keyslot': Room(
			id='keyslot',
			description=[
				'To the north you see a castle, but the bridge to cross the moat is raised.\n',
				'You see a slot for a key, but you have none.\n',
				'To the North by Northwest you see a shed, but west is your only way there.\n',
				'To the south you see the Wharg-ridden entrance. \n',
				'Off to the east, you see various structures.\n',
				'What will you do?\n',
			],
			exits={'west': 'clearing', 'south': 'trees_junction', 'east': 'structures'},
			gate=Gate('CASTLE_KEY', keyslot_open),
		),
		'moat_entrance': Room(
			id='moat_entrance',
			description=['\n\nThis is the entrance to the moat.\n'],
			transition='VICTORY',
		),
		'clearing': Room(
			id='clearing',
			description=[
				"You're in a clearing.\n",
				'To the northwest you see a shed, but your only way to it is west through a suspicious marsh.\n',
				'To the south is a field of long grass.\n',
				'To the east is the moat entrance.',
			],
			exits={'west': 'marsh', 'south': 'long_grass', 'east': 'keyslot'},
		),
		'marsh': Room(
			id='marsh',
			description=['You see a shed to the north and the clearing to the east that you just came from.\n'],
			exits={'north': 'shed', 'east': 'clearing'},
			encounter=Encounter(WHARG, 2),
		),
		'shed': Room(
			id='shed',
			description=['Go back and find the entrance!\n'],
			exits={'south': 'marsh'},
			encounter=Encounter(GOBLIN, 1),
			unlock={'value': 'CASTLE_KEY', 'display': False},
			gate=Gate('KEY_SHED', shed_open),
		),
		'long_grass': Room(
			id='long_grass',
			description=[
				'To the west is a mysterious cave.\n',
				'To the north is a clearing\n',
			],
			exits={'west': 'cave', 'north': 'clearing'},
			encounter=Encounter(WHARG, 2),
		),
		'cave': Room(
			id='cave',
			description=['The cave is a dead end. You can only go East towards the long grass...\n'],
			exits={'east': 'long_grass'},
			encounter=Encounter(WHARG, 2),
		),
		'structures': Room(
			id='structures',
			description=[
				'To the west is the moat entrance.\n',
				'To the Northeast and Southeast are structures.\n',
				'Where will you go?\n',
			],
			exits={'west': 'keyslot', 'east': 'east_structures'},
			encounter=Encounter(WHARG, 2),
		),
		'east_structures': Room(
			id='east_structures',
			description=[
				'Back west is the suspicious field and beyond is the moat entrance.\n',
				'To the North you see a carriage.\n',
				'To the south, there appears to be a large chest...\n',
			],
			exits={'west': 'structures', 'north': 'carriage', 'south': 'chest'},
		),
		'carriage': Room(
			id='carriage',
			description=["You've got your potions filled up. You can only head south...\n"],
			exits={'south': 'east_structures'},
			dispenser='potions',
		),
		'chest': Room(
			id='chest',
			description=['The chest is empty. Only makes sense to head back north\n'],
			exits={'north': 'east_structures'},
			encounter=Encounter(GIANT_WHARG, 1),
			unlock={'value': 'NEW_WEAPON', 'display': False},
			gate=Gate('NEW_WEAPON', chest_open),
		),
	}
	return Phase(entry='entrance', rooms=rooms)


swamp_phase = build_swamp()
