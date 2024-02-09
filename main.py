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

simon.createPattern()
print(simon.pattern)
while running:
	clock.tick(60)
	if ticker == 60:
		ticker = 0
	ticker += 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	simon.runPattern()
	simon.update()
	pygame.display.flip()