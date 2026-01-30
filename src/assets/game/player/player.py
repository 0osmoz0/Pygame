# /src/game/player/player.py

import pygame
import os 


class Player(object):
    def __init__(self, x, y):
        # on charge l'image de pacman
        self.image = pygame.image.load(os.path.join("assets", "pacman-art", "pacman-right", "1.png"))

        # on creer un rect a partir de l'image 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    # Afficher le player 
    def draw(self, screen):
        screen.blit(self.image, self.rect)

        


