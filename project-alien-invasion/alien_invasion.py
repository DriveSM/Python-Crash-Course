# ---------------------------------------------
#   Program by Anton B.
#
#   Ver.    Date
#   1.0     2021
# ---------------------------------------------

import sys

import pygame


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""
    
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')
        
    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслеживание событийц клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Отображение последнего прорисованног экрана.
            pygame.display.flip()

def main():
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()


if __name__ == '__main__':
    main()
