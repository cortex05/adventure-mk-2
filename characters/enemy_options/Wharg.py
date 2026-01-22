from characters.Enemy import Enemy


class Wharg(Enemy):
    name = "Wharg"
    name_tense = "A Wharg"
    enemy_health = 100
    max_enemy_health = 100
    enemy_attack_damage = 60
    attack_variable = 5
    special_attack = "Bites"
    base_experience_yield = 5
    exp_range = 2
    dodge_chance = 7
    keen = 5
