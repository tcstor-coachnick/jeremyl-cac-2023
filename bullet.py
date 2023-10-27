import pygame
from game_object import GameObject
class Bullet(GameObject):
    def __init__(self, cannon_x, cannon_y, cannon_width, cannon_height, bullet_width, bullet_height, image, speed, dmg, direction):
        x = cannon_x + (cannon_width/2) - (bullet_width/2)
        y = cannon_y + (cannon_height/2) - (bullet_height/2)
        super().__init__(x, y, bullet_width, bullet_height, image)
        self.speed = speed
        self.dmg = dmg
        self.direction = direction
        #makes all the variables for bullet
    def move(self):
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed
    def get_hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

