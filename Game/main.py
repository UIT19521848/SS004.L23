import pygame
from pygame.locals import *


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = None
        self.x = 0
        self.y = 0

    def draw(self):
        pass


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = None
        self.x = 0
        self.y = 0

    def draw(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass

    def move_down(self):
        pass

    def move_up(self):
        pass


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((255, 255, 255))
        self.snake = Snake(self.surface)
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
            pass


if __name__ == "__main__":
    game = Game()
    game.run()
