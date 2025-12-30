from characters.Enemy import Enemy

# Non boss Duke
class Guard(Enemy):
    name = "Guard"
    name_tense = "A Guard"
    enemy_health = 400
    max_enemy_health = 400
    enemy_attack_damage = 75
    attack_variable = 10
    special_attack = "Lunges"
    base_experience_yield = 40
    exp_range = 3