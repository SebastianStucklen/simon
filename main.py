import pygame
import random
import math
from pygame import mixer

pygame.init()
mixer.init()

pygame.display.set_caption("simo")
screen = pygame.display.set_mode((800,800))
from simon import Simon
simon = Simon(screen)

from score import displayScore

ticker = 0
running = True
clock = pygame.time.Clock()

haha = pygame.mixer.Sound("resources/haha.mp3")
loser = pygame.image.load("resources/lose.png")


simon.createPattern(True)
while running:
	screen.fill((0,0,0))
	displayScore(screen,simon.patternLength-4)
	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	if simon.lose:
		haha.play()
		haha.play()
		haha.play()
		haha.play()
		screen.blit(loser, (0,0))
		pygame.display.flip()
		pygame.time.wait(1000)
		running = False
	simon.update()

	pygame.display.flip()