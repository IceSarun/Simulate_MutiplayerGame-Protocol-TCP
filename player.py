import pygame

class Player():
    def __init__(self, x, y, width, radius, color):
        self.x = x
        self.y = y
        self.width = width
        self.radius = radius
        self.color = color
        self.circle = x,y 
        self.vel = 3

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.circle, self.radius)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        # Update position
        self.update()
    
    def update(self):
        self.circle = (self.x, self.y)
