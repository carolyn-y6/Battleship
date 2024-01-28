# * ***********************************************************************
# Carolyn Yang
# Cryptography

# This program is my own work - Digital Signature CY
# To help people have some fun with Battle Ship


# initializing board
board = []
for x in range(7):
    board.append(["-"] * 7)


# Print the board
def print_board(board):
    for row in board:
        print(" ".join(row))


# Check if the user hit anything and mark where the user hit
def change_board(board, x, y):
    if (x == 1 and y == 1) or (x == 2 and y == 1) or (x == 3 and y == 1):
        board[y - 1].pop(x - 1)
        board[y - 1].insert(x - 1, "X")
    elif (x == 7 and y == 2) or (x == 7 and y == 3):
        board[y - 1].pop(x - 1)
        board[y - 1].insert(x - 1, "X")
    elif (x == 2 and y == 5) or (x == 3 and y == 5):
        board[y - 1].pop(x - 1)
        board[y - 1].insert(x - 1, "X")
    elif (x == 5 and y == 5):
        board[y - 1].pop(x - 1)
        board[y - 1].insert(x - 1, "X")
    elif (x == 3 and y == 6) or (x == 3 and y == 7):
        board[y - 1].pop(x - 1)
        board[y - 1].insert(x - 1, "X")
    else:
        board[y - 1].pop(x - 1)
        board[y - 1].insert(x - 1, "O")

    # Check if the user hit anything


def check_for_win(board):
    if (board[0].count("X") == 3) and (board[1].count("X") == 1) and (board[2].count("X") == 1) and (
            board[4].count("X") == 3) and (board[5].count("X") == 1) and (board[6].count("X") == 1):
        print("You've sunk all ships! Congrats!")
        return 1


# starting the game and printing the initial empty board
v = 1
while v == 1:
    print(" ")
    print("Let's play Battleship!")
    print_board(board)
    i = 1
    # To loop around for the actual game
    while i == 1:
        print()
        x = int(input("Put in a number for the x-coordinate (1-7): "))
        while ((x < 0 or x > 7) and x != 0):
            x = int(input("     -> Error! Put in a number for the x-coordinate (1-7): "))
        y = int(input("Put in a number for the y-coordinate (1-7): "))
        while ((y < 0 or y > 7) and y != 0):
            y = int(input("     -> Error! Put in a number for the y-coordinate (1-7): "))
        change_board(board, x, y)
        print_board(board)
        if check_for_win(board) == 1:
            i = 3

    # Check if the user wants to play again and loop accordingly
    again = input("Do you want to play again? (y/n): ")
    while again.upper() != "NO" and again.upper() != "N" and again.upper() != "Y" and again.upper() != "YES":
        again = input("     -> Error! Do you want to play again? (y/n): ")
    if (again.upper() == "NO") or (again.upper() == "N"):
        print("Awww see you again next time...")
        v = 2
        break
    elif (again.upper() == "YES") or (again.upper() == "Y"):
        print("YAy! Good to see you again!")
        v = 1






