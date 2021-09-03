import pygame

class Enemy(pygame.sprite.Sprite):

    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.move_counter = 0
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 1
    def update(self):
        self.move_counter += 1
        self.rect.x += self.speed
        if self.move_counter == 66:
            self.move_counter = 0
            self.speed *= -1





