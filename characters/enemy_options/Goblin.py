from characters.Enemy import Enemy


class Goblin(Enemy):
    name = "Goblin"
    name_tense = "A Goblin"
    max_enemy_health = 40
    enemy_attack_damage = 10
    special_attack = "Slices"
    base_experience_yield = 30
    exp_range = 5