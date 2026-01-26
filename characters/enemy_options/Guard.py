from characters.Enemy import Enemy

# Non boss Duke
class Guard(Enemy):
    name = "Guard"
    name_tense = "A Guard"
    enemy_health = 400
    max_enemy_health = 400
    enemy_attack_damage = 85
    attack_variable = 15
    special_attack = "Lunges"
    base_experience_yield = 40
    exp_range = 3
    dodge_chance = 8
    keen = 5