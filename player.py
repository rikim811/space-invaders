import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 300
        self.rect.bottom = 760
        self.speed = 8
        self.screen_width = 600
        self.lazer_fx = pygame.mixer.Sound('img/laser.wav')
        self.lazer_fx.set_volume(0.05)
        self.bullet_image = pygame.image.load('img/bullet.png')
        self.gun_cooldown = 400
        self.last_fired = pygame.time.get_ticks()


    def update(self,Bullet,bullet_group):
        time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] and self.rect.right < self.screen_width:
            self.rect.x += self.speed

        if keys[pygame.K_SPACE] and time - self.last_fired > self.gun_cooldown:
            self.lazer_fx.play()
            x = self.rect.centerx
            y = self.rect.top
            bullet = Bullet(self.bullet_image, x, y)
            bullet_group.add(bullet)
            self.last_fired = time




