"Cambio de proyecto"
from Game import *

"Nombre: Python Invaders"

import pygame
import sys

pygame.init()
pygame.mixer.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WIDTH, HEIGHT = 500, 500


class First_Screen:
    def __init__(self):
        self.juego = Game()
        pygame.mixer.music.load(".\\assets\\music\\toby fox - UNDERTALE Soundtrack - 02 Start Menu.mp3")

        self.pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Menú Principal Python Invaders')

        self.fuente = pygame.font.SysFont('Arial', 30)

        self.fondo_imagen = pygame.image.load(".\\assets\\images\\TitleGame.png")
        self.fondo_imagen = pygame.transform.scale(self.fondo_imagen, (WIDTH, HEIGHT))

        # Funcion para poner texto y mostrarlo en pantalla

    def mostrar_texto(self,texto, color, x, y):
        texto_render = self.fuente.render(texto, True, color)
        self.pantalla.blit(texto_render, (x, y))

    def menu_principal(self):
        en_menu = True
        pygame.mixer.music.play(-1)
        while en_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.stop()
                        self.iniciar_juego()
                    elif event.key == pygame.K_2:
                        self.opciones()
                    elif event.key == pygame.K_3:
                        pygame.quit()
                        sys.exit()

            self.pantalla.blit(self.fondo_imagen, (0, 0))
            self.mostrar_texto("1. Iniciar", GREEN, WIDTH // 3, HEIGHT // 2)
            self.mostrar_texto("2. Opciones", RED, WIDTH // 3, HEIGHT // 2 + 50)
            self.mostrar_texto("3. Salir", RED, WIDTH // 3, HEIGHT // 2 + 1100)
            pygame.display.update()

    def iniciar_juego(self):
        self.juego.start_game()

    def opciones(self):
        print("Opciones!")
