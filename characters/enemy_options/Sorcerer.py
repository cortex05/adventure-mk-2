from characters.Enemy import Enemy


class Sorcerer(Enemy):
    name = "Sorcerer"
    name_tense = "A Sorcerer"
    max_enemy_health = 100
    enemy_attack_damage = 20
    special_attack = "Curses"
    base_experience_yield = 40
    exp_range = 3
