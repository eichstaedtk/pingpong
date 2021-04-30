import pygame

WINDOW_HEIGHT = 640
WINDOW_WIDTH = 480
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)


def start():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Ping Pong Game made by @Konrad")
    game_active = True
    clock = pygame.time.Clock()
    run_screen(screen, clock, game_active)


def run_screen(screen, clock, game_active):
    ball_y = 10
    ball_x = 30
    ball_move_y = 4
    ball_move_x = 4
    racket_height = 100

    player_1_x = 20
    player_1_y = 20
    player_1_move = 0
    player_2_x = WINDOW_WIDTH - (2 * 20)
    player_2_y = 20
    player_2_move = 0
    ball_switch = 0

    while game_active:

        for event in pygame.event.get():
            game_active, player_1_move, player_2_move = handle_key_events(event, game_active, player_1_move,
                                                                          player_2_move)

        screen.fill(COLOR_BLACK)

        player1, player2, ball = draw_game(screen, ball_y, ball_x, player_1_x, player_1_y, player_2_x,
                                           player_2_y, racket_height)

        ball_x += ball_move_x
        ball_y += ball_move_y

        if ball_y > WINDOW_HEIGHT or ball_y < 0:
            ball_move_y = ball_move_y * -1

        if ball_x > WINDOW_WIDTH or ball_x < 0:
            ball_move_x = ball_move_x * -1

        if player_1_move != 0:
            player_1_y += player_1_move

        if player_1_y < 0:
            player_1_y = 0

        if player_1_y > WINDOW_HEIGHT - racket_height:
            player_1_y = WINDOW_HEIGHT - racket_height

        if player_2_move != 0:
            player_2_y += player_2_move

        if player_2_y < 0:
            player_2_y = 0

        if player_2_y > WINDOW_HEIGHT - racket_height:
            player_2_y = WINDOW_HEIGHT - racket_height

        if player1.colliderect(ball):
            ball_move_x = ball_move_x * -1
            ball_x = 40
            ball_switch += 1
            racket_height -= 5

        if player2.colliderect(ball):
            ball_move_x = ball_move_x * -1
            ball_x = player_2_x - 40
            ball_switch += 1
            racket_height -= 5

        ausgabetext = "Ballwechsel: " + str(ball_switch)
        font = pygame.font.SysFont(None, 40)
        text = font.render(ausgabetext, True, COLOR_RED)
        screen.blit(text, [100, 10])

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


def handle_key_events(event, game_active, player_1_move, player_2_move):
    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        game_active = False
        print("Game over ....")
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            player_1_move = -6
        elif event.key == pygame.K_DOWN:
            player_1_move = 6

        elif event.key == pygame.K_w:
            player_2_move = -6
        elif event.key == pygame.K_s:
            player_2_move = 6
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            player_1_move = 0
        elif event.key == pygame.K_w or event.key == pygame.K_s:
            player_2_move = 0
    return game_active, player_1_move, player_2_move


def draw_game(screen, ball_1_y, ball_1_x, player_1_x, player_1_y, player_2_x, player_2_y, racket_height):
    ball = pygame.draw.ellipse(screen, COLOR_WHITE, [ball_1_x, ball_1_y, 20, 20])
    player_1 = pygame.draw.rect(screen, COLOR_WHITE, [player_1_x, player_1_y, 20, racket_height])
    player_2 = pygame.draw.rect(screen, COLOR_WHITE, [player_2_x, player_2_y, 20, racket_height])
    return player_1, player_2, ball


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
