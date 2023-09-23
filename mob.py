import math

import pygame
from character import Character
from colours import WHITE
import random

ATTACK_RANGE = 10
ENEMY_SPEED = 1

class Mob(Character):
    def __init__(self) -> None:
        super().__init__((random.randint(0, 600),random.randint(0, 800)))
        self.rect_colour = WHITE
        self.speed = 1
        self.is_attacking = False
        self.last_attack = 0
        self.attack_cooldown = 1000

    def ai(self, player):
        dx = 0
        dy = 0

        player_distance = math.sqrt(((self.rect.centerx - player.rect.centerx) ** 2) + ((self.rect.centery - player.rect.centery)** 2))
 
        if self.rect.centerx > player.rect.centerx:
            dx = -ENEMY_SPEED
        if self.rect.centerx < player.rect.centerx:
            dx = ENEMY_SPEED
        if self.rect.centery > player.rect.centery:
            dy = -ENEMY_SPEED
        if self.rect.centery < player.rect.centery:
            dy = ENEMY_SPEED

        self.move(dx, dy, [])

        if self.is_attacking and self.last_attack + self.attack_cooldown < pygame.time.get_ticks():
            self.is_attacking = False

        if player_distance < ATTACK_RANGE and not self.is_attacking:
            self.is_attacking = True
            self.last_attack = pygame.time.get_ticks()
            player.receive_damage(5)
            print(f"player.health: {player.health}")
            

    
