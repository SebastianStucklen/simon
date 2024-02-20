import pygame

font = pygame.font.Font('freesansbold.ttf', 32)

def displayScore(screen,score):
    text = font.render(str(score),True,(255,255,255))
    screen.blit(text,(400,50))