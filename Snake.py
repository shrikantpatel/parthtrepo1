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
#1 is up, 2 will be right, 3 is down, and 4 is left
direction = 1 #1 is up, 2 will be right, 3 is down, and 4 is left
update_snake = 0

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
        # we want to see if theere is a keypress and we will be using the arrow key
        elif event.type == pygame.KEYDOWN:
            # we add the "and direction != 30" to the code because we want to make sure that if the snake is going up it cannot go down and go through itself
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            if event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
            if event.key == pygame.K_DOWN and direction != 1:
                direction = 3
            if event.key == pygame.K_LEFT and direction != 2:
                direction = 4
                
                
                
    # update snake starts wiht a value of 0 so  it does not meet 99 so it keeps on running until it reaches 99            
    if update_snake > 99:
        update_snake = 0    
        # so for each segment of the snake we are moving it by one in the list to make it look like it is moving
        #EX. moving segment 3 into the place of segment 2 and segment 4 into the place of segment 3
        snake_pos = snake_pos[-1:] + snake_pos[:-1]
        #going upward
        if direction == 1:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] - cell_size
        if direction == 3:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] + cell_size
        if direction == 2:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] + cell_size
        if direction == 4:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] - cell_size
    
    
    
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
    
    update_snake += 1
    
#stop pygame
pygame.quit()