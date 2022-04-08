from common import *
from pygame.locals import QUIT, K_a, K_d, K_SPACE
from pygame.image import load
from pygame.sprite import Sprite, GroupSingle, Group, groupcollide
from pygame.time import Clock
from pygame.transform import scale

pygame.init()
window = pygame.display.set_mode((900, 630))
bg = scale(load('../Sprites/space-bg.jpg'), (900, 630))
clock = Clock()

gravity = 1.5
friction = 1


class Solo(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('../Sprites/chao.png')
        self.rect = self.image.get_rect(center=(450, 585))


class Box1(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('../Sprites/box1.png')
        self.rect = self.image.get_rect(center=(225, 135))
        self.mass = 3
        self.horizontal_speed = 5
        self.vertical_speed = 0
        self.vertical_initial_speed = 9
        self.state = 'falling'
        self.time = 0
        self.obstacle_mass = 1


    def update(self):
        global solo, box1, box2
        keys = pygame.key.get_pressed()
        if groupcollide(solo, box1, False, False):
            self.state = 'normal'
            self.rect.y -= 5
        if self.state == 'normal':
            if keys[K_d]:
                if groupcollide(box1, box2, False, False):
                    self.rect.x += (self.horizontal_speed - friction) - self.obstacle_mass
                else:
                    self.rect.x += self.horizontal_speed - friction
            elif keys[K_a]:
                self.rect.x -= self.horizontal_speed - friction
            elif keys[K_SPACE]:
                self.state = 'jumping'
                self.time = 0
                self.vertical_speed = 0
        elif self.state == 'jumping':
            if self.vertical_speed > 0:
                self.state = 'falling'
            self.vertical_speed -= self.vertical_initial_speed - gravity * self.time
            self.rect.y += self.vertical_speed
            self.time += 1
        elif self.state == 'falling':
            self.rect.y += gravity * self.time
            self.time += 1


class Box2(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('../Sprites/box2.png')
        self.rect = self.image.get_rect(center=(495, 165))
        self.mass = 1
        self.state = 'falling'
        self.time = 0
        self.obstacle_force = 3

    def update(self):
        global solo, box1, box2
        if groupcollide(solo, box2, False, False):
            self.state = 'normal'
            self.rect.y -= 1
        if self.state == 'normal':
            if groupcollide(box1, box2, False, False):
                self.rect.x += self.obstacle_force
        elif self.state == 'falling':
            self.rect.y += gravity * self.time
            self.time += 1



solo = GroupSingle(Solo())
box1 = GroupSingle(Box1())
box2 = GroupSingle(Box2())
while True:
    clock.tick(15)
    window.blit(bg, (0, 0))
    box1.draw(window)
    box2.draw(window)
    drawMesh(window)
    solo.draw(window)
    box1.update()
    box2.update()
    for ev in pygame.event.get():  # Close event
        if ev.type == QUIT:
            break
    pygame.display.update()
