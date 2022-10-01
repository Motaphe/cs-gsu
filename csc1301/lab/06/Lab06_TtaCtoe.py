# Prolog
# Author:  Suzal Regmi
# Email:  sregmi2@student.gsu.edu
# Section: 036
# Reference: no one
# Timestamp: 8:44 PM, 30th September 2022
# Approximate Time Taken: 1 hour

# Assignment Info: We coded a program that takes a 3x3 Tic-Tac-Toe board as input and 
# displays which player won, or if both players won.


tik_board = [input(f"Row {_} (can only be 'X', 'O', or 'E'): ") for _ in range(0, 3)]

to_print = []

for i in range(0, 3):
    if len(set(tik_board[i])) == 1:
        if to_print.count(f"{tik_board[i][0]} IS GOOD IN HORIZONTAL") == 0:
            to_print.append(f"{tik_board[i][0]} IS GOOD IN HORIZONTAL")


if tik_board[0][0] == tik_board[1][1]:
    if tik_board[1][1] == tik_board[2][2]:
        if to_print.count(f"{tik_board[0][0]} IS GOOD IN DIAGONAL") == 0:
            to_print.append(f"{tik_board[0][0]} IS GOOD IN DIAGONAL")

if tik_board[0][2] == tik_board[1][1]:
    if tik_board[1][1] == tik_board[2][0]:
        if to_print.count(f"{tik_board[0][2]} IS GOOD IN DIAGONAL") == 0:
            to_print.append(f"{tik_board[0][2]} IS GOOD IN DIAGONAL")

for i in range(0,3):
    if tik_board[0][i] == tik_board[1][i]:
        if tik_board[1][i] == tik_board[2][i]:
            if to_print.count(f"{tik_board[0][i]} IS GOOD IN VERTICAL") == 0:
                to_print.append(f"{tik_board[0][i]} IS GOOD IN VERTICAL")


try:
    to_print.remove("E IS GOOD IN HORIZONTAL")
except (ValueError):
    pass
try:
    to_print.remove("E IS GOOD IN DIAGONAL")
except (ValueError):
    pass
try:
    to_print.remove("E IS GOOD IN VERTICAL")
except (ValueError):
    pass


if len(to_print) != 0:
    for i in range(len(to_print)):
        print (to_print[i])
else:
    print ("THIS IS TIE")