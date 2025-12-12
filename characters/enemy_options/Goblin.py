from characters.Enemy import Enemy


class Goblin(Enemy):
    name = "Goblin"
    name_tense = "A Goblin"
    max_enemy_health = 250
    enemy_attack_damage = 50
    special_attack = "Slices"
    base_experience_yield = 10
    exp_range = 5