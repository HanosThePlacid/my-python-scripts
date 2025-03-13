import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS


BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (66, 66, 66)
O_COLOR = (239, 231, 200)
TEXT_COLOR = (255, 255, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")


font = pygame.font.SysFont(None, 40)


board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]


def draw_grid():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "X":
                pygame.draw.line(screen, X_COLOR, 
                                 (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 20),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - 20, row * SQUARE_SIZE + SQUARE_SIZE - 20), LINE_WIDTH)
                pygame.draw.line(screen, X_COLOR,
                                 (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + SQUARE_SIZE - 20),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - 20, row * SQUARE_SIZE + 20), LINE_WIDTH)
            elif board[row][col] == "O":
                pygame.draw.circle(screen, O_COLOR,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 3, LINE_WIDTH)

def check_winner():
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]

    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    if all(board[row][col] is not None for row in range(BOARD_ROWS) for col in range(BOARD_COLS)):
        return "Tie"

    return None


def reset_game():
    global board, player
    board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = "X"

def draw_text(text):
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)

def main():
    global board, player
    player = "X"
    game_over = False

    reset_game()
    screen.fill(BG_COLOR)
    draw_grid()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: 
                    reset_game()
                    screen.fill(BG_COLOR)
                    draw_grid()
                    game_over = False
                if event.key == pygame.K_q:  
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX, mouseY = event.pos
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if board[clicked_row][clicked_col] is None:
                    board[clicked_row][clicked_col] = player
                    if player == "X":
                        player = "O"
                    else:
                        player = "X"

                    draw_figures()
                    winner = check_winner()
                    if winner:
                        game_over = True
                        if winner == "Tie":
                            draw_text("It's a Tie!")
                        else:
                            draw_text(f"Player {winner} wins!")

        pygame.display.update()

if __name__ == "__main__":
    main()