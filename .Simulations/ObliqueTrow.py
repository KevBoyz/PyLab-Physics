import pygame
from math import sqrt

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()
clock = pygame.time.Clock()
width, height = 900, 630
window = pygame.display.set_mode((width, height))
bg = pygame.transform.scale(pygame.image.load('../Sprites/space-bg.jpg'), (width, height))


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../Sprites/chao.png')
        self.rect = self.image.get_rect(center=(10, 610))


class Cannon:


    def __init__(self):
        self.x = 10
        self.y = 466
        self.lines = []
        self.last_pos = 0

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.last_pos = pygame.mouse.get_pos()
                if len(self.lines) > 0:
                    self.lines.pop()
                self.lines.append(self.last_pos)
        for pos in self.lines:
            x = pos[0]
            y = pos[1]
            dx = x - self.x
            dy = y - self.y
            d = sqrt(dx**2 + dy**2)
            print(d, dx, dy)
            pygame.draw.line(window, red, (self.x, self.y), (x, y))


ground = pygame.sprite.GroupSingle(Ground())
cannon = Cannon()
while True:
    clock.tick(-1)
    window.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    ground.draw(window)
    cannon.update()
    pygame.display.update()


