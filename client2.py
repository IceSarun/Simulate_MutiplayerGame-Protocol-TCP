import pygame
from network import Network
from player import Player

width = 500
height = 500
backg = pygame.image.load("backG.jpg") 
win = pygame.display.set_mode((width, height),0,32)
pygame.display.set_caption("Simulate Multiplayer Game Beta Version")

def redrawWindow(win,p1, p2):
    # win.fill((255,0,255))
    win.blit(backg,(0,0))
    p1.draw(win)
    p2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getPose()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2)

main()

