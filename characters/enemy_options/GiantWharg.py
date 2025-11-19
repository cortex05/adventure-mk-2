from characters.Enemy import Enemy


class GiantWharg(Enemy):
    name = "Giant Wharg"
    name_tense = "A Giant Wharg"
    max_enemy_health = 200
    enemy_attack_damage = 20
    special_attack = "Bites"
    base_experience_yield = 15
    exp_range = 1