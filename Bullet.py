import pygame


BULLET_SPEED = 3 # Velocidad de la bala

# Cargamos las imágenes para las balas en frames
bullet_img = (
    pygame.image.load(".\\assets\\images\\Shot\\shot2_1.png"),
    pygame.image.load(".\\assets\\images\\Shot\\shot2_2.png"),
    pygame.image.load(".\\assets\\images\\Shot\\shot2_3.png"),
    pygame.image.load(".\\assets\\images\\Shot\\shot2_asset.png")
)
# Cargamos las imágenes para la explosión de la bala
bullet_explosion = (
    pygame.image.load(".\\assets\\images\\Shot\\shot2_exp1.png"),
    pygame.image.load(".\\assets\\images\\Shot\\shot2_exp2.png"),
    pygame.image.load(".\\assets\\images\\Shot\\shot2_exp3.png"),
    pygame.image.load(".\\assets\\images\\Shot\\shot2_exp4.png")
)


# Definimos la clase Bullet que hereda de pygame.sprite.Sprite
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__() # Llamamos al constructor de Sprite
        self.bullet_frames = bullet_img # Asignamos las imágenes de la bala
        self.bullet_explosion_frames = bullet_explosion # Asignamos las imágenes de la explosión
        self.image = self.bullet_frames[0] # Inicializamos la imagen de la bala
        self.rect = self.image.get_rect() # Obtenemos el rect que rodea la bala
        self.rect.centerx = x # Establecemos la posición inicial de la bala en el eje x
        self.rect.bottom = y # Establecemos la posición inicial de la bala en el eje y
        self.speed = BULLET_SPEED # Asignamos la velocidad de la bala
        self.frame = 0 # Frame de la animación
        self.animation_state = "normal" # Estado de la animación

    def update(self):
        # Si la animación está por defecto (la bala se está moviendo)
        if self.animation_state == "normal":
            # Actualizamos el frame de la animación, lo que permite cambiar de imagen
            self.frame = (self.frame + 1) % 50 # La animación avanza a través de los frames
            self.image = self.bullet_frames[self.frame // 100] # Actualizamos la imagen de la bala en función del frame

            self.rect.y -= self.speed # Movemos la bala hacia arriba (disparo)

            # Si la bala sale de la pantalla (está fuera de los límites), la eliminamos
            if self.rect.bottom < 0:
                self.kill()
        # Si la animación está en estado de explosión ( está fuera de los límites )
        elif self.animation_state == "explosion":

            self.frame = (self.frame + 1) % 20 # Actualizamos el frame de la explosión
            self.image = self.bullet_explosion_frames[self.frame // 10] # Actualizamos la imagen de la explosión
            # Cuando el frame llegue a cero significará que la explosión termina y eliminamos la bala
            if self.frame == 0:
                self.kill()

    # Este método se llama para activar la animación de la explosión
    def trigger_explosion(self):
        self.animation_state = "explosion"  # Cambiamos el estado de la animación a explosion
        self.frame = 0 # Reseteamos el frame a 0 para comenzar desde el inicio de la animación