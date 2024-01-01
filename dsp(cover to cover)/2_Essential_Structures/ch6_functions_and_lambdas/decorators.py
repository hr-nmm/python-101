import random

character = "Sir Bob"
health = 15
xp = 0


def eat_food(food):
    global health

    if health <= 0:
        print(f"{character} is too weak.")
        return

    print(f"{character} ate {food}.")
    health += 1
    print(f"    Health: {health} | XP: {xp}")


def fight_monster(monster, strength):
    global health, xp
    if health <= 0:
        print(f"{character} is too weak.")
        return

    if random.randint(1, 20) >= strength:
        print(f"{character} defeated {monster}.")
        xp += 10
    else:
        print(f"{character} flees from {monster}.")
        health -= 10
        xp += 5
    print(f"    Health: {health} | XP: {xp}")


## driver code

eat_food("bread")
fight_monster("Imp", 15)
fight_monster("Direwolf", 15)
fight_monster("Minotaur", 19)

"""
o/p => 
Sir Bob ate bread.
    Health: 16 | XP: 0
Sir Bob flees from Imp.
    Health: 6 | XP: 5
Sir Bob defeated Direwolf.
    Health: 6 | XP: 15
Sir Bob flees from Minotaur.
    Health: -4 | XP: 20
"""

## decorator implementation

import functools
import random

character = "Sir Bob"
health = 15
xp = 0


def character_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if health <= 0:
            print(f"{character} is too weak.")
            return

        result = func(*args, **kwargs)
        print(f"    Health: {health} | XP: {xp}")
        return result

    return wrapper


@character_action
def eat_food(food):
    global health
    print(f"{character} ate {food}.")
    health += 1


@character_action
def fight_monster(monster, strength):
    global health, xp
    if random.randint(1, 20) >= strength:
        print(f"{character} defeated {monster}.")
        xp += 10
    else:
        print(f"{character} flees from {monster}.")
        health -= 10
        xp += 5


## driver for improved version
eat_food("bread")
fight_monster("Imp", 15)
fight_monster("Direwolf", 15)
fight_monster("Minotaur", 19)

"""
o/p => 
Sir Bob ate bread.
    Health: 16 | XP: 0
Sir Bob flees from Imp.
    Health: 6 | XP: 5
Sir Bob flees from Direwolf.
    Health: -4 | XP: 10
Sir Bob is too weak.
"""
