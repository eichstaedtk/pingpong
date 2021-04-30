import pygame


def start():
    pygame.init()
    ORANGE = (255, 140, 0)
    ROT = (255, 0, 0)
    GRUEN = (0, 255, 0)
    SCHWARZ = (0, 0, 0)
    WEISS = (255, 255, 255)
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Ping Pong Game made by @Konrad")
    game_active = True
    clock = pygame.time.Clock()
    run_screen(screen,SCHWARZ,clock, game_active)


def run_screen(screen, background_color, clock, game_active):
    while game_active:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                print("Game over ....")

        screen.fill(background_color)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
