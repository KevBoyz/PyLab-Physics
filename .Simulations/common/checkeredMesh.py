import pygame


def drawMesh(screen):
    for i in range(0, 900, 90):
        horizontal_line = pygame.Surface((900, 1), pygame.SRCALPHA)
        horizontal_line.fill((0, 255, 0, 100))
        screen.blit(horizontal_line, (0, i - 1))
        # Vertical Surface
        vertical_line = pygame.Surface((1, 700), pygame.SRCALPHA)
        vertical_line.fill((0, 255, 0, 100))
        screen.blit(vertical_line, (i - 1, 0))

