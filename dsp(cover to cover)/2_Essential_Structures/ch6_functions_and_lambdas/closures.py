import random


# this is closure/function factory pattern => closure returns func object
def make_dice_cup(sides=6, dice=1):
    def roll():
        return tuple(random.randint(1, sides) for _ in range(dice))

    return roll


roll_for_damage = make_dice_cup(8, 5)
damage = roll_for_damage()
print(damage)  # (8, 5, 4, 6, 2)


## recursion with closures


def make_dice_cup1(sides=6, dice=1):
    def roll1():
        nonlocal dice
        if dice < 1:
            return ()
        die = random.randint(1, sides)
        dice -= 1
        return (die,) + roll1()

    return roll1


roll_for_damage1 = make_dice_cup1(sides=8, dice=5)
damage1 = roll_for_damage1()
print(damage1)  # (2, 8, 6, 4, 1)
