import pygame

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


class Ball(pygame.sprite.Sprite):
    def __init__(self, angle, vel, color, mass=1, radius=10, gravity=1.5, x=10, y=466):
        super().__init__()
        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x, self.y), (50, 100))
        self.radius = radius
        self.color = color
        self.angle = min(angle, 90)
        self.mass = mass
        self.xvel = self.yvel = vel
        self.gravity = gravity
        self.time = 0
        self.state = 'normal'
        self.route = []

    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
        try:
            pygame.draw.lines(window, green, False, self.route, 2)
        except ValueError:
            pass

    def lance(self):
        self.route.append((self.x, self.y))
        self.yvel -= self.time * self.gravity
        self.x += self.xvel
        self.y -= self.yvel
        self.time += 1


    def update(self):
        if self.y > 850:
            self.state = 'dead'
        if pygame.sprite.groupcollide(ball1, ground, False, False):
            if self.state == 'lanced':
                self.state = 'normal'
                self.x -= self.xvel
                self.y += self.yvel + 2
                self.yvel = self.xvel
                self.time = 0
            else:
                self.y -= 1
        else:
            if self.state == 'normal':
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.state = 'lanced'
            elif self.state == 'lanced':
                self.lance()

        self.rect = pygame.Rect((self.x, self.y), (self.radius, self.radius))
        self.draw()


ball1 = pygame.sprite.GroupSingle(Ball(45, 30, blue))
# ball2 = pygame.sprite.GroupSingle(Ball(155, 235, 10, red, 0, 7, 7, 8))
ground = pygame.sprite.GroupSingle(Ground())
while True:
    clock.tick(20)
    window.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    ground.draw(window)
    ball1.update()
    # ball2.update()
    pygame.display.update()


