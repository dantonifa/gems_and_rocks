# CSE 210 greed_for_gems game. Author: David Antonio Fajardo
"""Overview
Greed is a game in which the player seeks to gather as many 
falling gems as possible. 
The game continues as long as the player wants more!

Rules (Algorithm:)
Greed is played according to the following rules.



1. Gems  and rocks  randomly appear and fall from the top of the screen.
2. The player can move left or right along the bottom of the screen.
3. If the player touches a gem they earn a point.
4. If the player touches a rock they lose a point.

5. Gems and rocks are removed when the player touches them.
6. The game continues until the player closes the window."""

import pygame
from pygame.locals import K_LEFT, K_RIGHT   
import random

pygame.init()
"COLORS"
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)
"SETTINGS"
width = 800
height = 600 
size = (width, height)
screen = pygame.display.set_mode((size))
pygame.display.set_caption("Gems and Rocks")
screen.fill(BLACK)
SQUARE_SIZE = 32
FPS = 60 #Frames per second
Frames_per_sec = pygame.time.Clock()

"SCORE"

score = int(0)

#Game classes

class Rocks (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rock.png")
        self.size = (25, 25)
        self.surf = pygame.Surface ((25, 25))
        # Scale the image to your needed size
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.surf.get_rect(center = (random.randint(40, 760), 0))
    
    def move(self):
        self.rect.move_ip(0, 6)
        if (self.rect.bottom > 600):
            self.rect.center = (random.randint(30, 760), 0)
    
    def draw(self, surface ):
        pygame.Surface.blit(surface, self.image, self.rect)                       
    
class Diamonds (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("diamond.png")
        self.size = (25, 25)
        self.surf = pygame.Surface ((25, 25))
        # Scale the image to your needed size
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.surf.get_rect(center = (random.randint(40, 760), 0))
    
    def move(self):
        self.rect.move_ip(0, 5)
        if (self.rect.bottom > 600):
            self.rect.center = (random.randint(30, 760), 0)
    
    def draw(self, surface ):
        pygame.Surface.blit(surface, self.image, self.rect)  
        
class Rubies (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rubies.png")
        self.size = (25, 25)
        self.surf = pygame.Surface ((25, 25))
        # Scale the image to your needed size
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.surf.get_rect(center = (random.randint(40, 760), 0))
    
    def move(self):
        self.rect.move_ip(0, 4)
        if (self.rect.bottom > 600):
            self.rect.center = (random.randint(30, 760), 0)
    
    def draw(self, surface ):
        pygame.Surface.blit(surface, self.image, self.rect)  



class Catcher(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect(center = (400, 584))
        
    def draw (self, surface):
       pygame.Surface.blit(surface, self.image, self.rect )
    
    def update(self):
        
        global score
        
        pressed_key = pygame.key.get_pressed()
        
        if self.rect.left > 0:
            if pressed_key [K_LEFT]: 
                self.rect.move_ip (-5, 0)
                
        if self.rect.right < width:
            if pressed_key [K_RIGHT]: 
                self.rect.move_ip (5, 0)
                                
        if pygame.sprite.spritecollide(self, rocks_sprites, False):
            score += -1
            
        if pygame.sprite.spritecollide(self, diamonds_sprites, False ):
            score += 1
            
        if pygame.sprite.spritecollide(self, rubies_sprites, False):
            score += 1
            
    
        
#Game Score-display function

def score_display(message, color, font_type, x, y):
    """Displays the score on top-left of the screen"""
        
    font_type = pygame.font.SysFont('Comic Sans MS', 32)
    
    text = font_type.render(message, True, color)
    
    text_rec = text.get_rect()
    
    text_rec.topleft = (10, 10)
    
    screen.blit(text, text_rec)
        
       
     
C = Catcher()        
R = Rocks()
D = Diamonds()
Ru = Rubies() 
catcher_sprites = pygame.sprite.Group()
catcher_sprites.add(C)
rocks_sprites = pygame.sprite.Group()        
rocks_sprites.add(R)
diamonds_sprites = pygame.sprite.Group()
diamonds_sprites.add(D)
rubies_sprites = pygame.sprite.Group()
rubies_sprites.add(Ru)

while True:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    
    C.update()
    R.move()
    D.move()
    Ru.move()
    
    screen.fill(BLACK)
    
    C.draw(screen)
    R.draw(screen)
    D.draw(screen)
    Ru.draw(screen)
    
    score_display(f"Score: {score}", WHITE, ("Comic Sans MS", 32), 10, 10) 
    
    pygame.display.update()
    Frames_per_sec.tick(FPS)
        
    
      
    

    

   