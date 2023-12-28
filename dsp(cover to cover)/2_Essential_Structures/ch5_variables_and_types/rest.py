board = [["-"] * 3] * 3  # Create a board(tic-tac-toe)[2-d board]
print(board)
board[1][0] = "X"

for row in board:
    print(f"{row[0]} {row[1]} {row[2]}")  ## gets "X" in all first elements
## Reason since it was created with 1 list which got used three times, I now have three aliases for one mutable value!

board_correct = [["-"] * 3 for _ in range(3)]
print(board_correct)
board_correct[1][0] = "X"

for row in board_correct:
    print(f"{row[0]} {row[1]} {row[2]}")  ## got "X" in Column 0 : Row 1
