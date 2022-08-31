import random
import sys
import pygame
pygame.init()#В этой программе для инициализации шрифта courier

SIZE_BLOCK = 20
HEADER_MARGIN = 70
MARGIN = 1
COUNT_BLOCKS = 20
FRAME_COLOR = (1, 255, 204)
HEADER_COLOR = (0, 204, 153)
SNAKE_COLOR = (0, 102, 0)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
RED = (224, 0, 0)
size = [SIZE_BLOCK*COUNT_BLOCKS+MARGIN*(COUNT_BLOCKS-1)+2*SIZE_BLOCK, 
        HEADER_MARGIN+SIZE_BLOCK*COUNT_BLOCKS+MARGIN*(COUNT_BLOCKS-1)+2*SIZE_BLOCK]

class SnakeBlock:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def is_inside(self) -> bool:
        return 0<=self.x<COUNT_BLOCKS and 0<=self.y<COUNT_BLOCKS
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SnakeBlock) and self.x == __o.x and self.y == __o.y

def get_random_empty_block() -> SnakeBlock:
    x = random.randint(0,COUNT_BLOCKS-1)
    y = random.randint(0,COUNT_BLOCKS-1)
    empty_block = SnakeBlock(x, y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0,COUNT_BLOCKS-1)
        empty_block.y = random.randint(0,COUNT_BLOCKS-1)
    return empty_block


def draw_block(color: tuple, row: int, column: int) -> None:
    pygame.draw.rect(screen, color, [SIZE_BLOCK+column*SIZE_BLOCK + MARGIN*(column+1), 
                                             HEADER_MARGIN+SIZE_BLOCK+row*SIZE_BLOCK + MARGIN*(row+1), 
                                             SIZE_BLOCK, 
                                             SIZE_BLOCK])

snake_blocks=[SnakeBlock(9,9)]
apple = get_random_empty_block()
d_row = buf_row = 0
d_col = buf_col = 1
total = 0
speed = 1
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
timer = pygame.time.Clock()#для задания количества кадров отрисовки
courier = pygame.font.SysFont('courier', 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col:
                buf_row = -1
                buf_col = 0
            elif event.key == pygame.K_DOWN and d_col:
                buf_row = 1
                buf_col = 0
            elif event.key == pygame.K_LEFT and d_row:
                buf_row = 0
                buf_col = -1
            elif event.key == pygame.K_RIGHT and d_row:
                buf_row = 0
                buf_col = 1
    
    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    text_total = courier.render(f'Total:  {total}', 0, WHITE)
    text_speed = courier.render(f'Speed:  {speed}', 0, WHITE)
    screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
    screen.blit(text_speed, (250, SIZE_BLOCK))

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column)%2:
                color = WHITE
            else:
                color = BLUE
            draw_block(color, row, column)

    head = snake_blocks[-1]
    if not head.is_inside():
        print('crash')
        pygame.quit()
        sys.exit()
    
    draw_block(RED, apple.x, apple.y)

    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)

    pygame.display.flip()#что бы изменения применились
    if apple == head:
        total += 1
        speed = total//5 + 1
        snake_blocks.append(apple)
        apple = get_random_empty_block()

    d_row = buf_row
    d_col = buf_col
    head = snake_blocks[-1]
    new_head = SnakeBlock(head.x + d_row, head.y + d_col)

    if new_head in snake_blocks:
        print('crash')
        pygame.quit()
        sys.exit()

    snake_blocks.append(new_head)
    snake_blocks.pop(0)
    
    timer.tick(3+speed)#кол. отрисовки кадров