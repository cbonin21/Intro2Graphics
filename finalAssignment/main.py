"""
Source File Name: main.py
Author's Name: Craig Bonin
Last Modified: 7/28/2013
Last Modified By: Craig Bonin
*************************************
Program Description-
This is a side Scrolling Game.

*****************************************
Version History
*****************************************
v0.1
- Created Start Page
*****************************************

"""

import pygame, random

class Player(pygame.sprite.Sprite):
    #Creating Sprite Object
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        
    #Updating Sprite Object    
    def update (self):
        self.rect.center = 
        
        
#Baddie Class        
class Baddie(pygame.sprite.Sprite):
    
    #Creating Baddie Sprite Object
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image = self.randomBaddie()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.reset()
        self.dx = random.randint(5,10)
        
    #Determines what baddie will show up
    def randomBaddie(self):
        number = random.randint(1,3)
        if number == 1:
            return "car1.png"
        elif number ==2 :
            return "car2.png"
        else:
            return "car3.png"
def main():
    
    #Setting frame rate and gameloop
    keepGoing = True
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Craig's Cab Adventure")
    background = pygame.image.load("startScreen.png")
    background = background.convert()
    
    #Setting up Pygame
    pygame.init()
    pygame.mixer.init()
    
    #Background Music
    sound = pygame.mixer.Sound("backgroundMusic.wav")
    sound.play(-1, 0, 0)
    
    #Setting up sprites and background
    screen.blit(background, (0,0))
    playerSprite = Player()
    
    #For initial Start
    flag = True
    counter = 0
    
    #Game Loop
    while keepGoing:
        fps.tick(30)
        #Pygame event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and flag:
                    background = pygame.image.load("highway.png")
                    screen.blit(background, (0,0))

