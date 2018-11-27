import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """初始化飞船设置起始位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 获得船图像
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #在屏幕底部下方开始
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 为船中心存储一个十进制数值
        self.center = float(self.rect.centerx)

        # 运动旗帜
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def center_ship(self):
        """把船放屏幕上."""
        self.center = self.screen_rect.centerx

    def update(self):
        """根据移动更新船的位置"""
        # 更新船的中心值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.up<self.screen_rect.up:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.down>0:
            self.center -= self.ai_settings.ship_speed_factor
        # 更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """将船停在当前位置."""
        self.screen.blit(self.image, self.rect)