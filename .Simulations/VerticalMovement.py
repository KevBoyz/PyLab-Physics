from common import *
from pygame.locals import QUIT, K_a, K_d, K_SPACE
from pygame.image import load
from pygame.sprite import Sprite, GroupSingle
from pygame.time import Clock
from pygame.transform import scale

pygame.init()


class Chao(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('../Sprites/chao.png')
        self.rect = self.image.get_rect(center=(450, 585))


class Ball(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('../Sprites/cannonBallContrast.png')
        self.rect = self.image.get_rect(center=(226, 420))
        self.time = 0
        self.fall = False
        self.gravity = 1.5
        self.speed = 50
        self.jumping = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_d]:
            self.rect.x += 5
        elif keys[K_a]:
            self.rect.x -= 5
        if keys[K_SPACE]:
            self.jumping = True
        if self.jumping:
            if self.fall:
                self.fallBall()
            else:
                if self.speed - int(self.gravity * self.time) < 0:
                    self.rect.y -= 1
                    self.rect.y -= 1
                    self.rect.y -= 1
                    self.fall = True
                    self.speed = 50
                    self.time = 0
                else:
                    self.speed -= int(self.gravity * self.time)
                    self.rect.y -= self.speed
                    self.time += 1


    def fallBall(self):
        keys = pygame.key.get_pressed()
        if keys[K_d]:
            self.rect.x += 5
        elif keys[K_a]:
            self.rect.x -= 5
        if self.rect.y >= 370:
            if self.rect.y == 386:
                for c in range(0, 5):
                    self.rect.y += 1
            elif self.rect.y == 396:
                self.rect.y -= 5
            self.fall = False
            self.time = 0
            self.rect.y += 5
            self.jumping = False
        else:
            self.rect.y += self.time * self.gravity
            self.time += 1


window = pygame.display.set_mode((900, 630))
window.fill((5, 5, 5))
bg = scale(load('../Sprites/space-bg.jpg'), (900, 630))
chao = GroupSingle(Chao())
ball = GroupSingle(Ball())
clock = Clock()
while True:
    clock.tick(20)
    window.blit(bg, (0, 0))
    drawMesh(window)
    for ev in pygame.event.get():  # Close event
        if ev.type == QUIT:
            break
    chao.draw(window)
    ball.draw(window)
    ball.update()
    pygame.display.update()
