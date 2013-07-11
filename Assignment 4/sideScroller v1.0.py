"""
Source File Name: sideScroller.py
Author's Name: Craig Bonin
Last Modified: 7/9/2013
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

"""
import pygame, random, time

#Starts game.
def startGame():
    background = pygame.image.load("background.png")
    return background.convert()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        
        
    def update (self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.rect.center = (50, mouseY)
        
class Baddie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        
    def randomPicture(self):
        
            

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
    allSprites = pygame.sprite.Group(player)
    
    
    #For initial Start
    flag = True
    
    while keepGoing:
        fps.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and flag:
                    background = startGame()
                    screen.blit(background, (0,0))
                    flag = False
                
        if flag == False:
            allSprites.clear(screen, background)
            allSprites.update()
            allSprites.draw(screen)
            
        
        pygame.display.flip()

if __name__ == "__main__": main()