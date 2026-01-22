from characters.Enemy import Enemy


class Goblin(Enemy):
    name = "Goblin"
    name_tense = "A Goblin"
    enemy_health = 250
    max_enemy_health = 250
    enemy_attack_damage = 75
    attack_variable = 10
    special_attack = "Slices"
    base_experience_yield = 10
    exp_range = 5
    dodge_chance = 10
    keen = 5