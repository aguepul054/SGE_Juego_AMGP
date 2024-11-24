from Game import *
import pygame
import sys

# Iniciamos pygame y su sonido
pygame.init()
pygame.mixer.init()

# Dimensión de la ventana
WIDTH, HEIGHT = 500, 500


class First_Screen:
    def __init__(self):
        # Inicialización de la clase Juego y configuración de la pantalla
        self.juego = Game()
        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Menú Principal Python Invaders')

        # Fuente para el texto y carga de imágenes para los botones y fondo
        self.fuente = pygame.font.SysFont('Arial', 30)
        self.fondo_imagen = pygame.image.load(".\\assets\\images\\TitleGame.png")
        self.fondo_imagen = pygame.transform.scale(self.fondo_imagen, (WIDTH, HEIGHT))

        # Carga de las imágenes de los botones con tamaños ajustados
        self.buttonIniciar_normal = pygame.image.load(".\\assets\\images\\botonIniciar.png")
        self.buttonIniciar_presionado = pygame.image.load(".\\assets\\images\\botonIniciarPresionado.png")
        self.buttonSalir_normal = pygame.image.load(".\\assets\\images\\botonSalir.png")
        self.buttonSalir_presionado = pygame.image.load(".\\assets\\images\\botonSalirPresionado.png")

        # Redimensionamiento de los botones
        self.button_width, self.button_height = 135,75
        self.buttonIniciar_normal =  pygame.transform.scale(self.buttonIniciar_normal, (self.button_width, self.button_height))
        self.buttonIniciar_presionado =  pygame.transform.scale(self.buttonIniciar_presionado, (self.button_width, self.button_height))
        self.buttonSalir_normal =  pygame.transform.scale(self.buttonSalir_normal, (self.button_width, self.button_height))
        self.buttonSalir_presionado =  pygame.transform.scale(self.buttonSalir_presionado, (self.button_width, self.button_height))

        # Posicionamiento de los botones en la pantalla
        self.buttonIniciar_rect = self.buttonIniciar_normal.get_rect(center = (8*self.button_width//4, self.button_height//4+290))
        self.buttonSalir_rect = self.buttonSalir_normal.get_rect(center = (8*self.button_width//4, self.button_height//2+360))

        # Control de cuál botón está seleccionado
        self.button_seleccionado = 0
        self.result = None



    def handle_events(self):
        # Detección de pulsaciones de teclas o cierre de la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.result = "quit"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.button_seleccionado = (self.button_seleccionado + 1) % 2 # Cambio de selección
                elif event.key == pygame.K_UP:
                    self.button_seleccionado = (self.button_seleccionado - 1) % 2 # Cambio de selección
                elif event.key == pygame.K_RETURN:
                    self.ejecutar() # Ejecuta la acción del botón seleccionado



    def dibujar(self):
        # Dibuja el fondo y los botones, con el aspecto correspondiente según la selección
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
        # Condigura y ejecuta la pantalla de título con música de fondo
        pygame.mixer.music.stop()
        pygame.mixer.music.load(".\\assets\\music\\toby fox - UNDERTALE Soundtrack - 02 Start Menu.mp3")
        pygame.mixer.music.play(loops=-1, start=0.0)
        pygame.mixer.music.set_volume(0.5)

        # Bucle principal que mantiene el menú activo
        while self.running:
            self.handle_events()
            self.dibujar()
            pygame.display.flip() # Actualiza la pantalla
        return self.result

    def ejecutar(self):
        # Ejecuta la acción correspondiente dependiendo del botón seleccionado
        if self.button_seleccionado == 0:
            self.result = "start" # Inicia el juego
        elif self.button_seleccionado == 1:
            self.result = "quit" # Cierra el juego

        self.running = False

    def go_game(self):
        # Llama al metodo para iniciar el juego
        self.juego.start_game()

    def go_exit(self):
        # Cierra pygame y sale del programa
        pygame.quit()
        sys.exit()

