import pygame
import sys

WIDTH, HEIGHT = 500, 500


class Game_over_screen:
    pygame.init()

    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game_over_background = pygame.image.load(".\\assets\\images\\fondoGameOver.png")

        self.button1_normal = pygame.image.load(".\\assets\\images\\Boton1SinPresionarGO.png")
        self.button1_pulsado = pygame.image.load(".\\assets\\images\\Boton1PRESIONADOGO.png")
        self.button2_normal = pygame.image.load(".\\assets\\images\\Boton2SinPresionarGO.png")
        self.button2_pulsado = pygame.image.load(".\\assets\\images\\Boton2PRESIONADOGO.png")

        self.button_width, self.button_height = 135, 75
        self.button1_normal = pygame.transform.scale(self.button1_normal, (self.button_width, self.button_height))
        self.button1_pulsado = pygame.transform.scale(self.button1_pulsado, (self.button_width, self.button_height))
        self.button2_normal = pygame.transform.scale(self.button2_normal, (self.button_width, self.button_height))
        self.button2_pulsado = pygame.transform.scale(self.button2_pulsado, (self.button_width, self.button_height))

        self.button1_rect = self.button1_normal.get_rect(center=(2*WIDTH // 4, HEIGHT // 2 + 65))
        self.button2_rect = self.button2_normal.get_rect(center=(2 * WIDTH // 4, HEIGHT // 2 + 140))

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


    def ejecutar(self):
        if self.button_seleccionado == 0:
            self.result = "restart"
        elif self.button_seleccionado == 1:
            self.result = "quit"

        self.running = False


    def dibujar(self):

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
        while self.running:
            self.screen.fill((255, 255, 255))

            self.handle_events()

            self.dibujar()

            pygame.display.flip()

        return self.result

    def go_menu(self):
        from First_screen import First_Screen
        first_screen = First_Screen()
        first_screen.menu_principal()

    def go_exit(self):
        pygame.quit()
        sys.exit()


