class Settings():
    """设置类."""

    def __init__(self):
        """可视化界面参数."""
        # Screen settings.
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 玩家限制的次数
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 外星人设置
        self.fleet_drop_speed = 10

        # 游戏速度
        self.speedup_scale = 1.1
        # 外星人分数点设置
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化游戏改变得设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # 得分
        self.alien_points = 50

        # 1右-1左
        self.fleet_direction = 1

    def increase_speed(self):
        """增加速度设置和外点值"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)