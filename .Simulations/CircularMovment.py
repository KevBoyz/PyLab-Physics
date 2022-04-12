import pygame

from common import *
from pygame.locals import QUIT, K_a, K_d, K_SPACE
from pygame.image import load
from pygame.sprite import Sprite, GroupSingle, Group, groupcollide
from pygame.time import Clock
from pygame.transform import scale
import math

pygame.init()
window = pygame.display.set_mode((900, 630))
bg = scale(load('../Sprites/space-bg.jpg'), (900, 630))
clock = Clock()


class Ball(Sprite):

    def __init__(self):
        super().__init__()
        self.image = load('../Sprites/sun.png')
        self.rect = self.image.get_rect(center=(450, 315))
        self.ray = 100
        self.angle = 0

    def update(self):
        self.angle += 0.07
        position = pygame.Vector2((math.cos(self.angle * 3) * self.ray) + 415,
                                  (math.sin(self.angle * 2) * self.ray) + 300)
        self.rect = position


ball = GroupSingle(Ball())
while True:
    clock.tick(60)
    window.blit(bg, (0, 0))
    ball.draw(window)
    ball.update()


    for ev in pygame.event.get():  # Close event
        if ev.type == QUIT:
            break
    pygame.display.update()
