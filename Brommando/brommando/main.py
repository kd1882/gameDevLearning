# Example file showing a circle moving on screen
import os
import pygame

# pygame setup
pygame.init()
#load and set the logo
# load and set the logo
# logo = pygame.image.load("brommando_logo_test.png")

# pygame.display.set_icon(logo)
pygame.display.set_caption("BROMMANDO")

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

grass_texture = pygame.image.load('assets/asset_packs/grass.jpg')
rock_1 = pygame.image.load('assets/asset_packs/Free 2D Animated Vector Game Character Sprites/Environment/rock2.png')
brommando_logo = pygame.image.load('assets/artwork/brommando_logo_test.png')
test_font = pygame.font.Font('assets/asset_packs/font/Pixeltype.ttf', 50)
text_surface = test_font.render('BROMMANDO', False, 'Black')
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    ## poll for events
    ## pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(grass_texture, (0,0))
    screen.blit(brommando_logo, (360, 260))
    screen.blit(text_surface, (500, 600))



    pygame.display.update()

    ## fill the screen with a color to wipe away anything from last frame
    # screen.fill("dark green")
    # pygame.draw.circle(screen, "black", player_pos, 40)
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * dt

    ## flip() the display to put your work on screen
    # pygame.display.flip()

    ## limits FPS to 60
    ## dt is delta time in seconds since last frame, used for framerate-
    ## independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

## if __name__=="__main__":
##     # call the main function
##     main()