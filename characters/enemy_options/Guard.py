from characters.Enemy import Enemy


class Guard(Enemy):
    name = "Guard"
    name_tense = "A Guard"
    enemy_health = 80
    max_enemy_health = 80
    enemy_attack_damage = 20
    attack_variable = 5
    special_attack = "Lunges"
    base_experience_yield = 40
    exp_range = 3