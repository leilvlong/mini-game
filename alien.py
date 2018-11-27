import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """创造一个外星人类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置起始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像,并设置rect属性.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 在屏幕上开始每一个外星人
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 外星人的确切位置
        self.x = float(self.rect.x)

    def check_edges(self):
        """如果外星人在屏幕边缘,返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """外星人左右移动."""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """画出外星人的位置."""
        self.screen.blit(self.image, self.rect)

