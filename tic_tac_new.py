# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
def print_board():
    print("1   2   3")
    print("4   5   6")
    print("7   8   9")


def print_arr_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print()
# Print the updated board


def print_updated_board(board):
    for i in range(1, 10):
        if 'X' in board.keys() and i in board['X']:
            print('x  ', end=' ')
        elif 'O' in board.keys() and i in board['O']:
            print('o  ', end=' ')
        else:
            print(i, " ", end=' ')
        if (i % 3 == 0):
            print()

# Check for winner


def check_end_win(board):
    # print(board)
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]  # Return the winner symbol
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]  # Return the winner symbol
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][2]

    return ' '

# Function for... (choosing a player?)
# Update the board at selected index.


def update_board(board, index, val):
    row = (index-1)//3
    col = (index-1) % 3
    board[row][col] = val


def update_board_old(board, index, val):
    if val not in board:
        board[val] = [index]
    else:
        board[val].append(index)

# Validate the selected position by users.


def is_unique_and_valid_input(index, available_positions):
    if index in available_positions:
        return True
    return False


# ... write as many functions as you need


# Tic-tac-toe game, main functions of game, input from user, validation and checking for winner.
def tic_tac_toe_game(board_arr, available_positions):
    fillers = ['X', 'O']

    for i in range(9):
        while (1):
            # user input for position
            try:
                pIndex = int(
                    input(f"Player {i%2 + 1}, select your position\n"))
                # validation

                if (is_unique_and_valid_input(pIndex, available_positions)):
                    # Update the board.
                    update_board(board_arr, pIndex, fillers[i % 2])
                    available_positions.remove(pIndex)
                    break
                else:
                    print(
                        "Invalid Index, Please select the one between 1-9 and not filled.")
            except ValueError:
                print("Invalid input. Please enter a valid number between 1-9.")

        # print_updated_board(board)
        print_arr_board(board_arr)
        if (len(available_positions) <= 6 and ' ' != check_end_win(board_arr)):
            print(f"Player {i%2 + 1} is winner !")
            break
        elif len(available_positions) <= 0:
            print("Draw!! Game is over")
            break


if __name__ == "__main__":
    # Board will be dictionary of list, It will have 2 entry only,
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    print_board()

    while (1):
        # board = {}
        board_2d = [[" " for _ in range(3)] for _ in range(3)]
        print_arr_board(board_2d)
        available_positions = [i for i in range(1, 10)]
        tic_tac_toe_game(board_2d, available_positions)

        next_move = str(
            input("\n\n\nIn you want to continue, press C or c, else press anything\n"))
        if next_move in ['c', 'C']:
            continue
        else:
            break
