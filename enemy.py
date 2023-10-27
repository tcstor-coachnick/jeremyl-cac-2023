import random
import pygame
from game_object import GameObject
class Enemy(GameObject):
    def __init__(self, height, width, window_height, window_width, hp, speed, cannon_x, cannon_y, cannon_width, cannon_height):
        rand_axis = random.randint(0,3)
        if rand_axis == 0:
            y = 0 - height
            x = random.randint(0 - width, window_width)
        if rand_axis == 1:
            x = 0 - width
            y = random.randint(0 - height, window_height)
        if rand_axis == 2:
            y = window_height
            x = random.randint(0 - width, window_width)
        if rand_axis == 3:
            x = window_width
            y = random.randint(0 - height, window_height)
        #which side of the screen enemies spawn on
        super().__init__(x, y, width, height, "")
        self.hp = hp
        self.speed = speed
        self.calculate_direction(cannon_x, cannon_y, cannon_width, cannon_height)

    def calculate_direction(self, cannon_x, cannon_y, cannon_width, cannon_height):
        x = (cannon_x + (cannon_width/2)) - (self.x + (self.width/2))
        y = (cannon_y + (cannon_height/2)) - (self.y + (self.height/2))

        self.direction = pygame.math.Vector2(x,y).normalize()

    def move(self):
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed
    def get_hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)