import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化 pygame, settings, and screen 对象.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 游戏开始按钮
    play_button = Button(ai_settings, screen, "Play")

    #创建衣蛾实例来存储游戏统计信息和计分板
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 造一艘船和一群外星人以及发射子弹
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 一群外星人
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的循环控制.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)


run_game()