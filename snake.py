import pygame
import random

pygame.init()

screen_width = 600
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))
gameWindow.fill(pygame.Color("#ffffff"))
pygame.display.set_caption("Snake")
font = pygame.font.SysFont(None, 55)
#pygame.display.update()


def text_screen(text, color, x, y):
	screen_text = font.render(text, True, color)
	gameWindow.blit(screen_text, [x,y])


def snk(gameWindow, s_list, size):
	for x,y in s_list:
		pygame.draw.rect(gameWindow, pygame.Color("#c72014"), [x, y, size, size])

def gameloop():

	exit_game = False
	game_over = False
	xpos = 120
	ypos = 120
	size = 15
	fps = 30
	vel_x = 0
	vel_y = 0
	score = 0
	food_x = random.randint(0, (screen_width-8))
	food_y = random.randint(0, (screen_height-8))
	pygame.draw.rect(gameWindow, pygame.Color("#000000"), [food_x, food_y, 15, 15])
	clock = pygame.time.Clock()#to update the frame of the game
	s_len = 1
	s_list = []

	while not exit_game:

		# Checking for Game Over Condition
		if game_over == True:
			gameWindow.fill(pygame.Color("#ffffff"))
			text_screen("GAME OVER :(", pygame.Color("#ff0000"), screen_width/2-140, screen_height/2-30)
			text_screen("Press Enter to Continue", pygame.Color("#ff0000"), screen_width/2-200, screen_height/2+30)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						game_over = False
						gameloop()

		else:
			# Moving the Snake
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						vel_x = 10
						vel_y = 0
					if event.key == pygame.K_LEFT:
						vel_x = -10
						vel_y = 0
					if event.key == pygame.K_UP:
						vel_y = -10
						vel_x = 0
					if event.key == pygame.K_DOWN:
						vel_y = 10
						vel_x = 0
			# Eating Food
			if abs(xpos-food_x)<14 and abs(ypos-food_y)<14:
				score+=1
				s_len+=1
				food_x = random.randint(0, (screen_width-8))
				food_y = random.randint(0, (screen_height-8))

			# Updating th Coordinates
			xpos += vel_x
			ypos += vel_y

			# Snake Length and new size
			head = []
			head.append(xpos)
			head.append(ypos)
			s_list.append(head)
			if len(s_list)>s_len:
				del s_list[0]

			# Collison Conditions
			if (xpos >= 595 or xpos <= 5) or (ypos >= 595 or ypos <= 5):
				game_over = True
			if head in s_list[:-1]:
				game_over = True

			# The Game Canvas
			gameWindow.fill(pygame.Color("#ffffff"))
			snk(gameWindow, s_list, size)
			pygame.draw.rect(gameWindow, pygame.Color("#000000"), [food_x, food_y, size, size])
			text_screen("Score: " + str(score), pygame.Color("#000000"), 5, 5)
			pygame.display.update()
			clock.tick(fps)

	pygame.quit()
	quit()

gameloop()