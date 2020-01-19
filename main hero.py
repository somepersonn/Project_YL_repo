import os
import random

import pygame

pygame.init()

size = width, height = 800, 600

screen = pygame.display.set_mode(size)

pygame.display.flip()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


screen_rect = (0, 0, width, height)


class FireBall(pygame.sprite.Sprite):
    """Фаерболлы. Что умеют:
    при попадании во врага убивают его и исчезают"""
    image = pygame.transform.scale(load_image("fireball.png", -1), (20, 20))

    def __init__(self, x, y, vector, *groups):
        super().__init__(*groups)
        self.image = FireBall.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.v = 20
        self.vector = vector

    def update(self, *args):
        if pygame.sprite.spritecollideany(self, enemy_group):
            self.kill()
        if not self.rect.colliderect(screen_rect):
            self.kill()
        else:
            if self.vector == 1:
                self.rect.x += self.v
            if self.vector == 2:
                self.rect.x -= self.v
            if self.vector == 3:
                self.rect.y -= self.v
            if self.vector == 4:
                self.rect.y += self.v


class MainHero(pygame.sprite.Sprite):
    """Класс главного героя. Что умеет:
    1. бегает
    2. стреляет фаерболлами"""
    image = load_image("hero.png", -1)

    def __init__(self, frames_right, frames_left, frames_stand_left, frames_stand_right, *groups):
        super().__init__(*groups)
        self.frames_right = frames_right
        self.frames_left = frames_left
        self.frames_stand_left = frames_stand_left
        self.frames_stand_right = frames_stand_right
        self.cur_frame = 0
        self.frame_count = 0
        self.image = self.frames_right[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
        self.vector = 1
        self.vector_left_right = 4
        self.vector_stand = 1

    def update(self, *args):
        if self.frame_count % 5 == 0:
            if self.vector_left_right == 1:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_right)
                self.image = self.frames_right[self.cur_frame]
            if self.vector_left_right == 2:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left)
                self.image = self.frames_left[self.cur_frame]
            if self.vector_left_right == 3:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_stand_left)
                self.image = self.frames_stand_left[self.cur_frame]
            if self.vector_left_right == 4:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_stand_right)
                self.image = self.frames_stand_right[self.cur_frame]
        buttons = pygame.key.get_pressed()
        if buttons[pygame.K_UP]:
            self.rect.y -= 1
            self.vector = 3
        if buttons[pygame.K_DOWN]:
            self.rect.y += 1
            self.vector = 4
        if buttons[pygame.K_RIGHT]:
            self.rect.x += 1
            self.vector = 1
            self.vector_left_right = 1
        if buttons[pygame.K_LEFT]:
            self.rect.x -= 1
            self.vector = 2
            self.vector_left_right = 2
        if not pygame.key.get_pressed()[pygame.K_DOWN] and not pygame.key.get_pressed()[pygame.K_UP] \
                and not pygame.key.get_pressed()[pygame.K_LEFT] and not pygame.key.get_pressed()[pygame.K_RIGHT]:
            if self.vector_left_right == 1:
                self.vector_left_right = 4
            if self.vector_left_right == 2:
                self.vector_left_right = 3
        self.frame_count += 1

    def fire(self):
        FireBall(self.rect.x, self.rect.y, self.vector, all_sprites, fireballs)


all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
fireballs = pygame.sprite.Group()

hero = MainHero([load_image("bomzh_vprapo_okonchat0.png", -1), load_image("bomzh_vprapo_okonchat1.png", -1),
                 load_image("bomzh_vprapo_okonchat2.png", -1), load_image("bomzh_vprapo_okonchat3.png", -1),
                 load_image("bomzh_vprapo_okonchat4.png", -1), load_image("bomzh_vprapo_okonchat5.png", -1),
                 load_image("bomzh_vprapo_okonchat6.png", -1), load_image("bomzh_vprapo_okonchat7.png", -1)],
                [load_image("bomzh_vlevo_okonchat0.png", -1), load_image("bomzh_vlevo_okonchat1.png", -1),
                 load_image("bomzh_vlevo_okonchat2.png", -1), load_image("bomzh_vlevo_okonchat3.png", -1),
                 load_image("bomzh_vlevo_okonchat4.png", -1), load_image("bomzh_vlevo_okonchat5.png", -1),
                 load_image("bomzh_vlevo_okonchat6.png", -1), load_image("bomzh_vlevo_okonchat7.png", -1)],
                [load_image("stait_vlevo00.png", -1), load_image("stait_vlevo01.png", -1),
                 load_image("stait_vlevo02.png", -1),
                 load_image("stait_vlevo03.png", -1), load_image("stait_vlevo04.png", -1),
                 load_image("stait_vlevo05.png", -1),
                 load_image("stait_vlevo06.png", -1), load_image("stait_vlevo07.png", -1),
                 load_image("stait_vlevo08.png", -1)],
                [load_image("stait_vpravo00.png", -1), load_image("stait_vpravo01.png", -1), load_image(
                    "stait_vpravo02.png", -1),
                 load_image("stait_vpravo03.png", -1), load_image("stait_vpravo04.png", -1), load_image(
                    "stait_vpravo05.png", -1),
                 load_image("stait_vpravo06.png", -1), load_image("stait_vpravo07.png", -1), load_image(
                    "stait_vpravo08.png", -1)],
                all_sprites)

clock = pygame.time.Clock()
running = True
fps = 60
while running:
    screen.fill(pygame.Color("white"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hero.fire()

    all_sprites.update(event)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

