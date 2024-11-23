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
        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Menú Principal Python Invaders')

        self.fuente = pygame.font.SysFont('Arial', 30)

        self.fondo_imagen = pygame.image.load(".\\assets\\images\\TitleGame.png")
        self.fondo_imagen = pygame.transform.scale(self.fondo_imagen, (WIDTH, HEIGHT))

        self.buttonIniciar_normal = pygame.image.load(".\\assets\\images\\botonIniciar.png")
        self.buttonIniciar_presionado = pygame.image.load(".\\assets\\images\\botonIniciarPresionado.png")
        self.buttonSalir_normal = pygame.image.load(".\\assets\\images\\botonSalir.png")
        self.buttonSalir_presionado = pygame.image.load(".\\assets\\images\\botonSalirPresionado.png")


        self.button_width, self.button_height = 135,75
        self.buttonIniciar_normal =  pygame.transform.scale(self.buttonIniciar_normal, (self.button_width, self.button_height))
        self.buttonIniciar_presionado =  pygame.transform.scale(self.buttonIniciar_presionado, (self.button_width, self.button_height))
        self.buttonSalir_normal =  pygame.transform.scale(self.buttonSalir_normal, (self.button_width, self.button_height))
        self.buttonSalir_presionado =  pygame.transform.scale(self.buttonSalir_presionado, (self.button_width, self.button_height))

        self.buttonIniciar_rect = self.buttonIniciar_normal.get_rect(center = (8*self.button_width//4, self.button_height//4+290))
        self.buttonSalir_rect = self.buttonSalir_normal.get_rect(center = (8*self.button_width//4, self.button_height//2+360))

        self.button_seleccionado = 0
        self.result = None



    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.result = "quit"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.button_seleccionado = (self.button_seleccionado + 1) % 2
                elif event.key == pygame.K_UP:
                    self.button_seleccionado = (self.button_seleccionado - 1) % 2
                elif event.key == pygame.K_RETURN:
                    self.ejecutar()



    def dibujar(self):
        self.screen.blit(self.fondo_imagen, (0, 0))

        if self.button_seleccionado == 0:
            self.screen.blit(self.buttonIniciar_presionado, self.buttonIniciar_rect)
        else:
            self.screen.blit(self.buttonIniciar_normal, self.buttonIniciar_rect)

        if self.button_seleccionado == 1:
            self.screen.blit(self.buttonSalir_presionado, self.buttonSalir_rect)
        else:
            self.screen.blit(self.buttonSalir_normal, self.buttonSalir_rect)


    def tit_screen(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(".\\assets\\music\\toby fox - UNDERTALE Soundtrack - 02 Start Menu.mp3")
        pygame.mixer.music.play(loops=-1, start=0.0)
        pygame.mixer.music.set_volume(0.5)
        while self.running:

            self.handle_events()
            self.dibujar()
            pygame.display.flip()
        return self.result

    def ejecutar(self):

        if self.button_seleccionado == 0:
            self.result = "start"
        elif self.button_seleccionado == 1:
            self.result = "quit"

        self.running = False

    def go_game(self):
        self.juego.start_game()

    def go_exit(self):
        pygame.quit()
        sys.exit()

