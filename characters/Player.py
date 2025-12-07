# THE HERO CLASS

from items.armor.ArmorItem import ArmorItem


class Player:
    total_experience = 0
    base_level = 10
    to_next_level = 10
    level = 1

    health_potion_heal_amount = 30
    health_potion_drop_chance = 50  # 50 Percent chance to drop a health potion
    current_armor = 16
    # levelUpChance = 50 - Don't know about this...
    inventory = {
        "consumables": {
            # "potions": [],
            # "super_potions": []
        },
        "key_items": []
    }
    gear = {
        "armor": {
            "head": ArmorItem('Cheap Helmet', 'HEAD_CHEAP', 5, 'head', 1),
            "chest":  ArmorItem('Leather Chestplate', 'LEATHER_CHESTPLATE', 10, 'chest', 1),
            "legs": ArmorItem('Weathered Trousers', 'LEGS_WEATHERED', 1, 'legs', 1)
        },
        "weapons": {
            "main": None
        }
    }