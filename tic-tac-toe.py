
# In this script you can write your code.
# Start by writing all the functions.

# Function for ... (displaying the board?)
def print_board():
    print("1   2   3")
    print("4   5   6")
    print("7   8   9")

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
    target_set = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [1, 4, 7],
                  [2, 5, 8],
                  [3, 6, 9],
                  [1, 5, 9],
                  [3, 5, 7]
                  ]
    X_player = board['X']
    O_player = board['O']

    for seq in target_set:
        if set(seq).issubset(set(X_player)):
            return True

        elif set(seq).issubset(set(O_player)):
            return True

    return False

# Function for... (choosing a player?)
# Update the board at selected index.
def update_board(board, index, val):
    if val not in board:
        board[val] = [index]
    else:
        board[val].append(index)

# Validate the selected position by users.
def is_unique_and_valid_input(index, available_positions):
    if index in available_positions:
        return True
    return False



# Tic-tac-toe game, main functions of game, input from user, validation and checking for winner.
def tic_Tac_toe_game(board, available_positions):
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
                    update_board(board, pIndex, fillers[i % 2])
                    available_positions.remove(pIndex)
                    break
                else:
                    print(
                        "Invalid Index, Please select the one between 1-9 and not filled.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        print_updated_board(board)
        if (len(available_positions) <= 6 and check_end_win(board)):
            print(f"Player {i%2 + 1} is winner !")
            break
        elif len(available_positions) <= 1:
            print("Draw!! Game is over")
            break


if __name__ == "__main__":
    # Board will be dictionary of list, It will have 2 entry only,
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    print_board()
    while (1):
        board = {}
        available_positions = [i for i in range(1, 10)]
        tic_Tac_toe_game(board, available_positions)

        next_move = str(
            input("\n\n\nIn you want to continue, press C or c, else press anything\n"))
        if next_move in ['c', 'C']:
            continue
        else:
            break
