import pyscreeze
import pyautogui
from PIL import Image

for k in range(15):
    # c = int(input())
    m1 = []
    pyscreeze.screenshot("Screenshot_2.png")
    img = Image.open('Screenshot_2.png')
    img = img.load()
    # создаём массив в котором будут храниться данные о значениях леток
    y = 305
    x = 24
    for j in range(18):
        m2 = []
        for i in range(32):

            pixl = img[x, y]

            if j == 0:
                m2.append(0)
            elif j == 17:
                m2.append(0)
            elif i == 0:
                m2.append(0)
            elif i == 31:
                m2.append(0)
            elif pixl == (189, 189, 189):
                m2.append(0)
                # print(pixl, x, y)
            elif pixl == (0, 0, 252) or pixl == (1, 1, 251) or pixl == (142, 142, 205) or pixl == (
                    47, 47, 238) or pixl == (35, 35, 239) or pixl == (13, 13, 248) or pixl == (105, 105, 215) \
                    or pixl == (151, 151, 197) or pixl == (1, 1, 252) or pixl == (47, 47, 243) or pixl == (
                    47, 47, 234) or pixl == (0, 0, 255) or pixl == (106, 106, 218) or pixl == (
            12, 12, 251) or pixl == (
                    35, 35, 243):
                m2.append(1)
                # print(pixl, x, y)
            elif pixl == (0, 123, 0) or pixl == (47, 139, 47) or pixl == (47, 172, 142,) or pixl == (
                    142, 172, 142) or pixl == (35, 135, 35) or pixl == (83, 152, 83):
                m2.append(2)
                # print(pixl, x, y)
            elif pixl == (255, 0, 0) or pixl == (238, 47, 47) or pixl == (243, 35, 35) or pixl == (
                    205, 142, 142):
                m2.append(3)
                # print(pixl, x, y)
            elif pixl == (0, 0, 123) or pixl == (12, 12, 127) or pixl == (35, 35, 135) or pixl == (
                    142, 142, 172):
                m2.append(4)
                # print(pixl, x, y)
            elif pixl == (123, 0, 0) or pixl == (139, 47, 47) or pixl == (172, 142, 142) or pixl == (
                    160, 106, 106) or pixl == (135, 35, 35) or pixl == (177, 154, 154) or pixl == (152, 83, 83):
                m2.append(5)
                # print(pixl, x, y)
            elif pixl == (0, 0, 0):
                m2.append(10)
                # print(pixl, x, y)
            else:
                m2.append(77)
                # print(pixl, x, y)

            if i % 2 == 0:
                x += 32
            else:
                x += 32
        x = 24
        y += 32

        m1.append(m2)
    y = 305
    t = 13
    # дополняем массив разделив просто пустые клетки и клетки которые ещё не имеют значения так как не нажаты
    for j in range(18):

        for i in range(32):

            pixl = img[t, y]

            if j == 0:
                pass
            elif pixl == (255, 255, 255) or pixl == (205, 205, 205) or pixl == (238, 238, 238):
                m1[j][i] = 9
                # print(pixl, t, y)

            t += 32

        t = 9
        if j % 2 == 1:
            y += 33
        else:
            y += 31

    # логика определения мин или свободных клеток
    for j in range(18):
        for i in range(32):
            if j == 0:
                pass
            # m1[j-1][i-1] m1[j-1][i] m1[j-1][i+1]
            # m1[j][i-1]   m1[j][i]     m1[j][i+1]
            # m1[j+1][i-1] m1[j+1][i] m1[j+1][i+1]
            elif m1[j][i] == 1:
                if m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i - 1] != 9 and \
                        m1[j + 1][i + 1] != 9: # в случае если вокруг нету неизвестных нам клеток то эта клетка больше не несёт в себе информации
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][
                    i + 1] != 9 and m1[j - 1][i - 1] == 9 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 \
                    and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and \
                        m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:  # если m1[j-1][i-1] == 9 и вокруг всё отмечено то 1 становится 0
                    m1[j - 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][
                    i + 1] == 9 and m1[j - 1][i - 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j - 1][
                    i - 1] != 10:  # если m1[j+1][i+1] == 9 и вокруг всё отмечено то 1 становится 0
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] == 9 and m1[j + 1][
                    i + 1] != 9 and m1[j - 1][i - 1] != 9 \
                        and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10 and m1[j - 1][
                    i - 1] != 10:  # если m1[j+1][i] == 9 == 9 и вокруг всё отмечено то 1 становится 0
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] == 9 and m1[j + 1][i] != 9 and m1[j + 1][
                    i + 1] != 9 and m1[j - 1][i - 1] != 9 \
                        and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10 and m1[j - 1][
                    i - 1] != 10:  # если m1[j+1][i-1] == 9 и вокруг всё отмечено то 1 становится 0
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] == 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][
                    i + 1] != 9 and m1[j - 1][i - 1] != 9 \
                        and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and \
                        m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10 and \
                        m1[j - 1][
                            i - 1] != 10:  # если  m1[j][i+1] == 9 и вокруг всё отмечено то 1 становится 0
                    m1[j][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] == 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][
                    i + 1] != 9 and m1[j - 1][i - 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10 and m1[j - 1][
                    i - 1] != 10:
                    m1[j][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] == 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][
                    i + 1] != 9 and m1[j - 1][i - 1] != 9 \
                        and m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10 and m1[j - 1][
                    i - 1] != 10:  # если m1[j-1][i+1] == 9 и вокруг всё отмечено то 1 становится 0
                    m1[j - 1][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] == 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][
                    i + 1] != 9 and m1[j - 1][i - 1] != 9 and \
                        m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10 and m1[j - 1][
                    i - 1] != 10:  # если m1[j-1][i] == 9  и вокруг всё отмечено то 1 становится 0
                    m1[j - 1][i] = 10
                    m1[j][i] = 0

            elif m1[j][i] == 2:
                # m1[j-1][i-1] m1[j-1][i] m1[j-1][i+1]
                # m1[j][i-1]   m1[j][i]     m1[j][i+1]
                # m1[j+1][i-1] m1[j+1][i] m1[j+1][i+1]
                # УСЛОВИЕ на отметку двух мин если рядом нету не одной
                if m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i - 1] != 9 and \
                        m1[j + 1][i + 1] != 9: # в случае если вокруг нету неизвестных нам клеток то эта клетка больше не несёт в себе информации
                    m1[j][i] = 0
                elif m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and \
                        m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and \
                        m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i - 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i - 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j][i + 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i] != 10:
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10:
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

            elif m1[j][i] == 3:
                # УСЛОВИЕ на отметку 3 мин если рядом нету не одной, хотя то и не важно есть ли они рядом мы их не учитываем так как не ставим флажки в игре, главное что информация о минах есть в нашем массиве, также следуя логике нам всё равно сколько вокруг мин так как мы обозначим мины только в случае если вокруг нас 5 не мин или 5 известных нам ка безопасных клеток.
                if m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i - 1] != 9 and \
                        m1[j + 1][i + 1] != 9: # в случае если вокруг нету неизвестных нам клеток то эта клетка больше не несёт в себе информации
                    m1[j][i] = 0
                elif m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                          m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                    m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                    m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and  m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and \
                        m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                # m1[j-1][i-1] m1[j-1][i] m1[j-1][i+1]
                # m1[j][i-1]   m1[j][i]     m1[j][i+1]
                # m1[j+1][i-1] m1[j+1][i] m1[j+1][i+1]
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10 :
                    m1[j - 1][i - 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and  m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10  :
                    m1[j - 1][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j + 1][i-1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i-1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i-1] != 10 :
                    m1[j - 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j][i - 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and  m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and \
                        m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and \
                        m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and \
                        m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 :
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and \
                        m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and \
                        m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and\
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and \
                        m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i] != 10 :
                    m1[j - 1][i] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and\
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i - 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10 :
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j + 1][ i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j + 1][
                    i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i] != 10 :
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i - 1] != 10 :
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and \
                        m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and \
                        m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and m1[j + 1][i] != 9 and\
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and \
                        m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i] != 10 :
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i + 1] != 9 and m1[j + 1][i - 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i + 1] != 10 and m1[j + 1][i - 1] != 10:
                    m1[j][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i - 1] != 9 and m1[j + 1][i - 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i - 1] != 10 and m1[j + 1][i - 1] != 10:
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                    # m1[j-1][i-1] m1[j-1][i] m1[j-1][i+1]
                    # m1[j][i-1]    m1[j][i]    m1[j][i+1]
                    # m1[j+1][i-1] m1[j+1][i] m1[j+1][i+1]
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i - 1] != 9 and m1[j][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i - 1] != 10 and m1[j][i + 1] != 10:
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

            elif m1[j][i] == 4:
                # УСЛОВИЕ на отметку 3 мин если рядом нету не одной, хотя то и не важно есть ли они рядом мы их не учитываем так как не ставим флажки в игре, главное что информация о минах есть в нашем массиве, также следуя логике нам всё равно сколько вокруг мин так как мы обозначим мины только в случае если вокруг нас 5 не мин или 5 известных нам ка безопасных клеток.
                if m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i + 1] != 9:  # в случае если вокруг нету неизвестных нам клеток то эта клетка больше не несёт в себе информации
                    m1[j][i] = 0
                    # m1[j-1][i-1] m1[j-1][i] m1[j-1][i+1]
                    # m1[j][i-1]   m1[j][i]     m1[j][i+1]
                    # m1[j+1][i-1] m1[j+1][i] m1[j+1][i+1]
                elif m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j][i - 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j][i - 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                    # m1[j-1][i-1] m1[j-1][i] m1[j-1][i+1]
                    # m1[j][i-1]   m1[j][i]     m1[j][i+1]
                    # m1[j+1][i-1] m1[j+1][i] m1[j+1][i+1]
                elif m1[j - 1][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][
                    i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and \
                     m1[j + 1][i + 1] != 9 and \
                     m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                         i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and \
                     m1[j + 1][i + 1] != 9 and \
                     m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                     m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 :
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0
                    # m1[j-1][i-1] m1[j-1][i] m1[j-1][i+1]
                    # m1[j][i-1]   m1[j][i]     m1[j][i+1]
                    # m1[j+1][i-1] m1[j+1][i] m1[j+1][i+1]
                elif m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and  m1[j + 1][
                    i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i - 1] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 :
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and \
                     m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i] != 10 :
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and \
                        m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][
                    i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][
                    i] != 10 :
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j + 1][
                    i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i - 1] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][
                    i] != 10 :
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and \
                        m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 :
                    m1[j - 1][i - 1] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 :
                    m1[j - 1][i - 1] = 10
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][
                    i - 1] != 9 and \
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j + 1][
                    i - 1] != 10 :
                    m1[j - 1][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and\
                        m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10:
                    m1[j - 1][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j][i - 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i - 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j][i - 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i - 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10 :
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i] != 10 :
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and\
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i + 1] != 10 and \
                        m1[j + 1][i - 1] != 10 :
                    m1[j - 1][i] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and \
                         m1[j + 1][i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and \
                        m1[j + 1][i] != 10 :
                    m1[j - 1][i] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j + 1][
                    i - 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and \
                        m1[j + 1][i - 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i + 1] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i + 1] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10:
                    m1[j - 1][i] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j + 1][i] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j + 1][i] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j + 1][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j + 1][i - 1] != 10 and m1[j + 1][i] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i + 1] != 9 and\
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i + 1] != 10 and  m1[j + 1][i + 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i + 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i + 1] != 10 and m1[j + 1][
                    i - 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j + 1][i + 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j + 1][
                    i] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j + 1][i - 1] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j + 1][
                    i - 1] != 10:
                    m1[j - 1][i + 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j][i - 1] != 9 and m1[j][
                    i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j][i - 1] != 10 and m1[j][
                    i + 1] != 10 :
                    m1[j - 1][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and \
                        m1[j + 1][i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and \
                        m1[j + 1][i + 1] != 10:
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j][i] = 0
                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j + 1][i] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and \
                        m1[j + 1][i] != 10:
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j + 1][
                    i - 1] != 9 and\
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and \
                        m1[j + 1][i - 1] != 10:
                    m1[j][i - 1] = 10
                    m1[j][i + 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i + 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i + 1] != 10:
                    m1[j][i - 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0
                    # m1[j-1][i-1] m1[j-1][i] m1[j-1][i+1]
                    # m1[j][i-1]   m1[j][i]     m1[j][i+1]
                    # m1[j+1][i-1] m1[j+1][i] m1[j+1][i+1]

                elif m1[j - 1][i - 1] != 9 and m1[j - 1][i] != 9 and m1[j - 1][i + 1] != 9 and m1[j][
                    i - 1] != 9 and \
                        m1[j - 1][i - 1] != 10 and m1[j - 1][i] != 10 and m1[j - 1][i + 1] != 10 and m1[j][
                    i - 1] != 10:
                    m1[j][i + 1] = 10
                    m1[j + 1][i - 1] = 10
                    m1[j + 1][i] = 10
                    m1[j + 1][i + 1] = 10
                    m1[j][i] = 0
    def avtoclik(x, y, j, i):
        if m1[j - 1][i - 1] == 9:
            pyautogui.click(x - 31, y - 31)
        if m1[j - 1][i] == 9:
            pyautogui.click(x, y - 31)
        if m1[j - 1][i + 1] == 9:
            pyautogui.click(x + 31, y - 31)
        if m1[j][i - 1] == 9:
            pyautogui.click(x - 31, y)
        if m1[j][i + 1] == 9:
            pyautogui.click(x + 31, y)
        if m1[j + 1][i - 1] == 9:
            pyautogui.click(x - 31, y + 31)
        if m1[j + 1][i] == 9:
            pyautogui.click(x, y + 31)
        if m1[j + 1][i + 1] == 9:
            pyautogui.click(x + 31, y + 31)
    # клик по клеткам не являющимся минами
    y = 305
    x = 23
    for j in range(18):
        # m1[j-1][i-1] m1[j-1][i] m1[j-1][i+1]
        # m1[j][i-1]   m1[j][i]     m1[j][i+1]
        # m1[j+1][i-1] m1[j+1][i] m1[j+1][i+1]
        for i in range(32):
            if m1[j][i] == 0:
                pass
            elif m1[j][i] == 1:

                if m1[j - 1][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j + 1][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)

            elif m1[j][i] == 2:

                if m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j + 1][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j + 1][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j + 1][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i - 1] == 10 and m1[j][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i - 1] == 10 and m1[j + 1][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i - 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i - 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j + 1][i - 1] == 10 and m1[j][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j + 1][i - 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j + 1][i - 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i + 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i + 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j + 1][i + 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)

            elif m1[j][i] == 3:
                if m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j + 1][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10 and m1[j + 1][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j][i - 1] == 10 and m1[j][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j][i - 1] == 10 and m1[j + 1][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j][i - 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j][i - 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i - 1]:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j + 1][i] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)


                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and m1[j + 1][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j][i - 1] == 10 and m1[j][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j][i - 1] == 10 and m1[j+1][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j][i - 1] == 10 and m1[j+1][i ] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j][i - 1] == 10 and m1[j+1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j + 1][i - 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j + 1][i - 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j + 1][i] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and m1[j][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and m1[j + 1][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j + 1][i] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i - 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i - 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i - 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i - 1] == 10 and m1[j + 1][i] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i + 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j + 1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i + 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i + 1] == 10 and m1[j + 1][i] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j + 1][i - 1] == 10 and m1[j + 1][i] == 10 and m1[j + 1][i + 1] == 10:
                    avtoclik(x, y, j, i)

            elif m1[j][i] == 4:
                if m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and  m1[j][i-1]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and  m1[j][i+1]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10   and m1[j+1][i-1]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and  m1[j+1][i]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and  m1[j+1][i+1]== 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j][i - 1] == 10 and  m1[j][i+1]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j][i - 1] == 10  and m1[j+1][i-1]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j][i - 1] == 10 and  m1[j+1][i]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j][i - 1] == 10  and m1[j+1][i+1]== 10:
                    avtoclik(x, y, j, i)


                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j][i + 1] == 10 and  m1[j+1][i-1]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j][i + 1] == 10  and m1[j+1][i]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j][i + 1] == 10 and  m1[j+1][i+1]== 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j + 1][i - 1] == 10 and  m1[j+1][i]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j + 1][i - 1] == 10  and m1[j+1][i+1]== 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i] == 10 and m1[j + 1][i] == 10  and m1[j+1][i+1]== 10:
                    avtoclik(x, y, j, i)


                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and  m1[j][i+1]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and  m1[j+1][i-1]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and  m1[j+1][i]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10  and m1[j+1][i+1]== 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i + 1] == 10 and  m1[j+1][i-1]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i + 1] == 10  and m1[j+1][i]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i + 1] == 10  and m1[j+1][i+1]== 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10 and m1[j + 1][i - 1] == 10  and m1[j+1][i]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10 and m1[j + 1][i - 1] == 10 and  m1[j+1][i+1]== 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i - 1] == 10 and m1[j - 1][i + 1] == 10 and m1[j + 1][i] == 10  and m1[j+1][i+1]== 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i - 1] == 10 and m1[j][i - 1] == 10 and m1[j][i + 1] == 10  and m1[j+1][i-1]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j][i - 1] == 10 and m1[j][i + 1] == 10  and m1[j+1][i]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j][i - 1] == 10 and m1[j][i + 1] == 10  and m1[j+1][i+1]== 10:
                    avtoclik(x, y, j, i)


                elif m1[j - 1][i - 1] == 10 and m1[j][i - 1] == 10 and m1[j + 1][i - 1] == 10 and  m1[j+1][i]== 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j][i - 1] == 10 and m1[j + 1][i - 1] == 10 and  m1[j+1][i+1]== 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i - 1] == 10 and m1[j][i - 1] == 10 and m1[j + 1][i] == 10 and m1[j+1][i+1]== 10:
                    avtoclik(x, y, j, i)


                elif m1[j - 1][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i - 1]== 10 and m1[j+1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i - 1]== 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i - 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j + 1][i] and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and m1[j][i+1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and m1[j+1][i-1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and m1[j+1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i + 1] == 10 and m1[j+1][i-1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i + 1] == 10 and m1[j+1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and m1[j][i + 1] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j+1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i] == 10 and m1[j - 1][i + 1] == 10 and m1[j + 1][i] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i] == 10 and m1[j][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j+1][i-1] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j+1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i] == 10 and m1[j][i - 1] == 10 and m1[j+1][i - 1] == 10 and m1[j+1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j][i - 1] == 10 and m1[j+1][i - 1] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i] == 10 and m1[j][i - 1] == 10 and m1[j+1][i ] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j+1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i] == 10 and m1[j + 1][i - 1] == 10 and m1[j + 1][i] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)



                elif m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j+1][i-1] == 10 :
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j+1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and m1[j][i + 1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j+1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i + 1] == 10 and m1[j][i - 1] == 10 and m1[j + 1][i] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i + 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j+1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j - 1][i + 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)


                elif m1[j - 1][i + 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j - 1][i + 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j + 1][i] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                    # and m1[j-1][i-1] == 10        and m1[j-1][i] == 10        and m1[j-1][i+1] == 10
                    # and m1[j][i-1] == 10                     m1[j][i]         and m1[j][i+1] == 10
                    # and m1[j+1][i-1] == 10        and m1[j+1][i] == 10        and m1[j+1][i+1] == 10

                elif m1[j][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j+1][i] == 10:
                    avtoclik(x, y, j, i)
                elif m1[j][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j][i - 1] == 10 and m1[j][i + 1] == 10 and m1[j + 1][i] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j][i - 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j + 1][i] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

                elif m1[j][i + 1] == 10 and m1[j + 1][i - 1] == 10 and m1[j + 1][i] == 10 and m1[j+1][i+1] == 10:
                    avtoclik(x, y, j, i)

            x += 32
        x = 24
        y += 32






