import pygame
from game_object import GameObject
class Cannon(GameObject):    
    def __init__(self):
        super().__init__(515,335, 50, 50, "")
        self.direction = pygame.math.Vector2(0,-1)
        self.hp = 100
        self.atk_spd = 750
        self.dmg = 10
    def calculate_direction(self):
        mouse_pos = pygame.mouse.get_pos()

        x = mouse_pos[0] - (self.x + self.width/2)
        y = mouse_pos[1] - (self.y + self.height/2)

        if x == 0 and y == 0:
            x = 0
            y = -1
        #normalizing the vectors

        self.direction = pygame.math.Vector2(x,y).normalize()
