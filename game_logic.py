import random


def distribute_bombs(board_size, number_of_bombs):
    board = [['n' for i in range(board_size)] for j in range(board_size)]
    bombs = []
    board_size = len(board)
    while len(bombs) < number_of_bombs:
        x = random.randint(0, board_size ** 2 - 1)
        if x not in bombs:
            bombs.append(x)
    for bomb in bombs:
        board[bomb // board_size][bomb % board_size] = 'b'
    return board


def check_neighbors(board_list, i, j):
    board_size = len(board_list)
    counter = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dr, dc in directions:
        new_row, new_col = i + dr, j + dc
        if 0 <= new_row < board_size and 0 <= new_col < board_size and board_list[new_row][new_col] == 'b':
            counter += 1
    return counter


def get_location(mouse_x, mouse_y, board_size):
    x = (mouse_x - 48) // 36
    y = (mouse_y - 48) // 36
    if x < 0 or y < 0 or x >= board_size or y >= board_size:
        return -1, -1
    return x, y


def board_to_size(board_cells):
    return 96 + board_cells * 32 + 4 * (board_cells - 1), 96 + board_cells * 32 + 4 * (board_cells - 1)


def reveal_empty_cells(board, x, y, revealed, flags):
    if ((x, y) not in revealed) and (board[x][y] == 'n') and ((x, y) not in flags):
        revealed.append((x, y))
        if board[x][y] == 'n' and check_neighbors(board, x, y) == 0:
            if x + 1 < len(board):
                reveal_empty_cells(board, x + 1, y, revealed, flags)
            if 0 <= x - 1:
                reveal_empty_cells(board, x - 1, y, revealed, flags)
            if y + 1 < len(board[0]):
                reveal_empty_cells(board, x, y + 1, revealed, flags)
            if 0 <= y - 1:
                reveal_empty_cells(board, x, y - 1, revealed, flags)

    return revealed
