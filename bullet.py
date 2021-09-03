import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self,image,x,y,):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 8

    def update(self,enemy_group):
        self.rect.y -= self.speed
        if self.rect.centery == 0:
            self.kill()
        if pygame.sprite.spritecollide(self,enemy_group,True):
            self.kill()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 4


    def update(self,player_group):
        self.rect.y += self.speed
        if self.rect.centery == 800:
            self.kill()
        if pygame.sprite.spritecollide(self,player_group,False):
            self.kill()
