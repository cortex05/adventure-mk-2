from characters.Enemy import Enemy


class Duke(Enemy):
    name = "Lord Duke"
    name_tense = "A Duke"
    enemy_health = 400
    max_enemy_health = 400
    enemy_attack_damage = 70
    attack_variable = 15
    special_attack = "Tortures"
    base_experience_yield = 30
    exp_range = 5
    dodge_chance = 8
    keen = 15
