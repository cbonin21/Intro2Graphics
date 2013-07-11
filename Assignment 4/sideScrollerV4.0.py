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
v0.3
-Added Background Sprite attempting to get it to scroll
-Added food
-Re-worked baddie and food system
*****************************************
v0.4
-Added in game ending sequences
-Updated some of the sprites and how they interact

"""
import pygame, random

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
        image = self.randomBaddie()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.reset()
        self.dx = random.randint(5,10)
    
    #Updates sprite moving it to the left of the screen.
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
    #Resets sprite to the beginning of the screen
    def reset(self):
        self.rect.left = 500
        self.rect.centery = random.randint(0, 700)
        
    #Determines what baddie will show up
    def randomBaddie(self):
        number = random.randint(1,3)
        if number == 1:
            return "baddie1.png"
        elif number ==2 :
            return "baddie2.png"
        else:
            return "baddie3.png"

#Food Class        
class Food(pygame.sprite.Sprite):
    
    #Creating Food Sprite Object
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image = self.randomFood()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.reset()
        self.dx = random.randint(5,10)
    
    #Updates sprite moving it to the left of the screen.
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
    #Resets sprite to the beginning of the screen
    def reset(self):
        self.rect.left = 500
        self.rect.centery = random.randint(0, 500)
        
    #Determines what food will show up
    def randomFood(self):
        number = random.randint(1,3)
        if number == 1:
            return "food1.png"
        elif number ==2 :
            return "food2.png"
        else:
            return "food3.png"
        
#Background Sprite Class
class Background(pygame.sprite.Sprite):
    
    #Creates background Sprite and decreases it's x value
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("background.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 5
        self.reset()
        self.update()
        
    #Updates background Sprite
    def update(self):
        self.rect.right -= self.dx
        if self.rect.right >= 500:
            self.reset()
            print "NOthing"
            
    #Resets background Sprite       
    def reset(self):
        self.rect.left = 0
        print "nothing"

#Scoreboard sprite class
class Scoreboard(pygame.sprite.Sprite):
    #Creating the scoreboard sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.time = 60
        self.font = pygame.font.SysFont("None", 50)
    
    #Updating scoreboard Class    
    def update(self):
        self.text = "Time:{} Score:{}" .format(self.time, self.score)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()   

#GameEnd Class
class GameEnd(pygame.sprite.Sprite):
    #Creating the gameend Sprite
    def __int__it(self):
        pygame.sprite.Sprite.__init__(self)
        self.message = ""
        self.font = pygame.font.SysFont("None", 10)
    
    #Updating based on outcome 
    def update(self):
        self.font = pygame.font.SysFont("None", 10)
        self.text = "{}" .format(self.message)
        self.image = self.font.render(self.text, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        
#Main Class
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
                    background = pygame.image.load("background.png")
                    screen.blit(background, (0,0))
                    food1 = Food()
                    food2 = Food()
                    food3 = Food()
                    baddie1 = Baddie()
                    baddie2 = Baddie()
                    baddie3 = Baddie()
                    baddie4 = Baddie()
                    baddie5 = Baddie()
                    baddie6 = Baddie()
                    baddieFoodSprites = pygame.sprite.Group(baddie1, baddie2, baddie3, baddie4, baddie5, baddie6, food1, food2, food3)
                    scoreboardSprite = Scoreboard()
                    scoreboard = pygame.sprite.Group(scoreboardSprite)
                    player = pygame.sprite.Group(playerSprite)
                    endGame = GameEnd()
                    endGameGroup = pygame.sprite.Group(endGame)
                    endGameGroup.clear(screen, background)
                    flag = False
        
        #If to check of sprites should be updated and checks collisions
        if flag == False:
            #Checking for collision with baddie
            if playerSprite.rect.colliderect(baddie1.rect) or playerSprite.rect.colliderect(baddie2.rect)or playerSprite.rect.colliderect(baddie3.rect)or playerSprite.rect.colliderect(baddie4.rect)or playerSprite.rect.colliderect(baddie5.rect)or playerSprite.rect.colliderect(baddie6.rect):
                flag = True
                endGame.message = "You've lost./n Your score was " + str(scoreboardSprite.score) + "\n Press Space to start again."
                player.remove()
                scoreboard.remove()
                baddieFoodSprites.remove()
                endGameGroup.clear(screen, background)
                endGameGroup.update()
                endGameGroup.draw(screen)
                
            #Checking for collision with food
            if playerSprite.rect.colliderect(food1.rect):
                scoreboardSprite.score += 10
                food1.reset()
            elif playerSprite.rect.colliderect(food2.rect):
                scoreboardSprite.score += 10
                food2.reset()
            elif playerSprite.rect.colliderect(food3.rect):
                scoreboardSprite.score += 10
                food3.reset()
            
            if counter == 31:
                scoreboardSprite.time -= 1
                counter = 1
            
            #Updating and clearing sprites
            baddieFoodSprites.clear(screen, background)
            baddieFoodSprites.update()
            baddieFoodSprites.draw(screen)
            player.clear(screen, background)
            player.update()
            player.draw(screen)
            scoreboard.clear(screen, background)
            scoreboard.update()
            scoreboard.draw(screen)
            counter += 1
            
            #Checking to see if time runs out
            if scoreboardSprite.time == 0:
                screen.blit(background, (0,0))
                flag = True
                endGame.message = "Congradulations you've won! \n With a score of " + str(scoreboardSprite.score) + "\n Press Space to start again."
                baddieFoodSprites.remove()
                player.remove()
                scoreboard.remove()
                endGameGroup.clear(screen, background)
                endGameGroup.update()
                endGameGroup.draw(screen)
                
        #updates screen.   
        pygame.display.flip()

if __name__ == "__main__": main()