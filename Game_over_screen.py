import pygame
import sys

WIDTH, HEIGHT = 500, 500


class Game_over_screen:
    pygame.init()

    def __init__(self):
        self.running = True # Variable que control el bucle principal de la pantalla derrota
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game_over_background = pygame.image.load(".\\assets\\images\\fondoGameOver.png") # Carga el fondo de la pantalla de derrota

        # Carga las imágenes de los botones ( uno para reiniciar y otro para salir )
        self.button1_normal = pygame.image.load(".\\assets\\images\\Boton1SinPresionarGO.png")
        self.button1_pulsado = pygame.image.load(".\\assets\\images\\Boton1PRESIONADOGO.png")
        self.button2_normal = pygame.image.load(".\\assets\\images\\Boton2SinPresionarGO.png")
        self.button2_pulsado = pygame.image.load(".\\assets\\images\\Boton2PRESIONADOGO.png")

        # Redimensionamiento de los botones
        self.button_width, self.button_height = 135, 75
        self.button1_normal = pygame.transform.scale(self.button1_normal, (self.button_width, self.button_height))
        self.button1_pulsado = pygame.transform.scale(self.button1_pulsado, (self.button_width, self.button_height))
        self.button2_normal = pygame.transform.scale(self.button2_normal, (self.button_width, self.button_height))
        self.button2_pulsado = pygame.transform.scale(self.button2_pulsado, (self.button_width, self.button_height))

        # Posicionamiento de los botones en la pantalla
        self.button1_rect = self.button1_normal.get_rect(center=(2*WIDTH // 4, HEIGHT // 2 + 65))
        self.button2_rect = self.button2_normal.get_rect(center=(2 * WIDTH // 4, HEIGHT // 2 + 160))

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
                    self.button_seleccionado = (self.button_seleccionado + 1) % 2
                elif event.key == pygame.K_UP:
                    self.button_seleccionado = (self.button_seleccionado - 1) % 2
                elif event.key == pygame.K_RETURN:
                    self.ejecutar() # Ejecuta la acción del botón seleccionado


    def ejecutar(self):
        # Ejecuta la acción correspondiente dependiendo del botón seleccionado
        if self.button_seleccionado == 0:
            self.result = "restart" # Volver al menu
        elif self.button_seleccionado == 1:
            self.result = "quit" # Cerrar juego

        self.running = False


    def dibujar(self):
        # Dibuja el fondo y los botones, con el aspecto correspondiente según la selección
        self.screen.blit(self.game_over_background, (0, 0))

        if self.button_seleccionado == 0:
            self.screen.blit(self.button1_pulsado, self.button1_rect)
        else:
            self.screen.blit(self.button1_normal, self.button1_rect)

        if self.button_seleccionado == 1:
            self.screen.blit(self.button2_pulsado, self.button2_rect)
        else:
            self.screen.blit(self.button2_normal, self.button2_rect)


    def go_screen(self):
        # Condigura y ejecuta la pantalla de título con música de fondo
        pygame.mixer.music.stop()
        pygame.mixer.music.load(".\\assets\\music\\toby fox - UNDERTALE Soundtrack - 11 Determination.mp3")
        pygame.mixer.music.play(loops=-1, start=0.0)
        pygame.mixer.music.set_volume(0.5)

        # Bucle principal que mantiene el menú activo
        while self.running:
            self.screen.fill((255, 255, 255))
            self.handle_events()
            self.dibujar()
            pygame.display.flip() # Actualiza la pantalla
        return self.result

    def go_menu(self):
        # Volver al menu de nuevo
        from First_screen import First_Screen
        first_screen = First_Screen()
        result = first_screen.tit_screen()
        if result == "start":
            first_screen.go_game()
        elif result == "quit":
            first_screen.go_exit()

    def go_exit(self):
        # Salir del juego
        pygame.quit()
        sys.exit()


