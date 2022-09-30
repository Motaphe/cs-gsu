'''
make so that the program skips rows, colums and diagonals of "E"
discard invalid input
shorten the code (list comprehension?)
'''



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


if len(to_print) != 0:
    for i in range(len(to_print)):
        print (to_print[i])
else:
    print ("THIS IS TIE")