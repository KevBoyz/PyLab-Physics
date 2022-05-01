import pygame
import math
import time


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


def scenario_draw(win):
    for image, pos in [(GRASS, (0, 0)), (TRACK, (0, 0)), (TRACK_BORDER, (0, 0)), (FINISH, (0, 0))]:
        win.blit(image, pos)


GRASS = scale_image(pygame.image.load('../Sprites/TPC-simulation/grass.jpg'), 2)
TRACK = scale_image(pygame.image.load("../Sprites/TPC-simulation/track.png"), 0.9)
TRACK_BORDER = scale_image(pygame.image.load("../Sprites/TPC-simulation/track-border.png"), 0.9)
FINISH = pygame.image.load('../Sprites/TPC-simulation/finish.png')
RED_CAR = scale_image(pygame.image.load('../Sprites/TPC-simulation/red-car.png'), 0.55)
GREEN_CAR = scale_image(pygame.image.load('../Sprites/TPC-simulation/green-car.png'), 0.75)


class Car:
    def __init__(self, max_vel, rotation_vel):
        self.image = self.image
        self.x, self.y = self.start_pos
        self.vel = 0
        self.angle = 0
        self.acceleration = max_vel
        self.max_vel = max_vel
        self.rotation_vel = rotation_vel
        self.angulation = 0
        self.points = []

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()
        
    def move_backward(self):
        self.vel = max(self.vel - self.acceleration * 2, -self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        self.y -= vertical
        self.x -= horizontal
        # pygame.draw.line(window, (0, 255, 0), (self.x + 2, self.y + 5), (113 - 39, 113 - 9))

        pygame.draw.line(window, (255, 0, 0), (113 - 39, 113 - 9), (113 - 39, 113 * 2))
        pygame.draw.line(window, (255, 0, 0), (113 - 39, 113 * 2), (113 - 39 + 113, 113 * 2))
        pygame.draw.line(window, (255, 0, 0), (113 - 39, 113 * 2), (113 - 39 - 113, 113 * 2))
        pygame.draw.line(window, (255, 0, 0), (113 - 39, 113 * 2), (113 - 39, 113 * 2 + 113 - 7))

        pygame.draw.line(window, (0, 0, 255), (113 - 39 + 113, 113 * 2), (113 - 39, 113 - 9))

        self.points.append((self.x + 10, self.y + 18))
        try:
            pass
            pygame.draw.lines(window, (0, 0, 0), False, self.points, 2)
        except:
            pass

    def rotate(self, left=False, right=False):
        if self.vel == 0:
           pass
        else:
            if left:
                self.angle += self.rotation_vel
                if self.angle >= 0:
                    self.angulation = min(+self.angle % 360 / 4, 86)
                else:
                    self.angulation = -min(+self.angle % 360 / 4, 86)
            elif right:
                self.angle -= self.rotation_vel
                if self.angle >= 0:
                    self.angulation = min(+self.angle % 360 / 4, 94)
                else:
                    self.angulation = -min(+self.angle % 360 / 4, 94)

    def reduce_speed(self):
        self.vel = max(self.vel - 0.1 / 2, 0)
        self.move()

    def draw(self):
        blit_rotate_center(window, self.image, (self.x, self.y), self.angle)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move_forward()
        elif keys[pygame.K_s]:
            self.move_backward()
        if keys[pygame.K_d]:
            self.rotate(right=True)
        if keys[pygame.K_a]:
            self.rotate(left=True)
        self.reduce_speed()


class PlayerCar(Car):
    image = RED_CAR
    start_pos = 180, 200


height, width = TRACK.get_height(), TRACK.get_width()
window = pygame.display.set_mode((height, width))
pygame.display.set_caption('A cobra está fumando')
clock = pygame.time.Clock()


player_car = PlayerCar(4, 4)
while True:
    clock.tick(120)
    scenario_draw(window)
    player_car.draw()
    player_car.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    pygame.display.update()




