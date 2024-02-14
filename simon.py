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

		self.lose = False
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
		self.ticker = 0

		self.time = mixer.Sound.get_length(self.yellowSound)

		
	def update(self):
		#self.click()
		self.draw()
		self.runPattern()
		self.playerTurn()

	def draw(self):
		#score = pygame.text
		#self.screen.blit()
		self.drawRed()
		self.drawBlue()
		self.drawYellow()
		self.drawGreen()

	
	def drawRed(self):
		'''if color has been clicked, draw lighter color and start a timer'''
		'''once timer is out, return to normal color'''
		if self.red:
			pygame.draw.rect(self.screen , (255, 200, 200), (self.redRect))#, math.pi / 2, math.pi, 100)
			if mixer.Sound.get_num_channels(self.redSound)==0: #only plays a sound once
				mixer.Sound.play(self.redSound)
			else:
				self.red = False
		elif self.red == False: 	
			pygame.draw.rect(self.screen , (232, 63, 111), (self.redRect))#, math.pi / 2, math.pi, 100)
			self.red = False
	
	def drawBlue(self):
		
		if self.blue:
			pygame.draw.rect(self.screen , (200, 200, 255), (self.blueRect))#, math.pi*2, math.pi / 2, 100)
			if mixer.Sound.get_num_channels(self.blueSound)==0: #only plays a sound once
				mixer.Sound.play(self.blueSound)
			else:
				self.blue = False
		elif self.blue == False:
			pygame.draw.rect(self.screen , (34, 116, 165), (self.blueRect))#, math.pi*2, math.pi / 2, 100)
			self.blue = False
			
	def drawYellow(self):
		
		if self.yellow:
			pygame.draw.rect(self.screen , (255, 255, 200), (self.yellowRect))#, math.pi/2, math.pi, 100)
			if mixer.Sound.get_num_channels(self.yellowSound)==0: #only plays a sound once
				mixer.Sound.play(self.yellowSound)
			else:
				self.yellow = False
		elif self.yellow == False:
			pygame.draw.rect(self.screen , (255, 191, 0), (self.yellowRect))#, math.pi/2, math.pi, 100)
			self.yellow = False

	def drawGreen(self):
		
		if self.green:
			pygame.draw.rect(self.screen , (200, 255, 200), (self.greenRect))#, math.pi, (3 * math.pi / 2), 100)
			if mixer.Sound.get_num_channels(self.greenSound)==0: #only plays a sound once
				mixer.Sound.play(self.greenSound)
			else:	
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
			
	
	def createPattern(self,new: bool):
		'''generates a pattern'''
		if new:
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
		else:
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
	
	def runPattern(self):
		'''Runs the pattern '''
		if self.computerTurn:
			for O in range(self.patternLength):
				if self.pattern[O] == 'red':
					self.red = True#
					self.blue = False
					self.yellow = False
					self.green = False
				if self.pattern[O] == 'blue':
					self.red = False
					self.blue = True#
					self.yellow = False
					self.green = False
				if self.pattern[O] == 'yellow':
					self.red = False
					self.blue = False
					self.yellow = True#
					self.green = False
				if self.pattern[O] == 'green':
					self.red = False
					self.blue = False
					self.yellow = False
					self.green = True#
				self.draw()
				pygame.display.flip()
				pygame.time.wait(1019)
			self.computerTurn = False
			pygame.mixer.stop()

	def playerTurn(self):
		if self.computerTurn == False:
			if len(self.playerPattern) < self.patternLength:
				self.ticker+=1
				self.click()
				self.draw()
				if self.ticker == 240:
					self.lose = True
				if self.clicked != 'nothing':
					self.playerPattern.append(self.clicked)
					self.ticker = 0
					if self.clicked == 'red':
						self.red = True#
						self.blue = False
						self.yellow = False
						self.green = False
					if self.clicked == 'blue':
						self.red = False
						self.blue = True#
						self.yellow = False
						self.green = False
					if self.clicked == 'yellow':
						self.red = False
						self.blue = False
						self.yellow = True#
						self.green = False
					if self.clicked == 'green':
						self.red = False
						self.blue = False
						self.yellow = False
						self.green = True
					self.draw()
					pygame.display.flip()
					self.clicked = 'nothing'
					if pygame.mouse.get_pressed()[0]:
						pygame.time.wait(1019)
						pygame.mixer.stop()
			else:
				if self.playerPattern == self.pattern:
					self.computerTurn = True
					self.patternLength+=1
					self.playerPattern.clear()
					self.createPattern(False)
					self.clicked = 'nothing'
					pygame.time.wait(500)
				else:
					self.lose = True

			
