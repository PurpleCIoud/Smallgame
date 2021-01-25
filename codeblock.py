import pygame

W = 640
H = 640
running = True

screen = pygame.display.set_mode((W, H))


class Rectangle:
    def __init__(self, x, y):
        self.h = 64
        self.w = 64
        self.position_x = x
        self.position_y = y
        self.color = 'blue'

    def move(self, x, y):
        self.position_x += x
        self.position_y += y

    def draw(self):
        rectangle = pygame.draw.rect(screen, self.color, (self.position_x, self.position_y, self.h, self.w))
        return rectangle


square = Rectangle(10, 10)

while running:
    square.draw()
    pygame.time.delay(0)
    pygame.display.flip()
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                square.move(10, 0)
            elif event.key == pygame.K_a:
                square.move(-10, 0)
            elif event.key == pygame.K_s:
                square.move(0, 10)
            elif event.key == pygame.K_w:
                square.move(0, -10)
