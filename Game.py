
from pygame import *
import sys

from Player import *
from Alien import *
from Bullet import *
from Game_over_screen import *
from Win_screen import Win_screen

# PROYECTO SIN IMAGENES / ANIMACIONES / COLISIONES ENTRE ALIENS

WHITE = (255, 255, 255)
WIDTH, HEIGHT = 500, 500
ALIEN_ROWS = 4
ALIEN_COLS = 6
# Esto es para capar a los 60fps
FPS = 60

class Game:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Python Invaders')

        self.fondo_juego = pygame.image.load(".\\assets\\images\\python_invaders_background.png")
        self.fondo_juego = pygame.transform.scale(self.fondo_juego, (WIDTH, HEIGHT))


        self.all_sprites = pygame.sprite.Group()
        self.bullets_sprites = pygame.sprite.Group()
        self.aliens_sprites = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        for row in range(ALIEN_ROWS):
            for col in range(ALIEN_COLS):
                alien = Alien(50 + col * 60, 50 + row * 60)  # Espaciado entre los aliens
                self.all_sprites.add(alien)
                self.aliens_sprites.add(alien)

    def start_game(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(".\\assets\\music\\toby fox - UNDERTALE Soundtrack - 14 Heartache.mp3")
        pygame.mixer.music.play(loops=-1, start=0.0)
        pygame.mixer.music.set_volume(0.5)
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet(self.player.rect.centerx, self.player.rect.top)
                        self.all_sprites.add(bullet)
                        self.bullets_sprites.add(bullet)

            self.all_sprites.update()
            if pygame.sprite.spritecollide(self.player, self.aliens_sprites, False):
                self.game_over()


            for bullet in self.bullets_sprites:
                alien_hits = pygame.sprite.spritecollide(bullet, self.aliens_sprites, True)
                if alien_hits:
                    bullet.trigger_explosion()

            if not self.aliens_sprites:
                self.win_game()
                running = False

            self.screen.blit(self.fondo_juego, (0, 0))
            self.all_sprites.draw(self.screen)

            score_text = pygame.font.SysFont("Arial Black", 20).render(
                f"Aliens Restantes: {len(self.aliens_sprites)}",
                True, WHITE)
            self.screen.blit(score_text, (10, 10))

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def game_over(self):
        gameov = Game_over_screen()
        result = gameov.go_screen()

        if result == "restart":
            gameov.go_menu()
        elif result == "quit":
            gameov.go_exit()

    def win_game(self):
        wingame = Win_screen()

        result = wingame.go_screen()

        if result == "restart":
            wingame.go_menu()
        elif result == "quit":
            wingame.go_exit()
