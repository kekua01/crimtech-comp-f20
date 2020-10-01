import random
import pygame
import sys
import math

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1),
    'l' : (-1,0),
    'r' : (1,0)
}


class Snake(object):
    l = 1
    body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False
    ready = False

    def __init__(self):
        pass
    
    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        check = [self.direction, dir]
        if ('l' not in check and 'r' not in check) or ('u' not in check and 'd' not in check):
            pass
        else:
            self.direction = dir

    def collision(self):
        head = self.get_head()
        if head[0] > 23 or head[0] < 0 or head[1] < 0 or head[1] > 23 or head in self.body[1:]:
            return True
    
    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self, grow):
        if self.ready:
            if self.collision():
                self.kill()
            else:
                x, y = DIR[self.direction]
                new_pos = [(self.body[0][0]+x, self.body[0][1]+y)] + self.body[:-1] 
                if grow: 
                    new_pos.append(self.body[-1])
                    self.l += 1
                self.body = new_pos


    def kill(self):
        # TODO: See section 11, "Try again!"
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i), r)

    def handle_keypress(self, k):
        if k == pygame.K_UP:
            self.turn('u')
        if k == pygame.K_DOWN:
            self.turn('d')
        if k == pygame.K_LEFT:
            self.turn('l')
        if k == pygame.K_RIGHT:
            self.turn('r')

        # Implements feature #10. Also see lines (26) and (56)
        if k == pygame.K_SPACE:
            self.ready = True
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            self.handle_keypress(event.key)
    

# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        x = None
        while (not x) or x in snake:
            x = (rand_int(23), rand_int(23))
        self.position = x

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    apple = Apple()

    score = 0

    while True:
        grow = False
        ready = snake.ready
        # Implements feature #9
        clock.tick(9 + (1.2*math.log(score+0.1)))
        snake.check_events()
        draw_grid(surface)

        if snake.body[0] == apple.position:
            apple.place(snake.body)
            score += 1
            grow = True

        snake.move(grow)

        snake.draw(surface)
        apple.draw(surface)
        
        

        screen.blit(surface, (0,0))
        font = pygame.font.Font('freesansbold.ttf', 22)
        textScore = font.render('Score: ' + str(score), True, (255, 255, 255), None) 
        textStart = font.render('Press the space bar to begin!', True, (255, 255, 255), None)
        textRect1 = textScore.get_rect() 
        textRect2 = textStart.get_rect()
        textRect1.center = (WIDTH*SIZE*17/20, HEIGHT*SIZE/25) 
        textRect2.center = (WIDTH*SIZE*8/20, HEIGHT*SIZE/25) 
        screen.blit(textScore, textRect1) 
        if not ready:
            screen.blit(textStart, textRect2) 

        pygame.display.update()
        if snake.dead:
            print('You died. Score: %d' % score)
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()