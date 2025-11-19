from characters.Enemy import Enemy


class Goblin(Enemy):
    name = "Goblin"
    name_tense = "A Goblin"
    max_enemy_health = 40
    enemy_attack_damage = 40
    special_attack = "Slices"
    base_experience_yield = 20
    exp_range = 5