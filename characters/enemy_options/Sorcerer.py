from characters.Enemy import Enemy


class Sorcerer(Enemy):
    name = "Sorcerer"
    name_tense = "A Sorcerer"
    enemy_health = 300
    max_enemy_health = 300
    enemy_attack_damage = 80
    attack_variable = 25
    special_attack = "Curses"
    base_experience_yield = 40
    exp_range = 5
    dodge_chance = 3
    keen = 20
