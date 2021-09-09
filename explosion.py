import pygame


from bullet import EnemyBullet

class Explosion(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1,5):
            self.images.append(pygame.image.load(f'img/exp{i}.png'))
        self.image = self.images[0]
        self.rect = self.image.get_rect
        self.x = x
        self.y = y

