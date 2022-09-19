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
                f = 2 * 1/d
            else:
                f = 2 * 1/1
            if self.polarity == -1 and p.polarity == 1:
                if d > 0:
                    self.fx += f * dx
                    self.fy += f * dy
                self.x += self.fx/1
                self.y += self.fy/1
            elif self.polarity == -1 and p.polarity == -1:
                if d <= 50 and d > 0:
                    self.fx -= (f * dx)/1
                    self.fy -= (f * dy)/1
                self.x += self.fx/1000
                self.y += self.fy/1000
            elif self.polarity == 1 and p.polarity == 1:
                if d <= 150 and d > 0:
                    self.fx += f * dx
                    self.fy += f * dy
                else:
                    self.fx = 0
                    self.fy = 0
                self.x += self.fx
                self.y += self.fy
            
def main():
    run = True
    clock = pygame.time.Clock()

    particles = []
    for c in range(0, 50):
        particles.append(Particle(rand(), RED, 6, 1))
    for c in range(0, 20):
        particles.append(Particle(rand(), GREEN, 5, -1))

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
