class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (180, 180, 180)

        self.default_fps = 100

        self.player_HP = 6
        self.player_amount = 2
        self.friendly_servant_radius = 120
        self.hostile_servant_radius = 250
        self.player_radius = 400
        self.player_color = [(33, 243, 11), (11, 17, 243), (255, 32, 15)]

        self.HP_bar_length = 120
        self.HP_bar_width = 8
        self.HP_bar_color = (255, 40, 21)

        self.servant_select_circle_radius = 30
        self.servant_size = (self.servant_width, self.servant_height) = (120, 160)
        self.servant_interval = self.servant_height + 2*self.HP_bar_width

        self.hint_duration = 1 * self.default_fps
