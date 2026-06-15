import pygame
import sys

class Menu:
    def __init__(self, window):
        self.window = window

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.window.fill((0,0,0))
            pygame.display.update()