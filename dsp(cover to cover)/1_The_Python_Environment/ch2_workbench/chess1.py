#!/usr/bin/env python3

## when i named this file "chess.py" it was giving attribute error most likely due to a circular import) signals a circular import issue where modules are importing each other in a way that creates a loop.

##  This was a naming conflict shadowing chess module with a file named "chess.py", hence "chess1.py" worked..

import chess
board = chess.Board()
print(board.legal_moves)

board.push_san("e4")
print(board)
board.push_san("e5")
print(board.is_checkmate()) ## false
print(board)
board.push_san("Nf3")
print(board)