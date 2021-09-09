import random
from bullet import EnemyBullet


import pygame
class EnemyBullets(pygame.sprite.Group):

    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.cooldown = 1000
        self.last_shot = pygame.time.get_ticks()
        self.enemy_bullet_image = pygame.image.load('img/alien_bullet.png')

    def update(self, player_group,enemy_group,explosion_group):
        if pygame.time.get_ticks() - self.last_shot > self.cooldown:
            shooter = random.choice(enemy_group.sprites())
            x = shooter.rect.centerx
            y = shooter.rect.bottom
            self.last_shot = pygame.time.get_ticks()

            bullet = EnemyBullet(self.enemy_bullet_image, x, y)
            self.add(bullet)

        for bullet in self.sprites():
            bullet.update(player_group, explosion_group)
