# lambdas are nameless one line functions
add = lambda x, y: x + y
answer = add(2, 333)
print(answer)  # 335
print((lambda x, y: x * y)(2, 3))  # 6

## lambda use case
import random

health, xp = 10, 10


def attempt(action, min_roll, outcome):
    global health, xp
    roll = random.randint(1, 20)
    if roll >= min_roll:
        print(f"{action} SUCCEEDED")
        result = True
    else:
        print(f"{action} FAILED")
        result = False
    scores = outcome(result)
    health = health + scores[0]
    print(f"Health is now {health}")
    xp += scores[1]
    print(f"Experience is now {xp}")

    return result


def eat_bread(success):
    return (1, 0) if success else (-1, 0)


def fight_ice_weasel(success):
    return (0, 10) if success else (-10, 10)


## driver code
attempt("eating bread".capitalize(), 5, eat_bread)
attempt("fighting ice weasel".capitalize(), 15, fight_ice_weasel)

## lambda use case: when a func is to be passed as an arg to a function
attempt("eating bread".capitalize(), 5, lambda success: (1, 0) if success else (-1, 0))
attempt(
    "fighting ice weasel".capitalize(),
    15,
    lambda success: (0, 10) if success else (-10, 10),
)


# LAMBDAS AS Sorting keys
people = [
    ("Jason", "McDonald"),
    ("Denis", "Pobedrya"),
    ("Daniel", "Foerster"),
    ("Jaime", "López"),
    ("James", "Beecham"),
]

by_last_name = sorted(people, key=lambda x: x[1])
print(by_last_name)
# [('James', 'Beecham'), ('Daniel', 'Foerster'), ('Jaime', 'López'), ('Jason', 'McDonald'), ('Denis', 'Pobedrya')]
##  I want the tuples sorted by last name, which is the second item of each tuple, I have the lambda return that item, which is x[1].
