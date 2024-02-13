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

simon.createPattern(True)
while running:
	clock.tick(60)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	if simon.lose:
		running = False
	simon.update()

	pygame.display.flip()