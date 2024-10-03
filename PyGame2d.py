import pygame
import random
from dataclasses import dataclass
pygame.init()

def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return(x*10, y*10)

UP = 0 
RIGHT = 1
DOWN = 2
LEFT = 3
width = 600
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

snake = [(200, 200),(210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255)) #BRANCO

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255, 0, 0))

my_direction = LEFT

clock = pygame.time.Clock()
FPS = 60

#while True:
    #clock.tick(10)
    #for event in pygame.event.get():
    #    if event.type == QUIT:
    #        pygame.quit()
    #        exit()
    #    if event.type == pygame.KEYDOWN:
    #        if event.key == K_UP: my_direction = UP
    #        if event.key == K_DOWN: my_direction = DOWN
    #        if event.key == K_LEFT: my_direction = LEFT
    #        if event.key == K_RIGHT: my_direction = RIGHT
#
    #for i in range(len(snake) - 1,0,1):
    #    snake[1] = (snake[i-1][0], snake[i-1][1])
    #
    #if my_direction == UP:
    #    snake[0] = (snake[0][0], snake[0][1] - 10)
    #if my_direction == DOWN:
    #    snake[0] = (snake[0][0], snake[0][1] + 10)
    #if my_direction == RIGHT:
    #    snake[0] = (snake[0][0] + 10, snake[0][1])
    #if my_direction == LEFT:
    #    snake[0] = (snake[0][0] - 10, snake[0][1])
#
    #screen.fill((0,0,0))
    #screen.blit(apple, apple_pos)
    #for pos in snake:
    #    screen.blit(snake_skin,pos)
    #pygame.display.update()
#




    #screen = pygame.display.set_mode((450, 200))
    #pygame.display.set.caption("Eventos")

    #running = True
    #while running:
    #    for event in pygame.event.get():
    #        print(event)
    #        if event.type == pygame.QUIT:
    #            running = False
    #pygame.quit()


running = True
player_image = pygame.image.load('goat.png')
player_image.convert()
player = pygame.transform.scale
(player_image, (50, 75))

moving_right = False
moving_left = False
@dataclass
class PlayerLocation:
    x:int
    y:int
player_Location = PlayerLocation(x=155, y=125)
velocity = 3.5
while running:

    if moving_right:
        player_Location.x += velocity
    if moving_left:
        player_Location.x -= velocity

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: moving_left = True #my_direction = LEFT
            if event.key == pygame.K_RIGHT: moving_right = True #my_direction = RIGHT
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: moving_left = False #my_direction = LEFT
            if event.key == pygame.K_RIGHT: moving_right = False #my_direction = RIGHT

        if player_Location.x < 0:
            player_Location.x = 0
        if player_Location.x + player.get_width() > width:
            player_Location.x = width - player.get_width()

        pygame.display.updte()
        clock.tick(FPS)
    
pygame.quit()