import pygame
import random
import math
from pygame import mixer

pygame.init()
mixer.init()
class Simon:
	def __init__(self,screen):
		self.screen = screen
		#sound
		self.redSound = mixer.Sound("resources/1red.wav")
		self.blueSound = mixer.Sound("resources/2blue.wav")
		self.yellowSound = mixer.Sound("resources/3yellow.wav")
		self.greenSound = mixer.Sound("resources/4green.wav")

		self.pattern = []
		self.playerPattern = []
		
		self.red = False
		self.blue = False
		self.yellow = False
		self.green = False

		self.defRect = pygame.Rect(200,200,400,400)

		self.redRect = pygame.Rect(200,200,200,200)
		self.blueRect = pygame.Rect(400,200,200,200)
		self.yellowRect = pygame.Rect(400,400,200,200)
		self.greenRect = pygame.Rect(200,400,200,200)
		
	def update(self):
		self.click()

		self.drawRed(self.red)
		self.drawBlue(self.blue)
		self.drawYellow(self.yellow)
		self.drawGreen(self.green)


	def lose(self):
		if False:
			self.pattern.clear
			self.playerPattern.clear
			return True
	
	def drawRed(self,activated: bool = False):

		if activated:
			pygame.draw.rect(self.screen , (255, 200, 200), (self.redRect))#, math.pi / 2, math.pi, 100)
		else:
			pygame.draw.rect(self.screen , (232, 63, 111), (self.redRect))#, math.pi / 2, math.pi, 100)
	
	def drawBlue(self,activated: bool = False):
		if activated:
			pygame.draw.rect(self.screen , (200, 200, 255), (self.blueRect))#, math.pi*2, math.pi / 2, 100)
		else:
			pygame.draw.rect(self.screen , (34, 116, 165), (self.blueRect))#, math.pi*2, math.pi / 2, 100)

	def drawYellow(self,activated: bool = False):
		if activated:
			pygame.draw.rect(self.screen , (255, 255, 200), (self.yellowRect))#, math.pi/2, math.pi, 100)
		else:
			pygame.draw.rect(self.screen , (255, 191, 0), (self.yellowRect))#, math.pi/2, math.pi, 100)

	def drawGreen(self,activated: bool = False):
		if activated:
			pygame.draw.rect(self.screen , (200, 255, 200), (self.greenRect))#, math.pi, (3 * math.pi / 2), 100)
		else:
			pygame.draw.rect(self.screen , (50, 147, 111), (self.greenRect))#, math.pi, (3 * math.pi / 2), 100)
	
	def click(self):
		mPos = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if self.redRect.collidepoint(mPos):
			if click[0]:
				if mixer.Sound.get_num_channels(self.redSound)==0:
					mixer.Sound.play(self.redSound)
				self.red = True
		
		if self.blueRect.collidepoint(mPos):
			if click[0]:
				if mixer.Sound.get_num_channels(self.blueSound)==0:
					mixer.Sound.play(self.blueSound)
				self.blue = True

		if self.yellowRect.collidepoint(mPos):
			if click[0]:
				if mixer.Sound.get_num_channels(self.yellowSound)==0:
					mixer.Sound.play(self.yellowSound)
				self.yellow = True

		if self.greenRect.collidepoint(mPos):
			if click[0]:
				if mixer.Sound.get_num_channels(self.greenSound)==0:
					mixer.Sound.play(self.greenSound)
				self.green = True
			
	
	def createPattern(self):
		pass
		
		