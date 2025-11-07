from characters.Enemy import Enemy


class Sorcerer(Enemy):
    name = "Sorcerer"
    name_tense = "A Sorcerer"
    max_enemy_health = 20
    enemy_attack_damage = 10
    special_attack = "Curses"
    base_experience_yield = 20
    exp_range = 3
