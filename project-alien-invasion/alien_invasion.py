# ---------------------------------------------
#   Program by Anton B.
#
#   Ver.    Date
#   1.0     2021
# ---------------------------------------------

import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""
    
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height),
            pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
        pygame.display.set_caption('Alien Invasion')
        pygame.display.set_icon(pygame.image.load(
            r'images/ship.bmp'))
        
        self.ship = Ship(self)
        
        # Назначение цвета фона.
        self.bg_color = self.settings.bg_color
    
    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self.clock.tick(self.settings.fps)  # 60 fps
            
            self._check_events()
            self.ship.update()
            self._update_screen()
    
    def _check_events(self):
        # Отслеживание событийц клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Переместить корабль вправо
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # Переместить корабль влево
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    # Переместить корабль влево
                    self.ship.moving_left = False

            
    def _update_screen(self):
        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        
        # Отображение последнего прорисованног экрана.
        # pygame.display.flip()
        pygame.display.update()


def main():
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()


if __name__ == '__main__':
    main()
