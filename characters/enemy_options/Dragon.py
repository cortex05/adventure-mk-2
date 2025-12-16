from characters.Enemy import Enemy


class Dragon(Enemy):
    name = "Dragon"
    name_tense = "A Dragon"
    enemy_health = 10
    max_enemy_health = 10
    enemy_attack_damage = 100
    attack_variable = 5
    special_attack = "Scorches"
    base_experience_yield = 50
    exp_range = 10