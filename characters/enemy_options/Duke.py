from characters.Enemy import Enemy


class Duke(Enemy):
    name = "Lord Duke"
    name_tense = "A Duke"
    enemy_health = 60
    max_enemy_health = 60
    enemy_attack_damage = 20
    special_attack = "Tortures"
    base_experience_yield = 30
    exp_range = 5
