import pygame
from settings import *
from assets.game_funcs import Spritesheet

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Little Bunny Knows Kung Fu-Fu")
clock = pygame.time.Clock()

# Load backgrounds
background = pygame.image.load("assets/graphics/environment/littleBunnyKungFuFu.png").convert_alpha()
sprite_sheet_image = pygame.image.load('assets/graphics/character/sprite_move_test.png').convert_alpha()

# Load spritesheet
sprite_sheet = Spritesheet(sprite_sheet_image)


animation_list = []
animation_steps = [1, 2, 1, 2, 1, 2, 1, 2]
action = 1
last_update = pygame.time.get_ticks()
animation_cooldown = 250
frame  = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 20, 16, 3, BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #show background
    screen.blit(background, (0,0))

    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    #show frame image
    screen.blit(animation_list[action][frame], (0, 0))


    pygame.display.update()
    
pygame.quit()