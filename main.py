import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Маршрутка в Нижнем Новгороде (или ад на иву)")
clock = pygame.time.Clock()
FPS = 60

STATE_START = "start"
STATE_PLAYING = "playing"
STATE_GAMEOVER = "gameover"
STATE_WIN = "win"

state = STATE_START


def main_loop():
    global state
    running = True

    while running:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if state == STATE_START and event.key == pygame.K_SPACE:
                    state = STATE_PLAYING

        screen.fill((135, 206, 235))

        if state == STATE_START:
            font = pygame.font.SysFont("arial", 64)
            text = font.render("Маршрутка: Кузнечиха - Львовская", True, (0, 0, 0))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 50))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main_loop()
