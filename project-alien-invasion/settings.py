# ---------------------------------------------
#   Program by Anton B.
#
#   Ver.    Date
#   1.0     2021
# ---------------------------------------------

class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""
    
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 59, 89)
        self.fps = 60
        # настройки корабля
        self.ship_vel = 4.5


def main():
    pass


if __name__ == '__main__':
    main()
