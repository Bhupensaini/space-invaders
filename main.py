import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800 ,600))


# background
background = pygame.image.load("background.png")



# title and content
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)


# players
playerImg = pygame.image.load("spacecraft.png")
playerx = 350
playery = 480
playerx_change = 0


# enemy
enemyImg = pygame.image.load("alien.png")
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyx_change = 4
enemyy_change = 40


# bullet
bulletImg = pygame.image.load("bullet.png")
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 7
bullet_state = "ready"



def player(x, y):
	screen.blit(playerImg,(x,y))

def enemy(a, b):
	screen.blit(enemyImg,(a,b))

def fire_bullet(x,y):
	global bullet_state
	bullet_state = "fire"
	screen.blit(bulletImg, (x + 16, y + 10))



# game loop
running = True
while running:

	screen.fill((0,0,0))

	screen.blit(background, (0,0))

	# playerx += 0.1
	# playery += -0.2

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				# print("Left arrow key is pressed")
				playerx_change = -5

			if event.key == pygame.K_RIGHT:
				# print("Right arrow key is pressed")
				playerx_change = 5

			if event.key == pygame.K_SPACE:
				bulletx = playerx
				fire_bullet(playerx,bullety)


		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				# print("key is released")
				playerx_change = 0
	

	# checking for boundaries for spaceship
	playerx += playerx_change


	if playerx < 0:
		playerx = 0
	elif playerx >=736:
		playerx = 736



	enemyX += enemyx_change


	if enemyX < 0:
		enemyx_change = 4
		enemyY += enemyy_change
	elif enemyX >=736:
		enemyx_change = -4
		enemyY += enemyy_change


	if bullety<= 0:
		bullety = 480
		bullet_state = "ready"


	if bullet_state is "fire":
		fire_bullet(bulletx,bullety)
		bullety -= bullety_change


	player(playerx,playery)
	enemy(enemyX,enemyY)
	pygame.display.update()