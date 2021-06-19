import pygame
from pygame.locals import *
import time
SIZE = 40
class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("\source_image\apple.png").convert()
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x,self.y))
        pygame.display.flip()


class Snake:
    def __init__(self, surface, length):
        self.length = length
        self.parent_screen = surface
        self.block = pygame.image.load("\source_image\body_snake.png").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'left'

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i],self.y[i]))
        pygame.display.flip()


    def move_left(self):
        self.direction = 'left'
        self.x -= 10
        self.draw()

    def move_right(self):
        self.direction = 'right'
        self.x += 10
        self.draw()

    def move_down(self):
        self.direction = 'down'
        self.y += 10
        self.draw()

    def move_up(self):
        self.direction = 'up'
        self.y -= 10
        self.draw()
    def keep_moving(self):
        if self.direction == 'left':
            self.x -= 10
        if self.direction == 'right':
            self.x += 10
        if self.direction == 'down':
            self.y += 10
        if self.direction == 'up':
            self.y -= 10
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((255, 255, 255))
        self.snake = Snake(self.surface,2)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_UP:
                        self.snake.move_up()

                if event.type == QUIT:
                    running = False
            self.snake.walk()
            self.apple.draw()
            time.sleep(0.2)

if __name__ == "__main__":
    game = Game()
    game.run()
