import random


#  "roll_dice" function that rolls a single die with a specified number of sides:
def roll_dice(sides: int) -> int:
    return random.randint(1, sides)  # pure functional


print("Start Rolling")
player1, player2 = roll_dice(20), roll_dice(20)
print(
    f"player1 goes first (rolled {player1}) and beats {player2}"
) if player1 >= player2 else print(
    f"player2 goes first (rolled {player2} and beats {player1})"
)


#  "roll_dice" function that rolls multiple dice at once and every usage of that function will be affected:
def roll_dice_multiple(sides: int, dice: int) -> tuple:
    return tuple(random.randint(1, sides) for _ in range(dice))


print("Roll for initiative...")
player1, player2 = roll_dice_multiple(20, 2)  ## tuple unpacking
if player1 >= player2:
    print(f"Player 1 goes first (rolled {player1}) and beats {player2}")
else:
    print(f"Player 2 goes first (rolled {player2}) and beats {player2}")


## generators
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


x = simpleGeneratorFun()
print(
    x, type(x)
)  # <generator object simpleGeneratorFun at 0x7f6be2a2e960> <class 'generator'>
# Driver code to check above generator function
for value in x:
    print(value)  # 1 2 3


## roll_dice_multiple using recursion
def roll_dice_multiple_recursion(
    sides: int, dice: int = 1
) -> tuple[
    int
]:  ## we specified dice = 1 in the function definition itself => default parameter
    if dice < 1:
        return ()
    roll = random.randint(1, sides)
    return (roll,) + roll_dice_multiple_recursion(sides, dice - 1)  # WORKS FINE


dice_cup = roll_dice_multiple_recursion(6, 5)
print(dice_cup)
print(
    roll_dice_multiple_recursion(6)
)  # rolling A 6-side dice once, since no of dices are not passed as arg default is 1.
