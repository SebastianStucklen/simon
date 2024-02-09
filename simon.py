import pygame
import random
import math
from pygame import mixer
import time

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
		self.patternLength = 4
		self.computerTurn = True
		self.clicked = 'nothing'
		
		self.red = False
		self.blue = False
		self.yellow = False
		self.green = False

		self.defRect = pygame.Rect(200,200,400,400)

		self.redRect = pygame.Rect(200,200,200,200)
		self.blueRect = pygame.Rect(400,200,200,200)
		self.yellowRect = pygame.Rect(400,400,200,200)
		self.greenRect = pygame.Rect(200,400,200,200)
		
		self.activTicker = [0,0,0,0]
		self.patternTick = 0

		self.time = mixer.Sound.get_length(self.yellowSound)

		
	def update(self):
		self.click()
		self.draw()
		#self.runPattern()

	def draw(self):
		self.drawRed()
		self.drawBlue()
		self.drawYellow()
		self.drawGreen()


	def lose(self):
		if False:
			self.pattern.clear
			self.playerPattern.clear
			return True
	
	def drawRed(self):
		'''if color has been clicked, draw lighter color and start a timer'''
		'''once timer is out, return to normal color'''
		if self.red:
			pygame.draw.rect(self.screen , (255, 200, 200), (self.redRect))#, math.pi / 2, math.pi, 100)
			if mixer.Sound.get_num_channels(self.redSound)==0: #only plays a sound once
					mixer.Sound.play(self.redSound)
					self.red = False

		elif self.red == False:
			pygame.draw.rect(self.screen , (232, 63, 111), (self.redRect))#, math.pi / 2, math.pi, 100)
			self.red = False
	
	def drawBlue(self):
		
		if self.blue:
			pygame.draw.rect(self.screen , (200, 200, 255), (self.blueRect))#, math.pi*2, math.pi / 2, 100)
			if mixer.Sound.get_num_channels(self.blueSound)==0: #only plays a sound once
					mixer.Sound.play(self.blueSound)
					self.blue = False

		elif self.blue == False:
			pygame.draw.rect(self.screen , (34, 116, 165), (self.blueRect))#, math.pi*2, math.pi / 2, 100)
			self.blue = False
			
	def drawYellow(self):
		
		if self.yellow:
			pygame.draw.rect(self.screen , (255, 255, 200), (self.yellowRect))#, math.pi/2, math.pi, 100)
			if mixer.Sound.get_num_channels(self.yellowSound)==0: #only plays a sound once
					mixer.Sound.play(self.yellowSound)
					self.yellow = False

		elif self.yellow == False:
			pygame.draw.rect(self.screen , (255, 191, 0), (self.yellowRect))#, math.pi/2, math.pi, 100)
			self.yellow = False

	def drawGreen(self):
		
		if self.green:
			pygame.draw.rect(self.screen , (200, 255, 200), (self.greenRect))#, math.pi, (3 * math.pi / 2), 100)
			if mixer.Sound.get_num_channels(self.greenSound)==0: #only plays a sound once
					mixer.Sound.play(self.greenSound)
					self.green = False
					
		elif self.green == False:
			pygame.draw.rect(self.screen , (50, 147, 111), (self.greenRect))#, math.pi, (3 * math.pi / 2), 100)
			self.green = False
	
	def click(self):
		'''checks if the mouse is touching a color, and then checks if the left mouse button is pressed'''

		mPos = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if self.redRect.collidepoint(mPos):
			if click[0]:
				self.red = True
				self.clicked = 'red'
		
		if self.blueRect.collidepoint(mPos):
			if click[0]:
				self.blue = True
				self.clicked = 'blue'

		if self.yellowRect.collidepoint(mPos):
			if click[0]:
				self.yellow = True
				self.clicked = 'yellow'

		if self.greenRect.collidepoint(mPos):
			if click[0]:
				self.green = True
				self.clicked = 'green'
			
	
	def createPattern(self):
		'''generates a pattern'''
		for i in range(self.patternLength):
			self.pattern.append(
				random.choice(
					[	
						'red',
						'blue',
						'yellow',
						'green'
					]
				)
			)
	
	def runPattern(self,i: int = 0):
		'''Runs the pattern '''
		if self.computerTurn:
			if not i > 0:
				i = 0
			for O in range(len(self.pattern)*4):
				if O % 4 == 0:
					if self.pattern[i] == 'red':
						self.red = True#
						self.blue = False
						self.yellow = False
						self.green = False

					if self.pattern[i] == 'blue':
						self.red = False
						self.blue = True#
						self.yellow = False
						self.green = False

					if self.pattern[i] == 'yellow':
						self.red = False
						self.blue = False
						self.yellow = True#
						self.green = False

					if self.pattern[i] == 'green':
						self.red = False
						self.blue = False
						self.yellow = False
						self.green = True#

					self.draw()
					pygame.display.flip()
					i+=1
					pygame.time.wait(1021)
			self.computerTurn = False

	def playerTurn(self):
		pass