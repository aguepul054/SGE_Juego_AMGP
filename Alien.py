import pygame
import random
WIDTH, HEIGHT = 500,500


ALIEN_SPEED = 1

enemy_lvl1 = pygame.image.load(".\\assets\\images\\Aliens\\Enemy_1_A_Small.png")
enemy_lvl1_2 = pygame.image.load(".\\assets\\images\\Aliens\\Enemy_1_B_Small.png")
enemy_lvl1_3 = pygame.image.load(".\\assets\\images\\Aliens\\Enemy_1_C_Small.png")
enemy_lvl1_4 =pygame.image.load(".\\assets\\images\\Aliens\\Enemy_1_D_Small.png")

enemy_lvl1 = pygame.transform.scale(enemy_lvl1 ,(50,50))
enemy_lvl1_2 = pygame.transform.scale(enemy_lvl1_2,(50,50))
enemy_lvl1_3 = pygame.transform.scale(enemy_lvl1_3, (50,50))
enemy_lvl1_4 = pygame.transform.scale(enemy_lvl1_4,(50,50))


class Alien(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.gen = generador_imagenes()
        self.image = next(self.gen)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = ALIEN_SPEED
        self.direction = 1

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.direction = -self.direction
            self.rect.y += 10


def generador_imagenes():
    images = [
        enemy_lvl1,
        enemy_lvl1_2,
        enemy_lvl1_3,
        enemy_lvl1_4
    ]
    while True:
        yield random.choice(images)

