import sys
import pygame.display
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from src.const import COLOR_WHITE, WIN_WIDTH, WIN_HEIGHT
from src.entity import Entity
from src.entityFactory import EntityFactory

class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))
        self.timeout = 20000 # 20 Segundos

    def run(self):
        pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()

            # Printed Text
            self.level_text(
                14,
                f'{self.name} Timeout: {self.timeout / 1000:.1f}s',
                COLOR_WHITE,
                (10, 5)
            )

            self.level_text(
                14,
                f'FPS: {clock.get_fps():.0f}',
                COLOR_WHITE,
                (10, WIN_HEIGHT - 35)
            )

            self.level_text(
                14,
                f'Entidades: {len(self.entity_list)}',
                COLOR_WHITE,
                (10, WIN_HEIGHT - 20)
            )

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        pass


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

