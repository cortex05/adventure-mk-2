from items.Consumable import Consumable

class Potion(Consumable):
	item_name = 'potion'
	description = 'A potion to replenish 50 points of health.'
	heal_value = 50
	type = 'HEALTH'