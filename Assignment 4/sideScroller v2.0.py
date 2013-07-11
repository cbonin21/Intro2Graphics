"""
Source File Name: sideScroller.py
Author's Name: Craig Bonin
Last Modified: 7/11/2013
Last Modified By: Craig Bonin
*************************************
Program Description-
This is a side Scrolling Game.

*****************************************
Version History
*****************************************
v0.1
- Created Start Page
- 
*****************************************
v0.2
- Added Sprites for Player and Baddies
*****************************************

"""
import pygame, random, time

#Determines what baddie will show up
def randomBaddie(self):
        number = random.randint(1,3)
        if number == 1:
            return "baddie1.png"
        elif number ==2 :
            return "baddie2.png"
        else:
            return "baddie3.png"
#Player Class
class Player(pygame.sprite.Sprite):
    #Creating Sprite Object
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        
    #Updating Sprite Object    
    def update (self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.rect.center = (50, mouseY)
        
#Baddie Class        
class Baddie(pygame.sprite.Sprite):
    
    #Creating Baddie Sprite Object
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image = randomBaddie()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.reset()
        self.dx = random.randint(5,10)
    
    #Updates sprite
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right == 0:
            self.reset()
            
    #Resets sprite to the beginning of the screen
    def reset(self):
        self.rect.left = 0
        self.rect.centery = random.randint(0, 500)
        
def main():
    #Setting frame rate and gameloop
    keepGoing = True
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Fishy Fishy")
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
    player = Player()
    playerSprite = pygame.sprite.Group(player)
    
    
    #For initial Start
    flag = True
    counter = 0
    
    while keepGoing:
        fps.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and flag:
                    
                    flag = False
        
        if counter == 0:
            number = random.randint(1, 5)
            while number >= 0:
                baddie = Baddie()
                baddieSprites = pygame.sprite.Group(baddie)
        
        if flag == False:
            baddieSprites.clear(screen, background)
            baddieSprites.update()
            baddieSprites.draw(screen)
            playerSprite.clear(screen, background)
            playerSprite.update()
            playerSprite.draw(screen)
            counter += 1
            
        pygame.display.flip()

if __name__ == "__main__": main()