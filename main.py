import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Маршрутка в Нижнем Новгороде (или ад на иву)")
clock = pygame.time.Clock()

STATE_START = "start"

state = STATE_START


def main_loop():
    global state
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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
