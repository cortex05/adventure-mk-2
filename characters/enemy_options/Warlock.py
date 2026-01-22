from characters.Enemy import Enemy


class Warlock(Enemy):
    name = "Warlock"
    name_tense = "A Warlock"
    enemy_health = 600
    max_enemy_health = 600
    enemy_attack_damage = 100
    attack_variable = 20
    special_attack = "Hexes"
    base_experience_yield = 40
    exp_range = 5
    dodge_chance = 10
    keen = 5