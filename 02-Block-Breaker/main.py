import pygame

pygame.init()

screen_width = 480
screen_size = 600
mainWindow = pygame.display.set_mode((screen_width, screen_size))
mainWindow.fill(pygame.Color("#07434f"))
pygame.display.set_caption("Block-Breaker")
font = pygame.font.SysFont(None, 55)
pygame.display.update()


def create_blocks(mainWindow, blocks):
	for x,y in blocks:
		pygame.draw.rect(mainWindow, pygame.Color("#ffffff"), [x, y, 70, 10])

def text_screen(text, color, x, y):
	screen_text = font.render(text, True, color)
	mainWindow.blit(screen_text, [x,y])

def game():
	# Variables
	score = 0
	pad_x = screen_width/2-50
	pad_vel = 0
	ball_vel_x = +0.8
	ball_vel_y = -0.8
	ball_x = pad_x + 50
	ball_y = 567
	move_left = False
	move_right = False
	ball_move = False
	exit_game = False
	game_over = False

	# Initializing the Coordinates for blocks
	blocks = []
	x = 15
	y = 50
	for i in range(0,100):
		v = []
		v.append(x)
		v.append(y)
		blocks.append(v)
		if x+145 >= screen_width:
			x = 15
			y += 15
		else:
			x += 75

	# Game Loop
	while not exit_game:

		if game_over == True:
			mainWindow.fill(pygame.Color("#07434f"))
			text_screen("GAME OVER :(", pygame.Color("#ffffff"), screen_width/2-140, screen_size/2-30)
			text_screen("Press Enter to Continue", pygame.Color("#ffffff"), screen_width/2-200, screen_size/2+30)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						game_over = False
						game()

		else:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						move_right = True
					if event.key == pygame.K_LEFT:
						move_left = True
					if event.key == pygame.K_SPACE:
						ball_move = True

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_RIGHT:
						move_right = False
					if event.key == pygame.K_LEFT:
						move_left = False


			# Checking Border Conditions for Pad
			if pad_x <= 5:
				move_left = False
			if pad_x >= 375:
				move_right = False
			
			# Moveing the Pad
			if move_right == True:
				pad_x += 0.8
			if move_left == True:
				pad_x -= 0.8

			# Updating the Velocity of the Ball
			if ball_x <= 5:
				ball_vel_x = -(ball_vel_x)
			if ball_x >= 475:
				ball_vel_x = -(ball_vel_x)
			for x,y in blocks:
				if (x <= ball_x and ball_x <= x+70) and y+10 >= ball_y:
					blocks.remove([x,y])
					ball_vel_y = -(ball_vel_y)
					score += 10
					break

			# Ball and Pad Collison
			if ball_y+8 >= 580 and ball_x >= pad_x and ball_x <= pad_x+100:
				ball_vel_y = -ball_vel_y

			# Updating the Coordinates of the Ball
			if ball_move == True:
				ball_x += ball_vel_x
				ball_y += ball_vel_y
			else:
				ball_x = pad_x + 50
				ball_y = 567

			# Game Over Condition
			if ball_y >= 600:
				game_over = True

			# Updating the Screen
			mainWindow.fill(pygame.Color("#07434f"))
			create_blocks(mainWindow, blocks)
			text_screen("Score: " + str(score), pygame.Color("#ffffff"), 5, 5)
			pygame.draw.circle(mainWindow, pygame.Color("#ffffff"), (int(ball_x), int(ball_y)), 8)
			pygame.draw.rect(mainWindow, pygame.Color("#ffffff"), [pad_x, 580, 100, 10])
			pygame.display.update()
	
	pygame.quit()
	quit()		

game()