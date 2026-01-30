# /src/game/main.py

import pygame 
from player.player import Player

# initialiser le projet pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True 


player = Player(960, 590)


while running:
    # event pour quitter le jeu soit CMD + Q soit le button quitter 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # faire disparaitre l'écrans 
    screen.fill((0, 0, 0))

    # afficher le player (pacman)
    player.draw(screen)

    #mise a jour de l'écrans 
    pygame.display.flip()

    #limiter le jeu a 60fps 
    clock.tick(60)

pygame.quit  