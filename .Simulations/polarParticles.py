import pygame
import math
from random import randint
from time import sleep

pygame.init()

WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
PURPLE = (128,0,128)

FONT = pygame.font.SysFont("comicsans", 16)


def rand():
    return randint(300, 800), randint(200, 500)


class Particle:
    def __init__(self, pos, color, radius, polarity):
        self.color = color
        self.radius = radius
        self.polarity = polarity
        self.x, self.y = pos
        self.fx, self.fy = 0, 0
        self.r = r = 150 * self.polarity
        self.r_origin = self.r

    def draw(self, win):
        x = self.x
        y = self.y 
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def update_position(self, particles):
        for p in particles:
            dx = (self.x - p.x) * self.polarity
            dy = (self.y - p.y) * self.polarity
            d = math.sqrt(dx ** 2 + dy ** 2)
            if d > 0:
                f = 3 * 2/d
            else:
                f = 2 * 1/1
            if self.polarity <= -1 and p.polarity >= 1:
                if d > 0:
                    self.fx += (f * dx) * p.polarity 
                    self.fy += (f * dy) * p.polarity 
                self.x += self.fx/500
                self.y += self.fy/500
            elif self.polarity <= -1 and p.polarity <= -1:
                if 50 >= d > 0:
                    self.fx += (f * dx * 2) * p.polarity 
                    self.fy += (f * dy * 2) * p.polarity 
                self.x += self.fx/500
                self.y += self.fy/500
            elif self.polarity >= 1 and p.polarity >= 1:
                if self.r < p.r:
                    self.r = p.r
                if self.r >= d > 0:
                    self.fx += (f * dx)/2
                    self.fy += (f * dy)/2
                else:
                    self.fx = 0
                    self.fy = 0
                self.x += self.fx
                self.y += self.fy
                self.r = self.r_origin


def main():
    run = True
    clock = pygame.time.Clock()
    particles = []
    for c in range(0, 20):  # atoms
        particles.append(Particle(rand(), RED, 6, 1))
    for c in range(0, 5):  # eletrons
        particles.append(Particle(rand(), GREEN, 5, -1))
    for c in range(0, 1):  # cations
        particles.append(Particle(rand(), YELLOW, 7, 2))
    for c in range(0, 5):  # anions
        particles.append(Particle(rand(), PURPLE, 5, -4))
    for c in range(0, 0):  # neutrons
        particles.append(Particle(rand(), BLUE, 4, 0))

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))

        for particle in particles:
            particle.draw(WIN)
            particle.update_position(particles)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

main()
