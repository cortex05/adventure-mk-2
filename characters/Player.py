# THE HERO CLASS

class Player:
    total_experience = 0
    base_level = 10
    to_next_level = 10
    level = 1

    num_health_potions = 4
    health_potion_heal_amount = 30
    health_potion_drop_chance = 50  # 50 Percent chance to drop a health potion
    current_armor = 16
    # levelUpChance = 50 - Don't know about this...
    inventory = {
        "consumables": {
            "potions": []
        },
        "key_items": []
    }
    gear = {
        "armor": {
            "head": {
                "name": "Cheap Helmet",
                "id": "HEAD_CHEAP",
                "defense_bonus": 5,
                "part": "head"
            },
            "chest": {
                "name": "Leather Chestplate",
                "id": "LEATHER_CHESTPLATE",
                "defense_bonus": 10,
                "part": "chest"
            },
            "legs": {
                "name": "Weathered Trousers",
                "id": "HEAD_CHEAP",
                "defense_bonus": 1,
                "part": "legs"
            }
        },
        "weapons": {
            "main": None
        }
    }