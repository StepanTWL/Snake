import pygame
import sys
import random
from pygame.sprite import Group


class Apple():

    def __init__(self, screen):
        """inic apple"""

        self.screen = screen
        self.image = pygame.image.load('images/apple.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = int(random.uniform(0, 49)) * 16 + 8
        self.rect.centery = int(random.uniform(0, 39)) * 16 + 8
        self.newdata = False

    def output(self):
        """draw"""
        self.screen.blit(self.image, self.rect)

    def update_apple(self):
        """"""
        if (self.newdata):
            self.rect.centerx = int(random.uniform(0, 49)) * 16 + 8
            self.rect.centery = int(random.uniform(0, 39)) * 16 + 8



class Snake(pygame.sprite.Sprite):

    def __init__(self, screen):
        """inic snake"""
        super(Snake, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/snake_cell.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx + 8
        self.rect.centery = self.screen_rect.centery + 8
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False
        self.count_right = 0
        self.count_left = 0
        self.count_up = 0
        self.count_down = 0

    def output(self):
        """draw"""
        self.screen.blit(self.image, self.rect)

    def update_snake(self):
        """"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.count_right += 1
            self.count_left = 0
            self.count_up = 0
            self.count_down = 0
            if self.count_right == 160:
                self.centerx += 16
                self.count_right = 0
        elif self.mleft and self.rect.left > 0:
            self.count_right = 0
            self.count_left += 1
            self.count_up = 0
            self.count_down = 0
            if self.count_left == 160:
                self.centerx -= 16
                self.count_left = 0
        elif self.mup and self.rect.top > 0:
            self.count_right = 0
            self.count_left = 0
            self.count_up += 1
            self.count_down = 0
            if self.count_up == 160:
                self.centery -= 16
                self.count_up = 0
        elif self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.count_right = 0
            self.count_left = 0
            self.count_up = 0
            self.count_down += 1
            if self.count_down == 160:
                self.centery += 16
                self.count_down = 0

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def add_new_cell(self):        



pygame.init()
screen = pygame.display.set_mode((800, 640))
pygame.display.set_caption("Snape")
cells = Group()

bg_color = (0, 0, 0)
snake = Snake(screen)
apple = Apple(screen)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and snake.mup == False:
                snake.mdown = True
                snake.mup = False
                snake.mleft = False
                snake.mright = False
            if event.key == pygame.K_UP and snake.mdown == False:
                snake.mdown = False
                snake.mup = True
                snake.mleft = False
                snake.mright = False
            if event.key == pygame.K_LEFT and snake.mright == False:
                snake.mdown = False
                snake.mup = False
                snake.mleft = True
                snake.mright = False
            if event.key == pygame.K_RIGHT and snake.mleft == False:
                snake.mdown = False
                snake.mup = False
                snake.mleft = False
                snake.mright = True

    if (pygame.sprite.groupcollide(snake, apple, True, False))

    screen.fill(bg_color)
    snake.update_snake()
    snake.output()
    apple.output()
    snake.new_snake_cell(snake, apple)
    if (apple.newdata): 
        apple.update_apple()
        apple.newdata = False
    pygame.display.flip()

