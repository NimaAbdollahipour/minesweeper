from draws import *
from game_logic import *

pygame.init()

NO_OF_BOMBS = 10
BOARD_SIZE = 10
width, height = board_to_size(BOARD_SIZE)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minesweeper")

board = distribute_bombs(BOARD_SIZE, NO_OF_BOMBS)
revealed = []
numbers = []
flags = []
game_over = False
win = False

while True:
    # Process Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            x, y = get_location(mouse_x, mouse_y, BOARD_SIZE)
            if event.button == 1:
                if x != -1:
                    if (x, y) not in revealed:
                        revealed = reveal_empty_cells(board, x, y, revealed, flags)
                        numbers = []
                        for item in revealed:
                            numbers.append((item[0], item[1], check_neighbors(board, item[0], item[1])))
                        if len(revealed) + NO_OF_BOMBS == BOARD_SIZE ** 2:
                            win = True
                            game_over = True
                        if (x, y) in flags:
                            flags.remove((x, y))
                        if board[x][y] == 'b':
                            game_over = True
            elif event.button == 3:
                if (x, y) not in flags:
                    flags.append((x, y))

    # Draw
    screen.fill((255, 255, 255))
    draw_board(len(board), revealed, screen)
    draw_numbers(numbers, flags, revealed, screen)
    draw_bombs(screen, board, flags, game_over)
    draw_flags(screen, flags)
    if game_over:
        draw_game_over(screen, width, height, win)
    pygame.display.flip()
