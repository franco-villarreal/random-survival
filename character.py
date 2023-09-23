import math
import pygame

from colours import RED


class Character():
    def __init__(self, pos) -> None:
        self.size = 50
        self.rect = pygame.Rect(pos[0],pos[1],self.size,self.size)
        self.rect_colour = RED
        self.speed = 5
        self.health = 100
        self.defense = 0
        self.is_alive = True

    def draw(self, surface):
        pygame.draw.rect(surface, self.rect_colour, self.rect, 1)

    def move(self, dx, dy, obstacles = []):        
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2)/2)
            dy = dy * (math.sqrt(2)/2)
        
        self.rect.x += dx
        self.calculate_dx_collitions(dx, obstacles)
        self.rect.y += dy
        self.calculate_dy_collitions(dy, obstacles)

    def calculate_dx_collitions(self, dx, obstacles):
        for obstacle in obstacles:
            if obstacle[1].colliderect(self.rect):
                if dx > 0:
                    self.rect.right = obstacle[1].left
                if dx < 0:
                    self.rect.left = obstacle[1].right
    
    def calculate_dy_collitions(self, dy, obstacles):
        for obstacle in obstacles:
            if obstacle[1].colliderect(self.rect):
                if dy > 0:
                    self.rect.bottom = obstacle[1].top
                if dy < 0:
                    self.rect.top = obstacle[1].bottom

    def receive_damage(self, damage):
        damage = damage - self.defense

        if damage > 0:
            self.health -= damage
        
        if self.health < 0:
            self.die()
    
    def die(self):
        self.health = 0
        self.is_alive = False
    
