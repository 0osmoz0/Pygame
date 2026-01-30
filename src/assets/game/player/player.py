# /src/game/player/player.py

import pygame
import os 


class Player(object):
    def __init__(self, x, y):
        # on charge l'image de pacman
        self.image = pygame.image.load(os.path.join("assets", "pacman-art", "pacman-right", "1.png"))

        # on creer un rect a partir de l'image 
        self.image = pygame.transform.scale(
           self.image, (64, 64)
        )
        self.rect = self.image.get_rect(center=(x, y))

        self.w = 64
        self.h = 64

    # Afficher le player 
    def draw(self, screen):
        screen.blit(self.image, self.rect)

        


