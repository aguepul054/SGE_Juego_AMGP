import pygame
import random
#Definimos el tamaño de la pantalla del juego
WIDTH, HEIGHT = 500,500

#Velocidad del alien
ALIEN_SPEED = 3

#Cargamos las imagenes de aliens y las redimensionamos
enemy_lvl1 = pygame.image.load(".\\assets\\images\\Aliens\\Enemy_1_A_Small.png")
enemy_lvl1_2 = pygame.image.load(".\\assets\\images\\Aliens\\Enemy_1_B_Small.png")
enemy_lvl1_3 = pygame.image.load(".\\assets\\images\\Aliens\\Enemy_1_C_Small.png")
enemy_lvl1_4 =pygame.image.load(".\\assets\\images\\Aliens\\Enemy_1_D_Small.png")
enemy_lvl2 = pygame.image.load(".\\assets\\images\\Aliens\\Enemy_2_A_Small.png")
enemy_lvl2_2 = pygame.image.load(".\\assets\\images\\Aliens\\Enemy_2_B_Small.png")
enemy_lvl2_3 = pygame.image.load(".\\assets\\images\\Aliens\\Enemy_3_A_Small.png")
enemy_lvl2_4 =pygame.image.load(".\\assets\\images\\Aliens\\Enemy_3_B_Small.png")
enemy_lvl3 = pygame.image.load(".\\assets\\images\\Aliens\\Enemy_4_A_Small.png")
enemy_lvl3_2 = pygame.image.load(".\\assets\\images\\Aliens\\Enemy_4_B_Small.png")
enemy_lvl3_3 = pygame.image.load(".\\assets\\images\\Aliens\\Enemy_4_C_Small.png")
enemy_lvl3_4 =pygame.image.load(".\\assets\\images\\Aliens\\Enemy_4_D_Small.png")

#Redimension de imagenes
enemy_lvl1 = pygame.transform.scale(enemy_lvl1 ,(50,50))
enemy_lvl1_2 = pygame.transform.scale(enemy_lvl1_2,(50,50))
enemy_lvl1_3 = pygame.transform.scale(enemy_lvl1_3, (50,50))
enemy_lvl1_4 = pygame.transform.scale(enemy_lvl1_4,(50,50))
enemy_lvl2 = pygame.transform.scale(enemy_lvl2 ,(50,50))
enemy_lvl2_2 = pygame.transform.scale(enemy_lvl2_2,(50,50))
enemy_lvl2_3 = pygame.transform.scale(enemy_lvl2_3, (50,50))
enemy_lvl2_4 = pygame.transform.scale(enemy_lvl2_4,(50,50))
enemy_lvl3 = pygame.transform.scale(enemy_lvl3 ,(50,50))
enemy_lvl3_2 = pygame.transform.scale(enemy_lvl3_2,(50,50))
enemy_lvl3_3 = pygame.transform.scale(enemy_lvl3_3, (50,50))
enemy_lvl3_4 = pygame.transform.scale(enemy_lvl3_4,(50,50))


class Alien(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.gen = generador_imagenes() # Usamos un generador de imágenes para asignar una imagen aleatoria al alien
        self.image = next(self.gen) # Asignamos la imagen aleatoria
        self.rect = self.image.get_rect() # Obtenemos el rect
        self.rect.x = x # Posicion inicial en el eje x
        self.rect.y = y # Posicion inicial en el eje y
        self.speed = ALIEN_SPEED # Velocidad del alien
        self.direction = 1 # Dirección inicial: 1 (Derecha)
        self.descenso = 10 # Cuánto desciente el alien al llegar al borde

    def update(self):

        self.rect.x += self.speed * self.direction # Movemos al alien según la dirección

        # Si el alien llega al borde de la pantalla (derecha o izquierda)
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.direction = -self.direction # Cambia la dirección ( de derecha a izquierda o viceversa)
            self.rect.y += self.descenso # Baja un poco

# Esta función genera aleatoriamente una imagen para el alien entre varias opciones
def generador_imagenes():
    # Lista de posibles imágenes para los aliens
    images = [
        enemy_lvl1,
        enemy_lvl1_2,
        enemy_lvl1_3,
        enemy_lvl1_4,
        enemy_lvl2,
        enemy_lvl2_2,
        enemy_lvl2_3,
        enemy_lvl2_4,
        enemy_lvl3,
        enemy_lvl3_2,
        enemy_lvl3_3,
        enemy_lvl3_4
    ]
    # Usamos un generador para devolver una imagen aleatoria continuamente
    while True:
        yield random.choice(images)

