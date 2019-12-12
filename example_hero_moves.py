import os
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


class MainHero(pygame.sprite.Sprite):
    image = load_image("creature.png", -1)

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = MainHero.image
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
        self.bull = True

    def update(self, *args):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.y -= 10
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.y += 10
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += 10
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= 10


all_sprites = pygame.sprite.Group()

hero = MainHero(all_sprites)

clock = pygame.time.Clock()
running = True
fps = 60
s = []
while running:
    screen.fill(pygame.Color("white"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         pos = event.pos
        #         s.append([pos, v_x, v_y])
        #         pygame.draw.circle(screen, pygame.Color("red"), pos, 10)
        #         bull = True

    all_sprites.update(event)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(fps)