import pygame

WIDTH, HEIGHT = 500,500 # Tamaño de la ventana del juego
PLAYER_SPEED = 2 # Velocidad del jugador


# Cargamos las imágenes del jugador ( su nave ) en distintas posiciones
player_imagen = (
    pygame.image.load(".\\assets\\images\\Ship\\ship_left1.png"),
    pygame.image.load(".\\assets\\images\\Ship\\ship_left2.png"),
    pygame.image.load(".\\assets\\images\\Ship\\ship_middle.png"),
    pygame.image.load(".\\assets\\images\\Ship\\ship_right2.png"),
    pygame.image.load(".\\assets\\images\\Ship\\ship_right1.png")
)

# Clase jugador que hereda de pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # Llamamos al constructor de Sprite
        self.player_frames = player_imagen # Asignamos las imágenes del jugador a una lista llamada player_frames
        self.image = self.player_frames[2] # Inicialmente mostramos la imagen del centro
        self.rect = self.image.get_rect() # Obtenemos el rect que rodea la imagen para poder moverla
        self.rect.centerx = WIDTH // 2 # Centrado en el eje x
        self.rect.bottom = HEIGHT - 10 # El jugador se sitúa cerca del fondo de la pantalla
        self.speed = PLAYER_SPEED # Velocidad del jugador
        self.animation_state = "normal" # Estado de la animación


    def update(self):
        keys = pygame.key.get_pressed() # Obtenemos el estado de las teclas presionadas

        # Si la tecla izquierda está presionada y el jugador no ha llegado al borde izquierdo
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed # Movemos al jugador a la izquierda
            self.animation_state = "left" # Cambiamos el estado de animacion
        # Si la tecla derecha está presionada y el jugador no ha llegado al borde derecho
        elif keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed # Movemos el jugador a la derecha
            self.animation_state = "right" # Cambiamos el estado de la animacion de nuevo
        else:
            self.animation_state = "normal" # Si no se presionan teclas, volveremos al estado por defecto

        # Actualizamos la animación
        self.update_animation()



    def update_animation(self):
        # Animación cuando el jugador se mueve hacia la izquierda
        if self.animation_state == "left":
            # Cambia entre las dos imágenes de la izquierda cada 200ms
            self.image = self.player_frames[0] if pygame.time.get_ticks() % 200 < 100 else self.player_frames[1]
        # Animación cando el jugador se mueve hacia la derecha
        elif self.animation_state == "right":
            # Cambia entre las dos imágenes de la derecha cada 200ms
            self.image = self.player_frames[3] if pygame.time.get_ticks() % 200 < 100 else self.player_frames[4]
        # Estado por defecto ( cuando no se mueve )
        else:
            self.image = self.player_frames[2]



