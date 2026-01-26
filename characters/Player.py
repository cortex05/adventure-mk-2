from items.armor.ArmorItem import ArmorItem

class Player:
    total_experience = 0
    base_level = 10
    to_next_level = 10
    level = 1

    health_potion_heal_amount = 30
    health_potion_drop_chance = 50
    current_armor = 16
    inventory = {
        "consumables": {

        },
        "key_items": []
    }
    gear = {
        "armor": {
            "head": ArmorItem('Cheap Helmet', 'HEAD_CHEAP', 3, 'head', 1),
            "chest":  ArmorItem('Leather Chestplate', 'LEATHER_CHESTPLATE', 10, 'chest', 1),
            "legs": ArmorItem('Weathered Trousers', 'LEGS_WEATHERED', 7, 'legs', 1)
        },
        "weapons": {
            "main": None
        }
    }