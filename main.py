import pygame
from player import Player
from enemy import Enemy
from pygame import mixer
from bullet import Bullet
from enemy_bullets import EnemyBullets
import random

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()
time_past = 0
game_status = False

screen_width = 600
screen_height = 800
clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Space Invaders")
bg = pygame.image.load('img/bg.png')

#load sound




#player
player = Player()
player_group = pygame.sprite.Group(player)

#bullet

bullet_group = pygame.sprite.Group()
#enemy_bullet
enemy_bullet_cooldown = 1000
enemy_bullets = EnemyBullets()


#bullet
bullet_image = pygame.image.load('img/bullet.png')
bullet_group = pygame.sprite.Group()

#enemies
enemy_image =[]
for i in range(1,5):
  location = f'img/alien{str(i)}.png'
  enemy_image.append(location)
enemy_group = pygame.sprite.Group()
for p in range(5):
  for i in range(5):
    enemy = Enemy(pygame.image.load(random.choice(enemy_image)),65+100*i,150+75*p)
    enemy_group.add(enemy)

while True:


  player.update(player,Bullet,bullet_group)

  for enemy in enemy_group:
    enemy.update()

  for bullet in bullet_group:
    bullet.update(enemy_group)
    enemy_bullets.update(player_group, enemy_group)







  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit(0)
  time_past += 1

  screen.blit(bg,(0,0))
  player_group.draw(screen)
  enemy_group.draw(screen)
  bullet_group.draw(screen)
  enemy_bullets.draw(screen)
  pygame.display.update()
  clock.tick(FPS)