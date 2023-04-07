import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

# Level Assets
sky_surface = pygame.image.load('assets/graphics/Sky.png').convert()
ground_surface = pygame.image.load('assets/graphics/ground.png').convert()
text_surface = test_font.render('Runner', False, "Black")

# Snail Assets
snail_surface = pygame.image.load('assets/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600,300))
snail_x_pos = 600

# Player Assets
player_surf = pygame.image.load('assets/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (350, 50))

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surf, player_rect)


    if player_rect.colliderect(snail_rect):
        print('collison')
    else:
        print('okay')



    pygame.display.update()
    clock.tick(60)