from pickle import FALSE
import pygame
import sys

class Snake():

    def __init__(self, screen):
        """inic snake"""

        self.screen = screen
        self.image = pygame.image.load('images/snake_cell.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def output(self):
        """draw"""
        self.screen.blit(self.image, self.rect)

    def update_snake(self):
        """"""
        if self.mright:
            self.rect.centerx += 1
        elif self.mleft:
            self.rect.centerx -= 1
        elif self.mup:
            self.rect.centery -= 1
        elif self.mdown:
            self.rect.centery += 1



pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snape")

bg_color = (0, 0, 0)
snake = Snake(screen)

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
    pygame.display.flip()



