from items.Consumable import Consumable

class SuperPotion(Consumable):
	item_name = 'super potion'
	description = 'An enhanced potion to replenish 100 points of health.'
	heal_value = 100
	type = 'HEALTH'