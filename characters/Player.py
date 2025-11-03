# THE HERO CLASS

class Player:
    total_experience = 0
    base_level = 1000
    to_next_level = 1000

    num_health_potions = 4
    health_potion_heal_amount = 30
    health_potion_drop_chance = 50  # 50 Percent chance to drop a health potion
    # levelUpChance = 50 - Don't know about this...
    inventory = {
        "consumables": {
            "potions": []
        },
        "key_items": {}
    }