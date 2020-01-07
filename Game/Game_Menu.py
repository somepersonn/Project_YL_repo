import pygame
LABELS = ['Название', 'Новая игра', 'Продолжить', 'Достижения', 'Настройки', 'Выход']

Frases = ['Никто из нас уже не сможет сказать, как выглядят трава, деревья и реки.',
          'Раньше эти края были прекрасной зелёной долиной, в которой все жили в радости и достатке',
          '*Показываем картинку деревни*',
          'Но всё изменилось, когда один из нас, возомнивший себя всемогущим, назвал себя Повелителем этого мира и бросил вызов Титанам',
          'Он явно переоценил свои силы и за его надменность поплатились все мы...',
          '*Показываем картину пустоши, выжженной земли, разорённой деревни и тд*',
          'Звали его ..... (Надо придумать). После его поединка с Титанами никто из нашего племени больше не видел его, ',
          'Скорее всего его заточили в ... - тюрьму, откуда нет выхода. Ах, да. Забыл представиться.',
          'Меня зовут ... (Тут вылазит окно, пользователь вводит имя персонажа)',
          'Я его сын. (Вот это поворот)',
          'И я во что бы то ни стало должен найти своего отца и с его помощью восстановить мир в наших землях.',
          'Для этого мне нужно спуститься в подземелья ... и освободить его, чтобы после с его помощью выкрасть у Титанов',
          '... - древний, могущественный артефакт, дарующий владельцу власть над всем/всей ... (Название мира)',
          'Итак, да начнётся приключение.',
          '*Показываем вход в ту тюрьму, перс заходит в неё*']

pygame.init()
w, h = 800, 500
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
pygame.display.set_caption('Super Game')
font = pygame.font.Font(None, 25)

def static_labels():
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

font = pygame.font.Font(None, 15)
K = -1
Flag = False
run = True

def intro():
    global run, Flag, K
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # При нажатии ЛКМ, меняется фраза.
                if event.button == 1:
                    if Flag == False and K < 14:  # Задаём максимум, равный максимальному индексу в списке Frases
                        K += 1
                        Flag = True
                    elif Flag == True and K < 14:  # Тута тоже.
                        K += 1
                    else:
                        Flag = False
                        K = -1
        screen.fill((0, 0, 0))
        if Flag:
            if K not in [2, 5]:
                screen.blit(font.render(Frases[K], 1, (255, 0, 0), (0, 0, 0)), (0, 255))
            elif K == 2:
                screen.blit(font.render(Frases[K], 1, (255, 0, 0), (0, 0, 0)), (0, 255))
            elif K == 5:
                pass
        pygame.draw.line(screen, (123, 0, 123), [0, 250], [750, 250], 1)

        pygame.display.flip()

    pygame.quit()

w = False
q = True

while q:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            q = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if event.button == 1 and (90 < x < 220) and (140 < y < 170):
                w = True
    screen.fill((0,0,0))
    static_labels()
    if w:
        intro()
    pygame.display.update()

pygame.quit()
