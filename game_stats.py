class GameStats:
    """Отслеживание статистики для игры."""

    def __init__(self, ai_game):
        """Инициализирует статистику игры."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
