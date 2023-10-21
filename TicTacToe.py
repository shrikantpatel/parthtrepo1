import pygame
from pygame.locals import *
pygame.init()
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
#title of the window
pygame.display.set_caption('TicTacToe')

#we will define all the variable here
line_width = 6
markers = []
clicked = False
pos = []
player = 1

#define coulours
green = (0, 255, 0)
red = (255, 0, 0)

#draw the grid
def draw_grid():
   #background color of the grid
   bg = (255, 255, 200)
   #grid color
   grid = (50, 50, 50)
   screen.fill(bg)
   for x in range(1,3):
      pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), line_width)
      pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), line_width)

for x in range(3):
   row = [0] * 3
   markers.append(row)

  
def draw_markers():
   x_pos = 0
   #will pull out each row of the list
   for x in markers:
      y_pos = 0
      for y in x:
         #if in that cell the marker belongs to player one...
         if y== 1:
            #then draw player ones icon
            pygame.draw.line(screen, green, (x_pos * 100 + 15 , y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
            pygame.draw.line(screen, green, (x_pos * 100 + 15 , y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
         #if y = -1 than is player two:
         if y == -1:
            pygame.draw.circle(screen, red,(x_pos * 100 + 50 , y_pos * 100 + 50), 38 , line_width)
         #for each iteration of y I want to increase the y position by one to move along to the next coordinate
         y_pos += 1
      #one were moved on from the y I want to move on to the x postion
      x_pos += 1
      
            

#this while loop will run the game and look for interaction from the user
run = True
#if we run this game it will keep running it
while run:
   
   draw_grid()
   draw_markers()
   
   for event in pygame.event.get():
      #this will allow us to stop the game when the window quits
      if event.type == pygame.QUIT:
         run = False
      #this will run a click cycle and take it as an input
      if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
         #when we click the mouse the variable clicked will become true
         clicked = True
      if event.type == pygame.MOUSEBUTTONUP and clicked == True:  
         #when we let go of the mouse button then the variable will become false again
         clicked = False
         #now we have to take the position of where the mouse was when if was clicked
         pos = pygame.mouse.get_pos()
         #now we need to extract the positions of x and y
         cell_x = pos[0]
         cell_y = pos[1]
         #now we need to see in which square the mouse is in 
         #our window size is 300 by 300 so if we divide by 100 than we can get the postion of the square
         #// allows us to do floor division which will give us a round number
         # EX. If we divide 5 by 2 using integer division, the result would be 2.
         if markers[cell_x // 100][cell_y //100] == 0:
            markers[cell_x // 100][cell_y //100] = player
            player *= -1
         
         
   #will update the code if any addition are made (images, etc)   
   pygame.display.update()
   
   
pygame.quit

