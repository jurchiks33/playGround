class GameStats:
    """Track statistics for alien invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.ai_settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0