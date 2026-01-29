import pygame 


# initialiser le projet pygame
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True 

# couleur du jeu
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#caracteristique 
speed = [1, 1]
gravity = 0.1

# button quitter le jeu 
button_rect = pygame.Rect(0, 0, 50, 25)
font = pygame.font.Font(None, 13)
button_text = font.render("Quitter", True, WHITE)

# Player 1
Player_1 = pygame.Rect(400, 300, 50, 50)


while running:
    # event pour quitter le jeu soit CMD + Q soit le button quitter 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                running = False
            
    # faire disparaitre l'écrans 
    screen.fill((0, 0, 0))


    #creer de la graviter 
    speed[1] += gravity
    Player_1 = Player_1.move(speed)

    # transformer le screen en rect 
    screen_rect = screen.get_rect()
    # empeche le player de sortir de l'ecrans 
    if not screen_rect.contains(Player_1):
        Player_1.clamp_ip(screen_rect) 
        

    # Afficher le boutton sur l'écrans 
    pygame.draw.rect(screen, RED, button_rect)
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))

    #affiche le Player sur l'écrans 
    pygame.draw.rect(screen, WHITE, Player_1)

    #mise a jour de l'écrans 
    pygame.display.flip()

    #limiter le jeu a 60fps 
    clock.tick(60)

pygame.quit 