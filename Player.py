import pygame
import Game
WIDTH, HEIGHT = 500,500
PLAYER_SPEED = 2
GREEN = (0,255,0)


player_imagen = (
    pygame.image.load(".\\assets\\images\\Ship\\ship_left1.png"),
    pygame.image.load(".\\assets\\images\\Ship\\ship_left2.png"),
    pygame.image.load(".\\assets\\images\\Ship\\ship_middle.png"),
    pygame.image.load(".\\assets\\images\\Ship\\ship_right2.png"),
    pygame.image.load(".\\assets\\images\\Ship\\ship_right1.png")
)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_frames = player_imagen
        self.image = self.player_frames[2]
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = PLAYER_SPEED
        self.animation_state = "normal"


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.animation_state = "left"
        elif keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
            self.animation_state = "right"
        else:
            self.animation_state = "normal"


        self.update_animation()



    def update_animation(self):
        if self.animation_state == "left":
            self.image = self.player_frames[0] if pygame.time.get_ticks() % 200 < 100 else self.player_frames[1]
        elif self.animation_state == "right":
            self.image = self.player_frames[3] if pygame.time.get_ticks() % 200 < 100 else self.player_frames[4]
        else:
            self.image = self.player_frames[2]



