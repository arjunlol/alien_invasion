class Settings():
    """A class storing all settings for alien invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 600
        self.screen_height= 450
        self.bg_color = (230,230,230)

        #Ship Settings
        self.ship_speed_factor = 1.5
