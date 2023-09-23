import math

import pygame
from character import Character
from colours import PINK

ATTACK_AURA = 200

class Player(Character):
    def __init__(self) -> None:
        super().__init__((0,0))
        self.is_attacking = False
        self.last_attack = 0
        self.attack_cooldown = 1000
        self.attack_rect = None
        self.attack_aura = ATTACK_AURA

    def draw(self, surface):
        pygame.draw.rect(surface, self.rect_colour, self.rect, 1)

        self.attack_rect = pygame.Rect(self.rect.x - (self.attack_aura // 2 - self.size // 2), self.rect.y - (self.attack_aura // 2 - self.size // 2 ),self.attack_aura,self.attack_aura)
        pygame.draw.rect(surface, PINK, self.attack_rect, 1)
    
    def update(self, mobs):
        for mob in mobs:
            mob_distance = math.sqrt(((self.attack_rect.centerx - mob.rect.centerx) ** 2) + ((self.attack_rect.centery - mob.rect.centery)** 2))

            if self.is_attacking and self.last_attack + self.attack_cooldown < pygame.time.get_ticks():
                self.is_attacking = False

            if mob_distance < self.attack_aura and not self.is_attacking:
                self.is_attacking = True
                self.last_attack = pygame.time.get_ticks()
                mob.receive_damage(10)
                print(f"mob.health = {mob.health}")



    