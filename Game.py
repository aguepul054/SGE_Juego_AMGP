

from Player import *
from Alien import *
from Bullet import *
from Game_over_screen import *
from Win_screen import Win_screen


WHITE = (255, 255, 255) # Color blanco para textos en pantalla
WIDTH, HEIGHT = 500, 500 # Dimensiones de la ventana de juego
ALIEN_ROWS = 4 # Número de filas de alienígenas
ALIEN_COLS = 7 # Número de columnas de alienígenas
FPS = 60 # Capamos los FPS a 60

class Game:

    def __init__(self):
        # Iniciamos pygame y la configuración de la ventana
        pygame.init()
        pygame.mixer.init() # Inicializa el mezclador de música
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Tamaño de la ventana
        pygame.display.set_caption('Python Invaders') # Titulo de la ventana

        # Carga y ajusta el fondo de pantalla
        self.fondo_juego = pygame.image.load(".\\assets\\images\\python_invaders_background.png")
        self.fondo_juego = pygame.transform.scale(self.fondo_juego, (WIDTH, HEIGHT))

        # Grupo de sprites para organizar el juego
        self.all_sprites = pygame.sprite.Group()
        self.bullets_sprites = pygame.sprite.Group()
        self.aliens_sprites = pygame.sprite.Group()

        # Creación del jugador y su adición al grupo de sprites
        self.player = Player()
        self.all_sprites.add(self.player)

        # Creación de los alienígenas y su adición a los grupos correspondientes
        for row in range(ALIEN_ROWS):
            for col in range(ALIEN_COLS):
                alien = Alien(50 + col * 60, 50 + row * 60)  # Posiciona cada alienígena con un espaciado entre ellos
                self.all_sprites.add(alien)
                self.aliens_sprites.add(alien) # Los alienígenas son añadidos también al grupo específico de aliens

    def start_game(self):
        pygame.mixer.music.stop() # Detiene cualquier música que este sonando
        pygame.mixer.music.load(".\\assets\\music\\toby fox - UNDERTALE Soundtrack - 14 Heartache.mp3") # Carga música
        pygame.mixer.music.play(loops=-1, start=0.0) # Reproduce la música en bucle
        pygame.mixer.music.set_volume(0.5) # Ajusta el volumen

        clock = pygame.time.Clock() # Crea un objeto para controlar los FPS
        running = True # Variable que indica si el juego sigue en ejecución

        while running:
            clock.tick(FPS) # Limita la cantidad de fotogramas por segundo

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False # Termina el juego si se cierra la ventana
                if event.type == pygame.KEYDOWN: # Si se presiona una letra
                    if event.key == pygame.K_SPACE: # Si la tecla es espacio
                        bullet = Bullet(self.player.rect.centerx, self.player.rect.top) # Crea una bala en la posicion del jugador
                        self.all_sprites.add(bullet) # Añade la bala al grupo de sprites
                        self.bullets_sprites.add(bullet) # Añade la bala al grupo específico de balas

            self.all_sprites.update() # Actualiza la posición de todos los sprites

            # Revisa si el jugador colisiona con algún alienígena
            if pygame.sprite.spritecollide(self.player, self.aliens_sprites, False):
                self.game_over()  # Si hay colisión, el jugado pierde y se muestra la pantalla de game over

            # Revisa si el jugador colisiona con algún alienígena
            for bullet in self.bullets_sprites:
                alien_hits = pygame.sprite.spritecollide(bullet, self.aliens_sprites, True) # Elimina los aliens alcanzados por la bala
                if alien_hits:
                    bullet.trigger_explosion() # Activa una explosión

            # Si no quedan aliens, el jugador gana
            if not self.aliens_sprites:
                self.win_game() # Muestra la pantalla de victoria
                running = False # Detiene el bucle del juego

            # Dibuja el fondo y todos los sprites en la pantalla
            self.screen.blit(self.fondo_juego, (0, 0))
            self.all_sprites.draw(self.screen)

            # Muestra e pantalla el número de aliens restantes
            score_text = pygame.font.SysFont("Arial Black", 20).render(
                f"Aliens Restantes: {len(self.aliens_sprites)}",
                True, WHITE)
            self.screen.blit(score_text, (10, 10))

            pygame.display.flip() # Actualiza la pantalla con los cambios realizados

        pygame.quit()
        sys.exit()

    def game_over(self):
        gameov = Game_over_screen()
        result = gameov.go_screen() # Llama a la pantalla de Game Over

        if result == "restart":
            gameov.go_menu()  # Si elige reiniciar, regresa al menu
        elif result == "quit":
            gameov.go_exit() # Si eige salir, acaba el juego

    def win_game(self):
        wingame = Win_screen()
        result = wingame.go_screen() # Llama a la pantalla de victoria

        if result == "restart":
            wingame.go_menu()
        elif result == "quit":
            wingame.go_exit()
