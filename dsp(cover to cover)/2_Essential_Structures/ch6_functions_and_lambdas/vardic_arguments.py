import random


# I want to allow the rolling of multiple dice, where each die may have a different number of sides:
def roll_dice(*dice):
    return tuple(random.randint(1, d) for d in dice)


print(roll_dice(20, 6, 8, 4, 7, 11))  # (7,2,3,1,1,9)


def roll_dice_recursion(*dice) -> tuple[int]:
    if not dice:
        return ()

    return (random.randint(1, dice[0]),) + roll_dice_recursion(*dice[1:])


print(roll_dice_recursion(20, 6, 8, 4, 7, 11))  # (13, 4, 5, 4, 1, 10)
## in func definition * packs the arguments in the tuple but inside func * unpacks the tuple into argument list
