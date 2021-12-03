import pygame   #  подключение библиотеки для создания графических игр
from dict import *
#  задаём количество отрисовываемых кадров в секунду
FPS = 30 # количество кадров в секунду
fpsClock = pygame.time.Clock()

#  цвета которые можем использовать
Aqua = (0, 255, 255)
Black = (0, 0, 0)
Blue = (0, 0, 255)
Fuchsia = (255, 0, 255)
Gray = (128, 128, 128)
Green = (0, 128, 0)
Lime = (0, 255, 0)
Maroon = (128, 0, 0)
NavyBlue = (0, 0, 128)
Olive = (128, 128, 0)
Orange = [255, 165, 0]
Purple = (128, 0, 128)
Red = (255, 0, 0)
Silver = (192, 192, 192)
Teal = (0, 128, 128)
White = (255, 255, 255)
Yellow = (255, 255, 0)
FineGray = (61, 57, 58)

pygame.init()   #  запуск игровой библиотеки

x = 1080   #  Ширина окна 1280
y = 668   #  Высота окна 768
mainscreen = pygame.display.set_mode((x, y))   #  Создание окна под именем mainscreen
margin = 10                                                            #  Отступ от края окна

pygame.display.set_caption("Кликер")                                   #  Задаём название окна
#icon = pygame.image.load('assets\icons\icon.png')  #  Задаём Иконку приложения

background = Gray                                                            #  Указываем фоновый цвет
rects = FineGray
fonty = 16                                                                                   #  Высота текста
font1_Obj1 = pygame.font.Font('freesansbold.ttf', fonty)   #  Выбираем шрифт

territory = pygame.image.load('assets/pic/map_24.png')          # Загрузить картинку 'map_24', с диска, под именем "territory"
food = pygame.image.load('assets/materials/food/fish_24.png')          # Загрузить картинку 'fish_24', с диска, под именем "territory"
water = pygame.image.load('assets/materials/food/water_24.png')          # Загрузить картинку 'map.png', с диска, под именем "territory"
mgrass = pygame.image.load('assets/materials/crafting_materials/herbal3.png')
money = pygame.image.load('assets/materials/crafting_materials/c_coin.png')

pic = 24 + 6
quater = int(x / 4)
fifth = int((x -2 * margin)/ 5)
line1 = 15
line2 = 60
line2Y = 60
line3 = line2 - 20 + line2Y + 5
line4 = 220

screenY = y - margin - (line2 - 20) - line2Y
screen_Y = screenY - 40

def draw_day(Day):
    #pygame.draw.rect(mainscreen, Orange, (0, 0, quater, 80), 5)
    #mainscreen.blit(territory, (margin, margin+100))                                           # Отобразить Объект с именем "territory"
    tabcount = font1_Obj1.render(f"Day: {Day}", True, (0, 0, 0))     # Создаём Текстовый Объект с именем "tabcount" -
    mainscreen.blit(tabcount, (margin+50, line1))                                           # Отобразить Объект с именем "tabcount"
    return

def draw_meal(Meal):
    #mainscreen.blit(territory, (margin, margin+100))                                           # Отобразить Объект с именем "territory"
    tabcount = font1_Obj1.render(f"Meal: {Meal}", True, (0, 0, 0))     # Создаём Текстовый Объект с именем "tabcount" -
    mainscreen.blit(tabcount, (quater + margin+50, line1))                                           # Отобразить Объект с именем "tabcount"
    return

def draw_humans(free, total):
    #mainscreen.blit(territory, (margin, margin+100))                                           # Отобразить Объект с именем "territory"
    tabcount = font1_Obj1.render(f"Humans: {free}\{total}", True, (0, 0, 0))     # Создаём Текстовый Объект с именем "tabcount" -
    mainscreen.blit(tabcount, ((2*quater) + margin+50, line1))                                           # Отобразить Объект с именем "tabcount"
    return

def draw_happines(h):
    #mainscreen.blit(territory, (margin, margin+100))                                           # Отобразить Объект с именем "territory"
    tabcount = font1_Obj1.render(f"Happines: {h}", True, (0, 0, 0))     # Создаём Текстовый Объект с именем "tabcount" -
    mainscreen.blit(tabcount, ((3*quater) + margin+50, line1))                                           # Отобразить Объект с именем "tabcount"
    return

def draw_menu():
    menu = ["Main", "Stock", "Work", "Map", "Wiki"]
    for i in range(5):
        x = margin + fifth * i
        pygame.draw.rect(mainscreen, rects, (x, line2 - 20, fifth, line2Y), 3)
        # mainscreen.blit(territory, (margin, margin+100))      # Отобразить Объект с именем "territory"
        names = font1_Obj1.render(f"{menu[i]}", True, (0, 0, 0))  # Создаём Текстовый Объект с именем "names" -
        mainscreen.blit(names, (x + 60, line2))         # Отобразить Объект с именем "names"
    return

def draw_main():
    pygame.draw.rect(mainscreen, rects, (margin, line2-30, fifth, 80), 5)
    #mainscreen.blit(territory, (margin, margin+100))                                           # Отобразить Объект с именем "territory"
    tabcount = font1_Obj1.render(f"Main", True, (0, 0, 0))     # Создаём Текстовый Объект с именем "tabcount" -
    mainscreen.blit(tabcount, (margin+50, line2))                                           # Отобразить Объект с именем "tabcount"
    return

def draw_stock():
    pygame.draw.rect(mainscreen, rects, (fifth + margin, line2-30, fifth, 80), 5)
    #mainscreen.blit(territory, (margin, margin+100))                                           # Отобразить Объект с именем "territory"
    tabcount = font1_Obj1.render(f"Stock", True, (0, 0, 0))     # Создаём Текстовый Объект с именем "tabcount" -
    mainscreen.blit(tabcount, (fifth + margin+50, line2))                                           # Отобразить Объект с именем "tabcount"
    return

def draw_work():
    pygame.draw.rect(mainscreen, rects, ((2*fifth) + margin, line2-30, fifth, 80), 5)
    #mainscreen.blit(territory, (margin, margin+100))                                           # Отобразить Объект с именем "territory"
    tabcount = font1_Obj1.render(f"Work", True, (0, 0, 0))     # Создаём Текстовый Объект с именем "tabcount" -
    mainscreen.blit(tabcount, ((2*fifth) + margin+50, line2))                                           # Отобразить Объект с именем "tabcount"
    return

def draw_map():
    pygame.draw.rect(mainscreen, rects, ((3*fifth) + margin, line2-30, fifth, 80), 5)
    #mainscreen.blit(territory, (margin, margin+100))                                           # Отобразить Объект с именем "territory"
    tabcount = font1_Obj1.render(f"Map", True, (0, 0, 0))     # Создаём Текстовый Объект с именем "tabcount" -
    mainscreen.blit(tabcount, ((3*fifth) + margin+50, line2))                                           # Отобразить Объект с именем "tabcount"
    return

def draw_wiki():
    pygame.draw.rect(mainscreen, rects, ((4*fifth) + margin, line2-30, fifth - margin - 10, 80), 5)
    #mainscreen.blit(territory, (margin, margin+100))                                           # Отобразить Объект с именем "territory"
    tabcount = font1_Obj1.render(f"Wiki", True, (0, 0, 0))     # Создаём Текстовый Объект с именем "tabcount" -
    mainscreen.blit(tabcount, ((4*fifth) + margin+50, line2))                                           # Отобразить Объект с именем "tabcount"
    return

def draw_main_screen(main_array):         #  main_array = [known_territory, territory, food, water, Scouts, Fisher]
    draw_array = []
    pygame.draw.rect(mainscreen, background, (margin, line2 - 20 + line2Y, x, screenY))     #  Зарисовываем фон вкладки
    #Y = y - 40
    #for i in range (line3,Y, 30):
    draw_territory(main_array[0], main_array[1])
    draw_food(main_array[2])
    draw_water(main_array[3])
    return

def draw_territory(k,u):
    mainscreen.blit(territory, (margin, line3-6))                                           # Отобразить Объект с именем "territory"
    tabcount = font1_Obj1.render(f"Territory: {k}\{u}", True, (0, 0, 0))     # Создаём Текстовый Объект с именем "tabcount" -
    mainscreen.blit(tabcount, (margin+pic, line3))                                           # Отобразить Объект с именем "tabcount"
    return

def draw_food(k):
    mainscreen.blit(food, ((1*quater) + margin, line3-6))                                             # Отобразить Объект с именем "territory"
    #pygame.draw.rect(mainscreen, Orange, (0,160,150,40))
    tabcount = font1_Obj1.render(f"Food: {k}", True, (0, 0, 0))     # Создаём Текстовый Объект с именем "tabcount" -
    mainscreen.blit(tabcount, (quater + margin+pic, line3))                                           # Отобразить Объект с именем "tabcount"
    return

def draw_water(k):
    mainscreen.blit(water, ((2*quater) + margin, line3-6))                                             # Отобразить Объект с именем "territory"
    #pygame.draw.rect(mainscreen, Orange, (0,160,150,40))
    tabcount = font1_Obj1.render(f"Water: {k}", True, (0, 0, 0))     # Создаём Текстовый Объект с именем "tabcount" -
    mainscreen.blit(tabcount, ((2*quater) + margin+pic, line3))                                           # Отобразить Объект с именем "tabcount"
    return

def draw_inventory():
    for i in range(4):
        x = margin + quater * i
        pygame.draw.rect(mainscreen, Orange, (x, line4, quater, 30), 5)
    return
'''
# Картинки Противника с каёмкой
 pygame.draw.line(DISPLAYSURF, RED, (154, 570), (X, 570), 10)   # DOWN
    pygame.draw.line(DISPLAYSURF, RED, (X-6, 300), (X-6, 570), 10)   # RIGHT
    #pygame.draw.circle(DISPLAYSURF, BLUE, (300, 500), 20, 0)
    #pygame.draw.ellipse(DISPLAYSURF, GREEN, (150, 400, 40, 80), 3)
    #pygame.draw.rect(DISPLAYSURF, RED, (200, 350, 100, 50))
    pygame.display.update()
    return

def draw_Aclick():
    if money1 >= a:
        color = Orange
    else:
        color = Grey
    pygame.draw.rect(screen, color, (x-butt_weight,60,butt_weight,butt_hight))
    tabcount = font_mini.render(f"Autocliker: {a}", True, (0, 0, 0))
    screen.blit(tabcount, (x-butt_weight+10, 70))
    upgrade_count = font_mini.render("Стоимость улучшения: " + str(a), True, (0, 0, 0))
    screen.blit(upgrade_count, (10, 567))
    return
'''