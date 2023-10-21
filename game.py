import pygame
from cannon import Cannon
from bullet import Bullet
from enemy import Enemy
#imports other files
class Game:
    #makes the window screen
    def __init__(self):
        pygame.init()
        self.window_w = 1080
        self.window_h = 720
        self.window = pygame.display.set_mode((self.window_w, self.window_h))

        #displays game window

        self.cannon = Cannon()
        self.bullets = []

        self.shoot_event = pygame.event.custom_type()
        pygame.time.set_timer(self.shoot_event, self.cannon.atk_spd)
        self.clock = pygame.time.Clock()
        self.fps = 60
        #makes the fps 60 with the bullet timer

        self.enemy = Enemy(25, 25, self.window_h, self.window_w, 5, 3, self.cannon.x, self.cannon.y, self.cannon.width, self.cannon.height)

        
    def main_game_loop(self):
        while True:
            self.clock.tick(self.fps)
            self.event_handler()
            self.window.fill((0,0,0))
            self.draw_cannon()
            for bullet in self.bullets:
                bullet.move()
            self.enemy.move()
            self.draw_bullet()
            self.draw_enemy()


            pygame.display.update()
    #types list of all events
    def event_handler(self):
        event_list = pygame.event.get()

        self.cannon.calculate_direction()

        for event in event_list:
            print (event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                #quiting the game event
            if event.type == self.shoot_event:
                new_bullet = Bullet(self.cannon.x, self.cannon.y, self.cannon.width, self.cannon.height, 5, 5, "", 5, 10, self.cannon.direction)
                self.bullets.append(new_bullet)
                #creates a new bullet when the bullet time ends


    def draw_cannon(self):
        #contruct square
        square = pygame.Rect(self.cannon.x, self.cannon.y, self.cannon.width, self.cannon.height)
        #step 2 : draw the square in the window
        pygame.draw.rect(self.window, (0,255,0), square)
        #step 3: tell the window to update

    def draw_bullet(self):
        for bullet in self.bullets:
            square = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
            pygame.draw.rect(self.window, (255,0,0), square)
            #draws bullet on the screen

    def draw_enemy(self):
        #contruct square
        square = pygame.Rect(self.enemy.x, self.enemy.y, self.enemy.width, self.enemy.height)
        #step 2 : draw the enemy in the window
        pygame.draw.rect(self.window, (0,255,0), square)
        #step 3: tell the window to update
