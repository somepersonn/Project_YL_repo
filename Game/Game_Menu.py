import pygame

LABELS = ['Название', 'Новая игра', 'Продолжить', 'Достижения', 'Настройки', 'Выход']
pygame.init()
w, h = 800, 500
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
pygame.display.set_caption('Super Game')
font = pygame.font.Font(None, 25)

q = True
while q:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            q = False
    screen.fill((0,0,0))
    screen.blit(font.render(LABELS[0], 1, (255, 0, 0), (0, 0, 0)), (100, 100))
    pygame.draw.rect(screen, (123, 0, 123), (90, 90, 130, 30), 1)
    screen.blit(font.render(LABELS[1], 1, (255, 0, 0), (0, 0, 0)), (100, 150))
    pygame.draw.rect(screen, (123, 0, 123), (90, 140, 130, 30), 1)
    screen.blit(font.render(LABELS[2], 1, (255, 0, 0), (0, 0, 0)), (100, 200))
    pygame.draw.rect(screen, (123, 0, 123), (90, 190, 130, 30), 1)
    screen.blit(font.render(LABELS[3], 1, (255, 0, 0), (0, 0, 0)), (100, 250))
    pygame.draw.rect(screen, (123, 0, 123), (90, 240, 130, 30), 1)
    screen.blit(font.render(LABELS[4], 1, (255, 0, 0), (0, 0, 0)), (100, 300))
    pygame.draw.rect(screen, (123, 0, 123), (90, 290, 130, 30), 1)
    screen.blit(font.render(LABELS[5], 1, (255, 0, 0), (0, 0, 0)), (100, 350))
    pygame.draw.rect(screen, (123, 0, 123), (90, 340, 130, 30), 1)
    pygame.display.update()

pygame.quit()
