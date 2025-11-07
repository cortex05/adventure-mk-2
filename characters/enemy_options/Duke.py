from characters.Enemy import Enemy


class Duke(Enemy):
    name = "Lord Duke"
    name_tense = "A Duke"
    max_enemy_health = 10
    enemy_attack_damage = 10
    special_attack = "Tortures"
    base_experience_yield = 30
    exp_range = 5
