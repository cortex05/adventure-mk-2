from characters.Enemy import Enemy


class GiantWharg(Enemy):
    name = "Giant Wharg"
    name_tense = "A Giant Wharg"
    enemy_health = 300
    max_enemy_health = 300
    enemy_attack_damage = 60
    attack_variable = 20
    special_attack = "Bites"
    base_experience_yield = 15
    exp_range = 1