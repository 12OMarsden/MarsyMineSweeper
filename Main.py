import random

print("Welcome to my version of Minesweeper     :)" + '\n')

no_of_bombs = 50
bomb = "X"
board_y = 25
board_x = 20


def get_random_coordinate(x, y):
    return [random.randint(0, x - 1), random.randint(0, y - 1)]


def make_array(x_size, y_size):
    return [[0 for y in range(y_size)] for x in range(x_size)]


def print_array(array):
    for r in array:
        for c in r:
            print(c, end=" ")
        print()


board = make_array(board_y, board_x)

# Get a no_of_bombs amount of unique coordinates
random_coordinates = []
for bombs in range(no_of_bombs):
    duplicate = True
    while duplicate:
        coordinate = get_random_coordinate(board_y, board_x)
        if coordinate in random_coordinates:
            duplicate = True
        else:
            random_coordinates.append(coordinate)
            duplicate = False

# Assign bomb positions
for coordinate in random_coordinates:
    x, y = coordinate
    board[x][y] = bomb

# Assign numbers around bombs
for x in range(board_y):
    for y in range(board_x):
        if board[x][y] != bomb:
            surrounding_bomb_counter = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < board_y and 0 <= j < board_x:
                            if board[i][j] == bomb:
                                surrounding_bomb_counter += 1

            board[x][y] = surrounding_bomb_counter

print_array(board)
