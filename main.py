import pygame

from character import Character
from colours import BLACK
from mob import Mob
from player import Player

FPS = 60
CAPTION = "Random Survivals"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
pygame.display.set_caption(CAPTION)

clock = pygame.time.Clock()
screen_info = pygame.display.Info()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

moving_left = False
moving_right = False
moving_up = False
moving_down = False



player = Player()
mobs = []

last_mob_spawn = pygame.time.get_ticks()
mobs_spawn_cooldown = 5000

def handle_move():
    dx = 0
    dy = 0

    if moving_right:
        dx = player.speed
    if moving_left:
        dx = -player.speed
    if moving_up:
        dy = -player.speed
    if moving_down:
        dy = player.speed

    return dx, dy

def spawn_mob():
    ticks = pygame.time.get_ticks()
    if ticks > last_mob_spawn + mobs_spawn_cooldown:
        mob = Mob()
        mobs.append(mob)
        last_mob_spawn = ticks
killed_mobs = 0


run = True
while run:
    clock.tick(FPS)
    screen.fill(BLACK)

    ticks = pygame.time.get_ticks()
    if ticks > last_mob_spawn + mobs_spawn_cooldown:
        mob = Mob()
        mobs.append(mob)
        last_mob_spawn = ticks

    dx, dy = handle_move()
    player.move(dx, dy)
    player.update(mobs)
    player.draw(screen)

    for mob in mobs:
        mob.ai(player)
        mob.draw(screen)

        if not mob.is_alive:
            killed_mobs += 1
            print(f"killed_mobs = {killed_mobs}")
            mobs.remove(mob)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True
            if event.key == pygame.K_ESCAPE:
                pause_game = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False

    pygame.display.update()

pygame.quit()