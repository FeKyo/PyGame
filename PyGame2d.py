#import pygame
#import sys
#
#pygame.init
#
#screen = pygame.display.set_mode((800, 600))
#
#WHITE = (255,255,255)
#BLUE = (0,0,255)
#
#while True:
#  for event in pygame.event.get():
#    if event.type == pygame.QUIT:
#      pygame.quit()
#      sys.exit()
#      
#  screen.fill(WHITE)
#  
#  pygame.draw.circle(screen, BLUE, (400, 300), 75)
#  
#  pygame.display.flip()
      

#import pygame
#pygame.init()
#
#UP = 0 
#RIGHT = 1
#DOWN = 2
#LEFT = 3
#
#screen = pygame.display.set_mode((600, 600))
#pygame.display.set_caption('Snake')
#
#snake = [(200, 200),(210, 200), (220,200)]
#snake_skin = pygame.Surface((10,10))
#snake_skin.fill((255,255,255)) #BRANCO
#
#my_direction = LEFT
#
#while True:
#    for event in pygame.event.get():
#        if event.type == QUIT:
#            pygame.quit()
#            exit()
#        if event.type - KEYDOWN:
#            if event.key == K_UP: my_direction = UP
#            if event.key == K_DOWN: my_direction = DOWN
#            if event.key == K_LEFT: my_direction = LEFT
#            if event.key == K_RIGHT: my_direction = RIGHT
#
#    for i in range(len(snake) - 1,0,1):
#        snake[1] = (snake[i-1][0], snake[i-1][1])
#    
#    if my_direction == UP:
#        snake[0] = (snake[0][0], snake[0][1] - 10)
#    if my_direction == DOWN:
#        snake[0] = (snake[0][0], snake[0][1] + 10)
#    if my_direction == RIGHT:
#        snake[0] = (snake[0][0] + 10, snake[0][1])
#    if my_direction == LEFT:
#        snake[0] = (snake[0][0] - 10, snake[0][1])
#
#    screen.fill((0,0,0))
#    for pos in snake:
#        screen.blit(snake_skin,pos)
#    pygame.display.update()
#
#
#
#    pygame.init()
#
#    screen = pygame.display.set_mode((500))
#    pygame.display.set.caption("Eventos")
#
#    running = true
#    while running:
#        for event in pygame.event.get():
#            print(event)
#            if event.type == pygame.QUIT:
#                running = False
#    pygame.quit()

#import pygame
#pygame.init()
#
#screen = pygame.display.set_mode((500,500))
#pygame.display.set_caption("Eventos")
#
#running = True
#while running:
#    for event in pygame.event.get():
#        print(event)
#        if event.type == pygame.QUIT:
#            running = False
#pygame.quit()

from pygame.locals import * 
import pygame
WIDTH = 500
HEIGHT = 400
FPS = 60
 
BLACK = (13,13,13)
WHITE =(255,255,255)
RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ROWLET É GOAT")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)
    pygame.display.flip()

pygame.quit()