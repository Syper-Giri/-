import pygame
import pygame as pg


# собственно делает кнопки
class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = pg.font.Font(None, 50).render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


def myFunction():
    pg.quit()


def intersection(x1y1, x2y2, x3y3, x4y4):
    try:
        px = ((x1y1[0] * x2y2[1] - x1y1[1] * x2y2[0]) * (x3y3[0] - x4y4[0]) - (x1y1[0] - x2y2[0]) * (
                x3y3[0] * x4y4[1] - x3y3[1] * x4y4[0])) / (
                     (x1y1[0] - x2y2[0]) * (x3y3[1] - x4y4[1]) - (x1y1[1] - x2y2[1]) * (x3y3[0] - x4y4[0]))
        py = ((x1y1[0] * x2y2[1] - x1y1[1] * x2y2[0]) * (x3y3[1] - x4y4[1]) - (x1y1[1] - x2y2[1]) * (
                x3y3[0] * x4y4[1] - x3y3[1] * x4y4[0])) / (
                     (x1y1[0] - x2y2[0]) * (x3y3[1] - x4y4[1]) - (x1y1[1] - x2y2[1]) * (x3y3[0] - x4y4[0]))
    except ZeroDivisionError:
        px = None
        py = None
    return px, py


def start_the_graph():
    global objects

    objects = []

    input_box = pg.Rect(100, 100, 90, 50)  # размер прямоугольника
    input_box2 = pg.Rect(300, 100, 140, 50)  # размер прямоугольника
    input_box3 = pg.Rect(500, 100, 140, 50)  # размер прямоугольника
    input_box4 = pg.Rect(800, 100, 140, 50)  # размер прямоугольника

    screen.fill((20, 80, 20))  # цвет фона
    font = pg.font.Font(None, 50)  # шрифт
    font2 = pg.font.Font(None, 40)  # шрифт текста
    font3 = pg.font.Font(None, 25)  # шрифт текста
    all_sprites = pygame.sprite.Group()  # группа спрайтов

    color = color_inactive
    color2 = color_inactive
    color3 = color_inactive
    color4 = color_inactive

    # оси координат
    pg.draw.line(screen, (0, 0, 0), [weight / 8, height / 2], [7 * weight / 8, height / 2], 3)  # ось x
    pg.draw.line(screen, (0, 0, 0), [weight / 2, height / 4], [weight / 2, 3 * height / 4], 3)  # ось y

    active = False
    active2 = False
    active3 = False
    active4 = False

    text = '_ _ _'
    text2 = '_ _ _ _ _'
    text3 = '_ _ _ _ _'
    text4 = '_ _ _ _ _'
    done = True

    k = 30  # константа увеличения
    customButton2 = Button(weight - 200, height - 200, 150, 70, 'Заново', main, True)
    customButton = Button(weight - 200, height - 120, 150, 70, 'Выход', myFunction, True)

    while done:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = False
            for object in objects:
                object.process()
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                if input_box2.collidepoint(event.pos):
                    active2 = not active
                else:
                    active2 = False
                if input_box3.collidepoint(event.pos):
                    active3 = not active
                else:
                    active3 = False
                if input_box4.collidepoint(event.pos):
                    active4 = not active
                else:
                    active4 = False

                color = color_active if active else color_inactive
                color2 = color_active if active2 else color_inactive
                color3 = color_active if active3 else color_inactive
                color4 = color_active if active3 else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        if text == 'р а с':
                            pg.draw.line(screen, (0, 0, 0), [weight / 2 - 30, height / 4 - 30],
                                         [weight / 2, height / 4], 3)
                            pg.draw.line(screen, (0, 0, 0), [weight / 2, height / 4],
                                         [weight / 2 + 30, height / 4 - 30], 3)

                            pg.draw.line(screen, (0, 0, 0), [weight / 2 + 30, 3 * height / 4 + 30],
                                         [weight / 2, 3 * height / 4], 3)
                            pg.draw.line(screen, (0, 0, 0), [weight / 2, 3 * height / 4],
                                         [weight / 2 - 30, 3 * height / 4 + 30], 3)
                        elif text == 'с о б':
                            pg.draw.line(screen, (0, 0, 0), [weight / 2 - 30, height / 4 + 30],
                                         [weight / 2, height / 4], 3)
                            pg.draw.line(screen, (0, 0, 0), [weight / 2, height / 4],
                                         [weight / 2 + 30, height / 4 + 30], 3)

                            pg.draw.line(screen, (0, 0, 0), [weight / 2 + 30, 3 * height / 4 - 30],
                                         [weight / 2, 3 * height / 4], 3)
                            pg.draw.line(screen, (0, 0, 0), [weight / 2, 3 * height / 4],
                                         [weight / 2 - 30, 3 * height / 4 - 30], 3)
                    else:
                        text = text.replace('_', event.unicode, 1)

                elif active2:
                    if event.key == pg.K_RETURN:
                        text2 = text2.replace('_', '0')
                        print(text2)
                    else:
                        text2 = text2.replace('_', event.unicode, 1)

                elif active3:
                    if event.key == pg.K_RETURN:
                        text3 = text3.replace('_', '0')
                        print(text3)
                        pg.draw.line(screen, (80, 0, 0),
                                     [weight / 2 - int(''.join(text3.split())[2:]) // 100 * k,
                                      height / 2 - int(''.join(text2.split())[2:]) / 10 * k],
                                     [weight / 2 - int(''.join(text3.split())[2:]) // 100 * k, height / 2],
                                     3)
                        pg.draw.line(screen, (80, 0, 0),
                                     [weight / 2 - int(''.join(text3.split())[2:]) // 100 * k,
                                      height / 2 - int(''.join(text2.split())[2:]) / 10 * k],
                                     [weight / 2 - int(''.join(text3.split())[2:]) // 100 * k + 8,
                                      height / 2 - int(''.join(text2.split())[2:]) / 10 * k + 8],
                                     3)
                        pg.draw.line(screen, (80, 0, 0),
                                     [weight / 2 - int(''.join(text3.split())[2:]) // 100 * k,
                                      height / 2 - int(''.join(text2.split())[2:]) / 10 * k],
                                     [weight / 2 - int(''.join(text3.split())[2:]) // 100 * k - 8,
                                      height / 2 - int(''.join(text2.split())[2:]) / 10 * k + 8],
                                     3)
                        text1 = font3.render('А', True,
                                             (80, 0, 0))
                        screen.blit(text1, (weight / 2 - int(''.join(text3.split())[2:]) // 100 * k - 20,
                                            height / 2 - int(''.join(text2.split())[2:]) / 10 * k))
                        text1 = font3.render('B', True,
                                             (80, 0, 0))
                        screen.blit(text1,
                                    (weight / 2 - int(''.join(text3.split())[2:]) // 100 * k - 20, height / 2 - 20))

                    else:
                        text3 = text3.replace('_', event.unicode, 1)

                elif active4:
                    if event.key == pg.K_RETURN:
                        text4 = text4.replace('_', '0')
                        print(text4)

                        # строим фокус
                        pg.draw.line(screen, (0, 0, 0),
                                     [weight / 2 - int(''.join(text4.split())[2:]) // 100 * k, height / 2 + 10],
                                     [weight / 2 - int(''.join(text4.split())[2:]) // 100 * k, height / 2 - 10],
                                     3)
                        pg.draw.line(screen, (0, 0, 0),
                                     [weight / 2 + int(''.join(text4.split())[2:]) // 100 * k, height / 2 + 10],
                                     [weight / 2 + int(''.join(text4.split())[2:]) // 100 * k, height / 2 - 10],
                                     3)

                        text1 = font2.render('F', True,
                                             (0, 0, 0))
                        screen.blit(text1, (weight / 2 - int(''.join(text4.split())[2:]) // 100 * k, height / 2 + 20))

                        pg.draw.line(screen, (0, 0, 0),
                                     [weight / 2 - 2 * int(''.join(text4.split())[2:]) // 100 * k, height / 2 + 10],
                                     [weight / 2 - 2 * int(''.join(text4.split())[2:]) // 100 * k, height / 2 - 10],
                                     3)
                        pg.draw.line(screen, (0, 0, 0),
                                     [weight / 2 + 2 * int(''.join(text4.split())[2:]) // 100 * k, height / 2 + 10],
                                     [weight / 2 + 2 * int(''.join(text4.split())[2:]) // 100 * k, height / 2 - 10],
                                     3)

                        pg.draw.line(screen, (0, 0, 0),
                                     [weight / 2 - 3 * int(''.join(text4.split())[2:]) // 100 * k, height / 2 + 10],
                                     [weight / 2 - 3 * int(''.join(text4.split())[2:]) // 100 * k, height / 2 - 10],
                                     3)
                        pg.draw.line(screen, (0, 0, 0),
                                     [weight / 2 + 3 * int(''.join(text4.split())[2:]) // 100 * k, height / 2 + 10],
                                     [weight / 2 + 3 * int(''.join(text4.split())[2:]) // 100 * k, height / 2 - 10],
                                     3)

                        # РИСУЕМ САМ ХОД ЛУЧА НАКОНЕЦ_ТО (ура ура)

                        # стрелочка до оси y
                        pg.draw.line(screen, (0, 0, 80),
                                     [weight / 2 - int(''.join(text3.split())[2:]) // 100 * k,
                                      height / 2 - int(''.join(text2.split())[2:]) / 10 * k],
                                     [weight / 2, height / 2 - int(''.join(text2.split())[2:]) / 10 * k],
                                     3)
                        pg.draw.line(screen, (0, 0, 80),
                                     [weight / 2 - (int(''.join(text3.split())[2:]) // 100 * k) // 2,
                                      height / 2 - int(''.join(text2.split())[2:]) / 10 * k],
                                     [weight / 2 - (int(''.join(text3.split())[2:]) // 100 * k) // 2 - 10,
                                      height / 2 - int(''.join(text2.split())[2:]) / 10 * k - 10],
                                     3)
                        pg.draw.line(screen, (0, 0, 80),
                                     [weight / 2 - (int(''.join(text3.split())[2:]) // 100 * k) // 2,
                                      height / 2 - int(''.join(text2.split())[2:]) / 10 * k],
                                     [weight / 2 - (int(''.join(text3.split())[2:]) // 100 * k) // 2 - 10,
                                      height / 2 - int(''.join(text2.split())[2:]) / 10 * k + 10],
                                     3)

                        if text == 'с о б':
                            a = intersection(
                                (weight / 2, height // 2),
                                (weight / 2 + int(''.join(text3.split())[2:]) // 100 * k * 4,
                                 height / 2 + int(''.join(text2.split())[2:]) / 10 * k * 4),
                                (weight / 2 + int(''.join(text4.split())[2:]) // 100 * k,
                                 height // 2),
                                (weight / 2 + int(''.join(text4.split())[2:]) // 100 * k * 5,
                                 height / 2 + int(''.join(text2.split())[2:]) / 10 * k * 4))
                            print(a[0], a[1])

                            # стрелочка после оси y
                            pg.draw.line(screen, (0, 0, 80),
                                         [weight / 2, height / 2 - int(''.join(text2.split())[2:]) / 10 * k],
                                         [a[0], a[1]],
                                         3)
                            # линия до центра
                            pg.draw.line(screen, (0, 0, 80),
                                         [a[0], a[1]],
                                         [weight / 2 - int(''.join(text3.split())[2:]) // 100 * k,
                                          height / 2 - int(''.join(text2.split())[2:]) / 10 * k],
                                         3)
                            pg.draw.line(screen, (80, 0, 0),
                                         [a[0], a[1]],
                                         [a[0], height / 2],
                                         3)
                            if weight / 2 - int(''.join(text3.split())[2:]) // 100 * k < a[0]:
                                pg.draw.line(screen, (80, 0, 0),
                                             [a[0], a[1]],
                                             [a[0] - 8, a[1] - 8],
                                             3)
                                pg.draw.line(screen, (80, 0, 0),
                                             [a[0], a[1]],
                                             [a[0] + 8, a[1] - 8],
                                             3)

                                text1 = font3.render("А'", True,
                                                     (80, 0, 0))
                                screen.blit(text1, (a[0] + 8, height / 2 + 8))
                                text1 = font3.render("B'", True,
                                                     (80, 0, 0))
                                screen.blit(text1,
                                            (a[0], a[1] + 8))

                            elif weight / 2 - int(''.join(text3.split())[2:]) // 100 * k > a[0]:
                                pg.draw.line(screen, (80, 0, 0),
                                             [a[0], a[1]],
                                             [a[0] + 8, a[1] + 8],
                                             3)
                                pg.draw.line(screen, (80, 0, 0),
                                             [a[0], a[1]],
                                             [a[0] - 8, a[1] + 8],
                                             3)

                                text1 = font3.render("B'", True,
                                                     (80, 0, 0))
                                screen.blit(text1, (a[0] - 20, height / 2 - 20))
                                text1 = font3.render("A'", True,
                                                     (80, 0, 0))
                                screen.blit(text1,
                                            (a[0] - 20, a[1] - 20))
                        elif text == 'р а с':
                            a = intersection((weight / 2 - int(''.join(text3.split())[2:]) // 100 * k,
                                              height / 2 - int(''.join(text2.split())[2:]) / 10 * k),
                                             (weight / 2 + int(''.join(text3.split())[2:]) // 100 * k,
                                              height / 2 + int(''.join(text2.split())[2:]) / 10 * k),
                                             (weight / 2 - int(''.join(text4.split())[2:]) // 100 * k, height / 2),
                                             (weight / 2 + int(''.join(text3.split())[2:]) // 100 * k,
                                              height / 2 - int(''.join(text2.split())[2:]) / 10 * k * 2))

                            pg.draw.line(screen, (0, 0, 80),
                                         [weight / 2 - int(''.join(text3.split())[2:]) // 100 * k,
                                          height / 2 - int(''.join(text2.split())[2:]) / 10 * k],
                                         [weight / 2 + int(''.join(text3.split())[2:]) // 100 * k,
                                          height / 2 + int(''.join(text2.split())[2:]) / 10 * k],
                                         3)

                            pg.draw.line(screen, (0, 0, 80),
                                         [weight / 2 - int(''.join(text4.split())[2:]) // 100 * k, height / 2],
                                         [weight / 2 + int(''.join(text3.split())[2:]) // 100 * k,
                                          height / 2 - int(''.join(text2.split())[2:]) / 10 * k * 2],
                                         3)

                            pg.draw.line(screen, (80, 0, 0),
                                         [a[0], a[1]], [a[0], height / 2],
                                         3)
                            pg.draw.line(screen, (80, 0, 0),
                                         [a[0], a[1]], [a[0] - 8, a[1] + 8],
                                         3)
                            pg.draw.line(screen, (80, 0, 0),
                                         [a[0], a[1]], [a[0] + 8, a[1] + 8],
                                         3)

                            text1 = font3.render("А'", True,
                                                 (80, 0, 0))
                            screen.blit(text1,
                                        (a[0] - 20, a[1] - 8))
                            text1 = font3.render("B'", True,
                                                 (80, 0, 0))
                            screen.blit(text1,
                                        (a[0] - 8, height / 2 + 8))

                    else:
                        text4 = text4.replace('_', event.unicode, 1)

        txt_surface = font.render(text, True, color)  # Воспроизведение текущего текста.
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        txt_surface2 = font.render(text2, True, color2)  # Воспроизведение текущего текста.
        screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))

        txt_surface3 = font.render(text3, True, color3)  # Воспроизведение текущего текста.
        screen.blit(txt_surface3, (input_box3.x + 5, input_box3.y + 5))

        txt_surface4 = font.render(text4, True, color4)  # Воспроизведение текущего текста.
        screen.blit(txt_surface4, (input_box4.x + 5, input_box4.y + 5))

        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)
        pg.draw.rect(screen, color2, input_box2, 2)
        pg.draw.rect(screen, color3, input_box3, 2)
        pg.draw.rect(screen, color4, input_box4, 2)

        text1 = font2.render('Тип линзы', True, (0, 0, 0))
        screen.blit(text1, (95, 30))
        text1 = font2.render('(рас/соб)', True, (0, 0, 0))
        screen.blit(text1, (95, 60))

        text1 = font2.render('Высота', True, (0, 0, 0))
        screen.blit(text1, (295, 30))
        text1 = font2.render('предмета', True, (0, 0, 0))
        screen.blit(text1, (295, 60))

        text1 = font2.render('Расстояние от', True, (0, 0, 0))
        screen.blit(text1, (495, 30))
        text1 = font2.render('предмета до линзы', True, (0, 0, 0))
        screen.blit(text1, (495, 60))

        text1 = font2.render('Фокус', True, (0, 0, 0))
        screen.blit(text1, (795, 60))

        all_sprites.draw(screen)
        pg.display.flip()


def main():
    global weight, height, screen, color_active, color_inactive

    screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)  # создать окно на весь экран
    height = pygame.display.Info().current_h  # высота экрана
    weight = pygame.display.Info().current_w  # ширина экрана
    pygame.display.set_caption("ход лучей в тонкой линзе")  # название окна

    color_inactive = pg.Color('green')  # цвет прямоугольника
    color_active = pg.Color('green')  # цвет текста в прямоугольнике
    start_the_graph()


if __name__ == '__main__':
    pg.init()  # запуск Pygame
    main()
    pg.quit()
