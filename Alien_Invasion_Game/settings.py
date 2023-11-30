class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize game's settings."""
        #Screen Settings
        self.screen_width = 1500
        self.screen_height = 900
        self.bg_color = (36, 33, 36)
        self.bullets_allowed = 30

        #Ship settings
        self.ship_speed = 2.5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed = 7.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (218,165,32)

        #Alien settings/
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #Fleet direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1