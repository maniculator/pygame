# coding: utf8
import pygame
import random
import sys
import time
# задааем размер окна, создаем окно размера size
size = [400, 460]
window = pygame.display.set_mode(size)
# задаем имя - в кавычках, т.к. текст - это строка
pygame.display.set_caption('My second file')

screen = pygame.Surface(size)
score = pygame.Surface([400, 60])
f = 0
z = 0
count = 0
csh = 0
step = 3
flag100 = 100

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))


def load_menu():
    items = [(150, 150, 'Start', ([12, 184, 252]), ([76, 12, 252]), 0),
             (150, 250, 'Finish', ([252, 12, 96]), ([96, 12, 252]), 1)]

    pygame.key.set_repeat(1, 1)
    pygame.mouse.set_visible(True)

    done = False
    item = 0
    while not done:
        # Заливка всех поверхностей
        screen.fill([255, 255, 255])
        score.fill([229, 229, 229])
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if item == 0:
                    done = True
                elif item == 1:
                    pygame.quit()
                    sys.exit()

        pointer = pygame.mouse.get_pos()
        for i in items:
            if pointer[0] > i[0] and pointer[0] < i[0] + 155 and pointer[1] > i[1] and pointer[1] < i[1] + 50:
                item = i[5]

        for i in items:
            if item == i[5]:
                screen.blit(gf.render(i[2], 1, i[4]), [i[0], i[1] - 40])
            else:
                screen.blit(gf.render(i[2], 1, i[3]), [i[0], i[1] - 40])

        window.blit(score, [0, 0])
        window.blit(screen, [0, 40])
        pygame.display.flip()


def you_win():
    done = False
    pygame.font.init()
    gf = pygame.font.Font(None, 50)
    while not done:
        screen.fill([255, 255, 255])
        score.fill([229, 229, 229])
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    winner = gf.render('YOU ARE THE WINNER!', 1, [0, 255, 0])
    screen.blit(winner, [50, 150])
    window.blit(screen, [0, 60])
    window.blit(score, [0, 0])
    pygame.display.flip()
    pygame.time.delay(50)
    pygame.display.flip()


def loser():
    done = False
    pygame.font.init()
    gf = pygame.font.Font(None, 50)
    while not done:
        screen.fill([255, 255, 255])
        score.fill([229, 229, 229])
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        lose = gf.render('YOU ARE THE LOSER!', 1, [255, 0, 0])
        screen.blit(lose, [60, 150])
        window.blit(screen, [0, 60])
        window.blit(score, [0, 0])
        pygame.display.flip()
        pygame.time.delay(50)
        pygame.display.flip()


def Intersect(s1_x, s2_x, s1_y, s2_y):
    if ((s1_x > s2_x - 50) and (s1_x < s2_x + 50) and (s1_y > s2_y - 50) and (s1_y < s2_y + 50)):
        return 1
    else:
        return 0


# создание персонажей
# герой
hero = Sprite(random.randint(0, 360), random.randint(250, 360), 'yellow.jpg')

# переменные-"переключатели" движения для героя
hero.right = True
hero.up = True
# враг
enemy = Sprite(200, 10, 'purple.png')
# переменные-"переключатели" движения для врага
enemy.right = True
enemy.up = False
gru = Sprite(200, 10, 'gru.png')
# переменные-"переключатели" движения для врага
gru.right = False
heart = Sprite(280, 360, 'heart.png')
heart1 = Sprite(320, 360, 'heart.png')
heart2 = Sprite(360, 360, 'heart.png')
heart3 = Sprite(200, 360, 'heart.png')
heart4 = Sprite(240, 360, 'heart.png')
heart5 = Sprite(280, 360, 'heart.png')
heart6 = Sprite(320, 360, 'heart.png')
heart7 = Sprite(360, 360, 'heart.png')
shot = Sprite(450, 450, 'banana.png')
shot1 = Sprite(0, 370, 'banana.png')
shot2 = Sprite(15, 370, 'banana.png')
shot3 = Sprite(30, 370, 'banana.png')
shot.up = True
nshot = Sprite(450, 450, 'pineapple.jpg')
nshot1 = Sprite(60, 370, 'pineapple.jpg')
nshot2 = Sprite(45, 370, 'pineapple.jpg')
nshot3 = Sprite(30, 370, 'pineapple.jpg')
nshot4 = Sprite(15, 370, 'pineapple.jpg')
nshot5 = Sprite(0, 370, 'pineapple.jpg')
nshot.up = True
pygame.key.set_repeat(1, 1)
running = True
pygame.font.init()
gf = pygame.font.Font(None, 50)
load_menu()

while running:
    # обработка событий
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                if hero.x >= 0:
                    hero.x -= 1
            if e.key == pygame.K_RIGHT:
                if hero.x <= 360:
                    hero.x += 1
            if e.key == pygame.K_UP:
                if hero.y >= 250:
                    hero.y -= 1
            if e.key == pygame.K_DOWN:
                if hero.y <= 360:
                    hero.y += 1
            if e.key == pygame.K_SPACE:
                if shot.y >= 249:
                    #if count <= 2:
                    shot.y = hero.y
                    shot.x = hero.x
                    shot.up = False
                if nshot.y >= 249:
                    #if count > 2:
                    nshot.y = hero.y
                    nshot.x = hero.x
                    nshot.up = False


    # задайте фоновый цвет
    screen.fill([255, 255, 255])
    score.fill([229, 229, 229])

    # движение персонажей
    if enemy.right == True:
        if enemy.x <= 360:
            enemy.x += step
        else:
            enemy.right = False
    if enemy.right == False:
        if enemy.x >= 0:
            enemy.x -= step
        else:
            enemy.right = True
    if shot.up == False:
        if shot.y >= -50:
            shot.y -= 20
        else:
            shot.up = True
            z = 1
    if shot.up == True:
        shot.x = 450
        shot.y = 450
        f = 0
    if gru.right == True:
        if gru.x <= 360:
            gru.x += step
        else:
            gru.right = False
    if gru.right == False:
        if gru.x >= 0:
            gru.x -= step
        else:
            gru.right = True
    if nshot.up == False:
        if nshot.y >= -50:
            nshot.y -= 20
        else:
            nshot.up = True
            z = 1
    if shot.up == True:
        nshot.x = 450
        nshot.y = 450
        f = 0

    # столкновение персонажей
    if Intersect(shot.x, enemy.x, shot.y + 40, enemy.y):
        shot.up = True
        enemy.up = False
        enemy.x = random.randint(0, 360)
        step += 1
        if f == 0:
            count += 1
            f = 1
    elif shot.y < 0:
        if count <= 2:
            count -= 1
            shot.up = True
            z = 1
    if z == 1:
        csh += 1
        z = 0
    if Intersect(nshot.x, gru.x, nshot.y + 40, gru.y):
        nshot.up = True
        gru.up = False
        gru.x = random.randint(0, 360)
        step += 1
        if f == 0:
            count += 1
            f = 1
    elif nshot.y < 0:
        count -= 1
        nshot.up = True
        z = 1
    if z == 1:
        csh += 1
        z = 0
    if count == 1:
        heart.x += 50
        heart.y += 50
    if count == 2:
        heart1.x += 50
        heart1.y += 50
    if count == 3 and flag100 == 100:
        heart2.x += 50
        heart2.y += 50
        screen.fill([255, 255, 255])
        score.fill([229, 229, 229])
        winner = gf.render('you are the winner', 1, [0, 0, 0])
        screen.blit(winner, [50, 150])
        window.blit(screen, [0, 60])
        window.blit(score, [0, 0])
        pygame.time.delay(5)
        pygame.display.flip()
        time.sleep(3)
        flag100 = -100
    if count == 4:
        heart3.x += 50
        heart3.y += 50
    if count == 5:
        heart4.x += 50
        heart4.y += 50
    if count == 6:
        heart5.x += 50
        heart5.y += 50
    if count == 7:
        heart6.x += 50
        heart6.y += 50
    if count == 8:
        heart7.x += 50
        heart7.y += 50
        you_win()

    if csh == 1:
        shot1.x += 100
        shot1.y += 100
    if csh == 2:
        shot2.x += 100
        shot2.y += 100
    if csh == 3:
        shot3.x += 100
        shot3.y += 100
    if csh == 4:
        nshot1.x += 100
        nshot1.y += 100
    if csh == 5:
        nshot2.x += 100
        nshot2.y += 100
    if csh == 6:
        nshot3.x += 100
        nshot3.y += 100
    if csh == 7:
        nshot4.x += 100
        nshot4.y += 100
    if csh == 8:
        nshot5.x += 100
        nshot5.y += 100
        time.sleep(1)
        loser()

    # отображение персонажей
    hero.render()
    if count <= 2:
        enemy.render()
        shot.render()
        shot1.render()
        shot2.render()
        shot3.render()
        heart.render()
        heart1.render()
        heart2.render()
    elif count > 2:
        gru.render()
        nshot.render()
        nshot1.render()
        nshot2.render()
        nshot3.render()
        nshot4.render()
        nshot5.render()
        heart3.render()
        heart4.render()
        heart5.render()
        heart6.render()
        heart7.render()
    text = gf.render('Счет: ' + str(count), 1, [0, 0, 0])

    # отображение окна
    score.blit(text, [10, 10])
    window.blit(screen, [0, 60])
    window.blit(score, [0, 0])
    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()