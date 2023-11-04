#import modules
import pygame
from pygame.locals import *

pygame.init()

# initialize all pygame modules 
screen_width = 600
screen_height = 600

#create the game window (Same as Tictactoe)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')


#define basic game variables
#for this program the screen will be divided into a grid with cells
# because we are dividing the cell_size into 10 there will be a total of 60 cells when going down or up and 60 cells when going left or right
cell_size = 10

#create the snake
#snake pos will hold the position of the snake
#we want to start in the middle so we divide screen width and height by 2
#we use int to get an integer instead of floats

snake_pos =[[int(screen_width / 2), int(screen_height/2)]]
# we use append to add it right behind the head of the snake above
#append allows us to keep on adding length to the snake as it eats more food
#we add cell size because we want the rectangle to be added underneath the first head of 10 units below which is our cell size
snake_pos.append([int(screen_width / 2), int(screen_height/2) + cell_size])
snake_pos.append([int(screen_width / 2), int(screen_height/2) + cell_size * 2])
snake_pos.append([int(screen_width / 2), int(screen_height/2) + cell_size * 3])


#colors
bg = (255, 200, 150)
red = (255, 0, 0)
body_inner = (50, 175, 25)
body_outer = (100, 100, 200)

def draw_screen():
    bg = (255, 200, 150)
    screen.fill(bg)

#create the loop with exit event handler (Same as tictactoe)
# will keep on running game until a false condition(event handler) is given
run = True
while run:
    
    draw_screen()
    
    # go through the events
    for event in pygame.event.get():
        # once the xit button is hit pygame.QUIT will set run to false and we will be out of the loop
        if event.type == pygame.QUIT:
            run = False
    
    #draw snake
    # we want the head to be a different color to show which direction it is going in
    head = 1
    for x in snake_pos:
        #if it is not the head use the normal snake colors
        if head == 0:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, body_inner, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))
        # if it is the head then use red
        if head == 1:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, red, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))
            head = 0
            
    
    #update the screen
    pygame.display.update()
    
#stop pygame
pygame.quit()