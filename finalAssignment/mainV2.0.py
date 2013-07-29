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
v0.2
- Added in bad guys, background, player sprites.
- Added in music.

"""

import pygame, random

#Scoreboard sprite class
class Scoreboard(pygame.sprite.Sprite):
    #Creating the scoreboard sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.time = self.timeAmount
        self.font = pygame.font.SysFont("None", 50)
    
    #Updating scoreboard Class    
    def update(self):
        self.text = "Time:{} Score:{}" .format(self.time, self.score)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()
        
    def setTimeAmount(self, seconds):
        self.timeAmount = seconds

class Player(pygame.sprite.Sprite):
    #Creating Sprite Object
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
    
    def moveUp(self):
        print 'whats the problem'
        if self.getLocationY() = 242:
            self.setLocationY(102)
        elif self.getLocationY() = 394:
            self.setLocationY(232)
            
    def moveDown(self):
        if self.getLocationY() = 102:
            self.setLocationY(242)
        elif self.getLocationY() = 242:
            self.setLocationY(394)

    #Updating Sprite Object    
    def update (self):
        self.rect.center = (216, self.getLocationY())
    
    def setLocationY(self, y):
        self.yLocation = y
    
    def getLocationY(self):
        return self.yLocation

class Background(pygame.sprite.Sprite):
    
    def __init(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("highway.png")
        self.rect = self.image.get_rect()
        self.reset()
        self.dx = 5
        
    def update(self):
        
        if self.rect.right == 500
            self.reset()
        
    def reset(self):
        self.rect.left = 0
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
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
        
    #Determines what baddie will show up
    def randomBaddie(self):
        number = random.randint(1,3)
        if number == 1:
            return "car1.png"
        elif number ==2 :
            return "car2.png"
        else:
            return "car3.png"
        
    #Resets sprite and assigns it to a new random lane    
    def reset(self):
        self.rect.left = 500
        number = random.randint(1,3)
        if number ==1:
            self.rect.centery = 102
        elif number == 2:
            self.rect.centery = 242
        else:
            self.rect.centery = 394
            
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
    scoreboardSprite = Scoreboard()
    playerSprite = Player()
    backgroundSprite = Background()
    
    #For initial Start
    counter = 0
    gameState = 0
    
    #Game Loop
    while keepGoing:
        fps.tick(30)
        #Pygame event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and gameState == 0:
                    scoreboardSprite.time = 20
                    screen.blit(background, (0,0))
                    enemy1 = Baddie()
                    gameState = 1
                    spritesGroup = pygame.sprite.LayeredUpdates.add(backgroundSprite, enemy1, playerSprite, scoreboardSprite)
                if event.key == pygame.K_2 and gameState == 0:
                    scoreboardSprite.time = 40
                    enemy2 = Baddie()
                    enemy1 = Baddie()
                    gameState = 1
                    screen.blit(background, (0,0))
                    spritesGroup = pygame.sprite.LayeredUpdates.add(backgroundSprite, enemy1, enemy2, playerSprite, scoreboardSprite)
                if event.key == pygame.K_3 and gameState == 0:
                    scoreboardSprite.time = 60
                    enemy2 = Baddie()
                    enemy1 = Baddie()
                    enemy3 = Baddie()
                    spritesGroup = pygame.sprite.LayeredUpdates.add(backgroundSprite, enemy1, enemy2, enemy3, playerSprite, scoreboardSprite)
                    screen.blit(background, (0,0))
                    gameState = 1
                if event.key == pygame.K_UP and gameState == 1:
                    playerSprite.moveUp()
                if event.key == pygame.K_DOWN and gameState == 2:
                    playerSprite.moveDown()
        
        if gameState = 1:
            spritesGroup.clear(screen, background)
            spritesGroup.update()
            spritesGroup.draw(screen)
            
            if counter == 31:
                scoreboardSprite.time -= 1
                counter = 1
            
            if scoreboardSprite.time == 0
                gameState = 3

