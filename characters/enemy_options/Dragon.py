from characters.Enemy import Enemy


class Dragon(Enemy):
    name = "Dragon"
    name_tense = "A Dragon"
    max_enemy_health = 10
    enemy_attack_damage = 100
    special_attack = "Scorches"
    base_experience_yield = 50
    exp_range = 10