from items.Consumable import Consumable

class Potion(Consumable):
	item_name = 'potion'
	description = 'A potion to replenish 20 points of health.'
	heal_value = 20
	type = 'HEALTH'