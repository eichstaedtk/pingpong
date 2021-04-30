import pygame

WINDOW_HEIGHT = 640
WINDOW_WIDTH = 480
RACKET_HEIGHT = 100


def start():
    pygame.init()
    ORANGE = (255, 140, 0)
    ROT = (255, 0, 0)
    GRUEN = (0, 255, 0)
    SCHWARZ = (0, 0, 0)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Ping Pong Game made by @Konrad")
    game_active = True
    clock = pygame.time.Clock()
    run_screen(screen, SCHWARZ, clock, game_active)


def run_screen(screen, background_color, clock, game_active):
    ball_1_y = 10
    ball_1_x = 30
    move_y = 4
    move_x = 4

    player_1_x = 20
    player_1_y = 20
    player_1_move = 0

    while game_active:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_active = False
                print("Game over ....")

            if event.type == pygame.KEYDOWN:

                # Taste für Spieler 1
                if event.key == pygame.K_UP:
                    player_1_move = -6
                elif event.key == pygame.K_DOWN:
                    player_1_move = 6

        screen.fill(background_color)

        draw_game(screen, ball_1_y, ball_1_x, player_1_x, player_1_y)

        ball_1_x += move_x
        ball_1_y += move_y

        if ball_1_y > WINDOW_HEIGHT or ball_1_y < 0:
            move_y = move_y * -1

        if ball_1_x > WINDOW_WIDTH or ball_1_x < 0:
            move_x = move_x * -1

        if player_1_move != 0:
            player_1_y += player_1_move

        if player_1_y < 0:
            player_1_y = 0

        if player_1_y > WINDOW_HEIGHT - RACKET_HEIGHT:
            player_1_y = WINDOW_HEIGHT - RACKET_HEIGHT

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


def draw_game(screen, ball_1_y, ball_1_x, player_1_x, player_1_y):
    weiss = (255, 255, 255)
    pygame.draw.ellipse(screen, weiss, [ball_1_x, ball_1_y, 20, 20])

    pygame.draw.rect(screen, weiss, [player_1_x, player_1_y, 20, RACKET_HEIGHT])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
