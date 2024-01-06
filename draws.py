import pygame


def draw_game_over(screen, width, height, win):
    if win:
        text = "YOU WIN!"
    else:
        text = "YOU LOSE!"
    pygame.draw.rect(screen, (255, 255, 255), (0, height // 2 - 32, width, 64))
    font = pygame.font.Font(None, 64)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = (width // 2, height // 2)
    screen.blit(text_surface, text_rect)


def draw_numbers(numbers_list, flags, revealed, screen):
    font = pygame.font.Font(None, 32)
    for number in numbers_list:
        if ((number[0], number[1]) not in flags) and ((number[0], number[1]) in revealed):
            if number[2] == 1:
                text_color = (0, 0, 255)
            elif number[2] == 2:
                text_color = (0, 180, 0)
            elif number[2] == 3:
                text_color = (255, 0, 0)
            else:
                continue
            text_surface = font.render(str(number[2]), True, text_color)
            text_rect = text_surface.get_rect()
            text_rect.center = (64 + number[0] * 36, 64 + number[1] * 36)
            screen.blit(text_surface, text_rect)


def draw_flags(screen, flags):
    for flag in flags:
        vertices = [(56 + 36 * flag[0], 68 + 36 * flag[1]), (56 + 36 * flag[0], 60 + 36 * flag[1]),
                    (72 + 36 * flag[0], 64 + 36 * flag[1])]
        pygame.draw.polygon(screen, (255, 0, 0), vertices)


def draw_bombs(screen, grid_list, flags, game_over):
    if game_over:
        for i, x in enumerate(grid_list):
            for j, y in enumerate(x):
                if y == 'b':
                    if (i, j) not in flags:
                        pygame.draw.circle(screen, (0, 0, 0), (64 + 36 * i, 64 + 36 * j), 8)


def draw_board(n, revealed, screen):
    for i in range(n):
        for j in range(n):
            rect_width, rect_height = 32, 32
            if (i, j) in revealed:
                rect_color = (100, 100, 100)
            else:
                rect_color = (200, 200, 200)
            rect_x, rect_y = 48 + 36 * i, 48 + 36 * j
            pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
