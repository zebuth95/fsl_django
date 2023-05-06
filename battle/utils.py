from monster.models import Monster


# Create your battle Algorithm here


def fight(monster_a: Monster, monster_b: Monster) -> Monster:
    if monster_a.speed > monster_b.speed:
        first_monster = monster_a
        second_monster = monster_b
    elif monster_a.speed < monster_b.speed:
        first_monster = monster_a
        second_monster = monster_b
    else:
        if monster_a.attack > monster_b.attack:
            first_monster = monster_a
            second_monster = monster_b
        else:
            first_monster = monster_a
            second_monster = monster_b

    while True:
        damage = first_monster.attack - second_monster.defense

        if damage <= 0:
            damage = 1

        second_monster.hp -= damage

        damage = second_monster.attack - first_monster.defense

        if damage <= 0:
            damage = 1

        first_monster.hp -= damage

        if first_monster.hp <= 0:
            return second_monster
        elif second_monster.hp <= 0:
            return first_monster
