class GameStats():

    def __init__(self, ai_settings):
        """数据更新统计"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 在不活跃状态下开始游戏
        self.game_active = False

        # 最高分不被重置
        self.high_score = 0

    def reset_stats(self):
        """\初始化可在游戏中统计的数据."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1