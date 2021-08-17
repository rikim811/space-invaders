import pygame
from player import Player
from enemy import Enemy
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

screen_width = 600
screen_height = 800
clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Space Invaders")
bg = pygame.image.load('img/bg.png')

#load sound
lazer_fx = pygame.mixer.Sound('img/laser.wav')
mixer.music.set_volume(0.7)


#player
player = Player()
player_group = pygame.sprite.Group(player)

#enemies
enemy = Enemy(pygame.image.load('img/alien1.png'),300,150)
enemy_group = pygame.sprite.Group(enemy)


while True:
  time = pygame.time.get_ticks()
  keys = pygame.key.get_pressed()
  player.update(keys,screen_width)

  if keys[pygame.K_SPACE] and time - player.last_fired < player.gun_cooldown:
    lazer_fx.play()
    print("pew pew")

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit(0)

  screen.blit(bg,(0,0))
  player_group.draw(screen)
  enemy_group.draw(screen)
  pygame.display.update()
  clock.tick(FPS)