import pygame
from src.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600,400))
        pygame.display.set_caption("Montain Shooter")

    def run(self):
        menu = Menu(self.window)
        while True:
            menu.run()
            # Check for all events
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #pygame.quit()
                    #quit()
