import pygame
import sys
import random


class Apple():

    def __init__(self, screen):
        """inic apple"""

        self.screen = screen
        self.image = pygame.image.load('images/apple.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.newdata = False

    def output(self):
        """draw"""
        self.rect.centerx = random.uniform(8, 792)
        self.rect.centery = random.uniform(8, 592)
        self.screen.blit(self.image, self.rect)

    def update_apple(self):
        """"""
        if (self.newdata == False)


class Snake():

    def __init__(self, screen):
        """inic snake"""

        self.screen = screen
        self.image = pygame.image.load('images/snake_cell.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def output(self):
        """draw"""
        self.screen.blit(self.image, self.rect)

    def update_snake(self):
        """"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.centerx += 0.1
        elif self.mleft and self.rect.left > 0:
            self.centerx -= 0.1
        elif self.mup and self.rect.top > 0:
            self.centery -= 0.1
        elif self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.centery += 0.1

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        



pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snape")

bg_color = (0, 0, 0)
snake = Snake(screen)
apple = Apple(screen)
apple.output()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.mdown = True
                snake.mup = False
                snake.mleft = False
                snake.mright = False
            if event.key == pygame.K_UP:
                snake.mdown = False
                snake.mup = True
                snake.mleft = False
                snake.mright = False
            if event.key == pygame.K_LEFT:
                snake.mdown = False
                snake.mup = False
                snake.mleft = True
                snake.mright = False
            if event.key == pygame.K_RIGHT:
                snake.mdown = False
                snake.mup = False
                snake.mleft = False
                snake.mright = True

    screen.fill(bg_color)
    snake.update_snake()
    snake.output()
    if (apple.newdata != True): 
        apple.output()
        apple.newdata = True
    pygame.display.flip()

