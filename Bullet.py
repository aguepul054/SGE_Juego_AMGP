import pygame


BULLET_SPEED = 3
bullet_img = (
    pygame.image.load(".\\assets\\images\\Shot\\shot2_1.png"),
    pygame.image.load(".\\assets\\images\\Shot\\shot2_2.png"),
    pygame.image.load(".\\assets\\images\\Shot\\shot2_3.png"),
    pygame.image.load(".\\assets\\images\\Shot\\shot2_asset.png")
)

bullet_explosion = (
    pygame.image.load(".\\assets\\images\\Shot\\shot2_exp1.png"),
    pygame.image.load(".\\assets\\images\\Shot\\shot2_exp2.png"),
    pygame.image.load(".\\assets\\images\\Shot\\shot2_exp3.png"),
    pygame.image.load(".\\assets\\images\\Shot\\shot2_exp4.png")
)



class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.bullet_frames = bullet_img
        self.bullet_explosion_frames = bullet_explosion
        self.image = self.bullet_frames[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = BULLET_SPEED
        self.frame = 0
        self.animation_state = "normal"

    def update(self):
        if self.animation_state == "normal":
            self.frame = (self.frame + 1) % 50
            self.image = self.bullet_frames[self.frame // 100]

            self.rect.y -= self.speed
            if self.rect.bottom < 0:
                self.kill()

        elif self.animation_state == "explosion":

            self.frame = (self.frame + 1) % 20
            self.image = self.bullet_explosion_frames[self.frame // 10]

            if self.frame == 0:
                self.kill()
    def trigger_explosion(self):
        self.animation_state = "explosion"
        self.frame = 0