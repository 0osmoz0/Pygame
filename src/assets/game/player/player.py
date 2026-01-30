# /src/game/player/player.py

import pygame
import os 


class Player(object):
    def __init__(self, x, y):


        self.speed = 5
         
        self.direction = "right"

        #animation 
        self.frame_index = 0
        self.animation_speed = 120 # speed en ms 
        self.last_update = pygame.time.get_ticks()

        # je charge les sprite de pacman
        self.images = {
            "right" : self.load_images("pacman-right"),
            "left" :  self.load_images("pacman-left"),
            "up" :  self.load_images("pacman-up"),
            "down" :  self.load_images("pacman-down"),
        }
        self.image = self.images[self.direction][self.frame_index]
        self.rect = self.image.get_rect(center=(x, y))
    
    def load_images(self, folder):
        path = os.path.join("assets", "pacman-art", folder)
        images = []
        for i in range (1, 4):
            img = pygame.image.load(os.path.join(path, f"{i}.png")).convert_alpha()
            img = pygame.transform.scale(img, (64, 64))
            images.append(img)
        return images

    # Afficher le player 
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def move(self, dx, dy, direction):
        self.rect.x += dx
        self.rect.y += dy
        self.direction = direction
        self.animate()

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.frame_index = (self.frame_index + 1) % len(self.images[self.direction])
            self.image = self.images[self.direction][self.frame_index]
       
        
        
        

        


