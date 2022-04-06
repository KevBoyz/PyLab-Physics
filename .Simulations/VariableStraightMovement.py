from common import *
from pygame.locals import QUIT, KEYDOWN, K_a, K_d
from pygame.image import load
from pygame.sprite import Sprite, GroupSingle
from pygame.time import Clock
from time import sleep
from pygame.transform import scale

pygame.init()


class Chao(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('../Sprites/chao.png')
        self.rect = self.image.get_rect(center=(450, 495))


class Car(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('../Sprites/car.png')
        self.rect = self.image.get_rect(center=(33, 343))
        self.time = 0
        self.a = 0.5
        self.stop = False

    def update(self):
        speed = self.a * self.time
        keys = pygame.key.get_pressed()
        if self.rect.x > 950:
            self.rect.x = -120
        elif self.rect.x < -150:
            self.rect.x = 933
        if keys[K_d]:
            self.rect.x += speed
            self.time += 1
        elif keys[K_a]:
            self.rect.x += speed
            if self.time > 0:
                self.time -= 3
            else:
                self.time -= 1
        elif not keys[K_d] and not keys[K_a]:
            if self.time > 0:
                self.time -= 1  # Força de atrito
            elif self.time < 0:
                self.time += 1
            self.rect.x += speed





window = pygame.display.set_mode((900, 630))
window.fill((5, 5, 5))
bg = scale(load('../Sprites/space-bg.jpg'), (900, 630))
chao = GroupSingle(Chao())
car = GroupSingle(Car())
clock = Clock()
while True:
    clock.tick(30)
    window.blit(bg, (0, 0))
    drawMesh(window)
    for ev in pygame.event.get():  # Close event
        if ev.type == QUIT:
            break
    chao.draw(window)
    car.draw(window)
    car.update()
    pygame.display.update()

