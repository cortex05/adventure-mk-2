from characters.Enemy import Enemy


class Dragon(Enemy):
    name = "Dragon"
    name_tense = "A Dragon"
    max_enemy_health = 40
    enemy_attack_damage = 100
    special_attack = "Scorches"
    experience_yield = 3000