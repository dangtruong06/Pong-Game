import pygame, sys, random
from pygame.math import Vector2

pygame.init()
height = 600
width = 1000
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
pygame.display.set_caption('Pong')

#images
background = pygame.image.load('pongback.png').convert_alpha()

class MAIN():
    def __init__(self):
        hello = 3

    def display_background(self):
        screen.blit(background, (0,0))

    def update(self):
        self.display_background()
        player.draw_player()
        bot.draw_bot()
        bot.move_bot()
        pong.move_pong()
        pong.bounce()
        pong.collision()
        
class BOT():
    def __init__(self):

        self.red = pygame.image.load('red.png').convert_alpha()
        self.red_rect = self.red.get_rect(center = (player.x_pos, player.y_pos))
        self.speed = 4

    def draw_bot(self):
        screen.blit(self.red, self.red_rect)
    
    def move_bot(self):
        if self.red_rect.top > pong.pong_rect.top:
            self.red_rect.centery -= self.speed
        elif self.red_rect.bottom < pong.pong_rect.bottom:
            self.red_rect.centery += self.speed

class PlAYER():
    def __init__(self):
        self.x_pos = 100 
        self.y_pos = 300

        self.blue = pygame.image.load('blue.png').convert_alpha()

        self.blue_rect = self.blue.get_rect(center = (self.x_pos +800, self.y_pos))

    def draw_player(self):
        screen.blit(self.blue, self.blue_rect)

class PONG():
    def __init__(self):
        self.x_pos = 505
        self.y_pos = random.randint(100,500)
        
        self.x_speed = 8
        self.y_speed = 3

        self.v_direction = ['up', 'down']
        self.vertical = random.choice(self.v_direction)

        self.h_direction = ['left', 'right']
        self.horizontal = random.choice(self.h_direction)

        self.pong = pygame.image.load('pong.png').convert_alpha()
        self.pong_rect = self.pong.get_rect(center = (self.x_pos, self.y_pos))
    
    def move_pong(self):
        if self.vertical == 'up' and self.horizontal == 'right':
           self.pong_rect.x += self.x_speed
           self.pong_rect.y -= self.y_speed

        elif self.vertical == 'up' and self.horizontal == 'left':
           self.pong_rect.x -= self.x_speed
           self.pong_rect.y -= self.y_speed

        elif self.vertical == 'down' and self.horizontal == 'right':
           self.pong_rect.x += self.x_speed
           self.pong_rect.y += self.y_speed
        
        elif self.vertical == 'down' and self.horizontal == 'left':
           self.pong_rect.x -= self.x_speed
           self.pong_rect.y += self.y_speed

        screen.blit(self.pong,self.pong_rect)

    def bounce(self):
        if self.pong_rect.top <= 0 or self.pong_rect.bottom >= height:
            self.y_speed = -self.y_speed
        elif self.pong_rect.right <= 0 or self.pong_rect.left >= width:
            sys.quit()

    def collision(self):
        if pygame.Rect.colliderect(self.pong_rect, bot.red_rect):
            self.x_speed = -self.x_speed
        elif pygame.Rect.colliderect(self.pong_rect, player.blue_rect):
            self.x_speed = -self.x_speed

        
#class objects
main = MAIN()
pong = PONG()
player = PlAYER()
bot = BOT()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        if player.blue_rect.top >= 0:
            player.blue_rect.y -= 3
    if keys[pygame.K_DOWN]:
        if player.blue_rect.bottom <= height:
            player.blue_rect.y += 3

    main.update()
    
    pygame.display.update()
    clock.tick(60)