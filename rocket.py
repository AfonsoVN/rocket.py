
import pygame
from pygame.locals import
from time import

pygame.init()
screen=pygame.display.set_mode((600,600))
player_x = 200
player_y = 200
keys = [False, False, False, False]
player = pygame.image.load("character.png")
background = pygame.image.load("bg.png")
while player_y < 600:
    screen.blit(background, (0,0))
    screen.blit(player, (player_x, player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #if it is quit the game
            pygame.quit()
            exit(0)
        #check if any keyboard button is pressed
        if event.type == pygame.KEYDOWN:
            #check which button is pressed
