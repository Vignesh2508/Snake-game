import pygame
import random

pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

WIDTH = 800
HEIGHT = 600

FPS = 30

win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Snake")

gameMode = False
xpos = WIDTH/2
ypos = HEIGHT/2

x_change = 0
y_change = 0

score = 0

apple_xpos = 100
apple_ypos = 100

snake_list=[]
snake_length = 1 

clock = pygame.time.Clock()

font = pygame.font.SysFont('comicsans', 20, True)

#pygame.draw.rect(win, red, (100,100,10,10))

def collision_det(XnY):
	if (XnY[0] <= apple_xpos + 10) and (XnY[0] + 10 >= apple_xpos):
		if (XnY[1] <= apple_ypos + 10) and (XnY[1] + 10 >= apple_ypos):
			return True

def snake_growth():
    if len(snake_list) > snake_length:
        del snake_list[0]
    for XnY in snake_list:
        win.fill(black, rect=[XnY[0], XnY[1], 10, 10])

def apples_growth(apple_xpos, apple_ypos):
	pygame.draw.rect(win, red, (apple_xpos,apple_ypos,10,10))

while not gameMode:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameMode = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -5
				y_change = 0
			if event.key == pygame.K_RIGHT:
				x_change = 5
				y_change = 0
			if event.key == pygame.K_UP:
				y_change = -5
				x_change = 0
			if event.key == pygame.K_DOWN:
				y_change = 5
				x_change = 0

	xpos = xpos + x_change
	ypos = ypos + y_change
	
	win.fill(white)
	
	# Snake growth list and functions

	apples_growth(apple_xpos, apple_ypos)

	snake_XnY_cord = []
	snake_XnY_cord.append(xpos)
	snake_XnY_cord.append(ypos)
	snake_list.append(snake_XnY_cord)
	
	snake_growth()

	collision = collision_det(snake_list[-1])

	if collision == True:
		snake_length += 1
		apple_xpos = random.randint(0,WIDTH-10)
		apple_ypos = random.randint(0,HEIGHT-10)

	clock.tick(FPS)
	pygame.display.update()