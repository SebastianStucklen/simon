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
ticker = 0
running = True
clock = pygame.time.Clock()
while running:
	clock.tick(60)
	
	if ticker % 90 == 0:
		ticker = 0
		simon.red = False
		simon.blue = False
		simon.yellow = False
		simon.green = False
	ticker += 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	simon.update()
	pygame.display.flip()