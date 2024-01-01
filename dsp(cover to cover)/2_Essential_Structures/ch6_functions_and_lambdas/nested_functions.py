## writing dice_roll:
from random import randint


def roll_dice(side=6, dice=1) -> tuple[int]:
    def roll():
        return randint(1, side)

    if dice < 1:
        return ()
    return (roll(),) + roll_dice(side, dice - 1)


print(roll_dice())  # (4,)
print(roll_dice(6, 5))  # (6, 4, 5, 6, 2)
