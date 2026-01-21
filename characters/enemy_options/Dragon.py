from characters.Enemy import Enemy


class Dragon(Enemy):
    name = "Dragon"
    name_tense = "A Dragon"
    enemy_health = 1000
    max_enemy_health = 10000
    enemy_attack_damage = 150
    attack_variable = 30
    special_attack = "Scorches"
    base_experience_yield = 50
    exp_range = 10