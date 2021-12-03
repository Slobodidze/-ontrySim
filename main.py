# This is a Симулятор Развития Страны
#  https://www.gamedevmarket.net/
import random
import math
import pygame.event
from dict import *
from gui import *
#contry = input('Как будет называться ваша Страна? ')
#name = input('Как к вам обращаться? ')
#print(f'О, {name}, вы стали у руля страны {contry}')
#print(f'Cтрана {contry}, в упадке. Необходмы кардинальные решения и действия')

#Resources
population = random.randint(20, 500)    #  Население
free_human = population
territory = random.randint(850, 10000)    #  Территория острова
known_territory = 0    #  Исследованая Територия
islands = 1    #  Количество островов
money = random.randint(1, 1000000)    #  Деньги -
wood = random.randint(1, 250)    #  Древесина +
stone = random.randint(1, 188)    #  Камни +
iron = random.randint(1, 110)    #  Железо +
copper = random.randint(1, 25)    #  Медь +
mgrass = random.randint(1, 1000)    #  Мед.Травы +
food = random.randint(1, 3000)    #  Пища +
water = random.randint(1, 3000)    #  Вода +
coal = random.randint(1, 80)    #  Уголь +

#Not Resources
Technology = 0                        #  Наш Технологический - научный уровень, знаний
ProductionLevel = 0             #  Наш уровень развития Промышленности
Production = {0:1, 1:2, 2:3, 3:4, 4:5}       #  уровень развития Промышленности и множитель
ProductionNames = {0:"Каменный век", 1:"Бронзовый век", 2:"Железный век", 3:"Век Пара", 4:"Век Полимеров"}       #  уровень развития Промышленности
Scouts = 0    #  Иссдедователи, скауты
Medics = 0    #  Медики
Miners = 0    #  Шахтёры, добытчики
Fisher = 0    #  Ловят рыбу и крабов с берега
Farmers = 0    #  Фермеры
Crafters = 0    #  Производственники
Builders = 0    #  Строители
print(f'у Вас {islands} Остров, Територии - {territory}км и населения {population} жителей')
print(f'Ресурсов: Денег - {money}, Древесины - {wood}')
print(f'Камней - {stone}, Железа - {iron}')
print(f'Меди - {copper}, Медикаменты - {mgrass}')
print(f'Еда - {food}, Вода - {water}')
print(f'Уголь - {coal}')

day = 1
meals = 0
happyness = 0

def check_humans(q):
    global free_human
    run = True
    while run:
        if 0 <= q <= free_human:
            ok = q
            free_human = free_human - q
            run = False
        else:
            print(f"Вы не можете отправить более {free_human} людей или менее Нуля")
            q = input('Введите новое число работников ')
            q = int(q)
            run = True
    return ok

def scout():    #  Всё что касается скаутов-исследователей
    global Scouts
    global known_territory
    Scouts = input('Сколько сегодня исследователей? ')
    Scouts = int(Scouts)    #  Преобразование строки в число
    Scouts = check_humans(Scouts)
    known_territory = known_territory + (Scouts * 10)
    print(f' Исследовано Територии - {known_territory}кв.км ')
    draw_territory(known_territory, territory)
    return

def fisher():    #  Всё что касается Рыбаков
    global Fisher
    global food
    Fisher = input('Сколько сегодня рыбачат? ')
    Fisher = int(Fisher)
    Fisher = check_humans(Fisher)
    q = random.randint(1, 3)    #  Генерируем случайное число от 1 до 3
    fish = Fisher * q
    print(f'Было поймано рыб или крабов {fish}')
    food = food + fish
    return

def scout2():    #  Всё что касается скаутов-исследователей
    global known_territory
    known_territory = known_territory + (Scouts * 10)
    print(f' Исследовано Територии - {known_territory}кв.км ')
    draw_territory(known_territory, territory)
    return

def fisher2():    #  Всё что касается Рыбаков
    global food
    fish = 0
    for i in range(Fisher):
        q = random.randint(1, 3)    #  Генерируем случайное число от 1 до 3
        fish = fish + q
    print(f'Было поймано рыб или крабов {fish}')
    food = food + fish
    return

def Line1():
    global meals
    draw_day(day)
    foods = int(food/population)      # На сколько дней хатает еды
    waters = int(water/population)      # На сколько дней хатает воды
    if foods > waters:      # Если запасов Еды больше
        meals = waters      # Предупреждаем о запасах ВОДЫ
    else:
        meals = foods
    draw_meal(meals)
    draw_humans(free_human, population)
    draw_happines(happyness)
    return

mode = 'main'     #main,stock, work, map, wiki
def Line2():
    #draw_main()
    #draw_stock()
    #draw_work()
    #draw_map()
    #draw_wiki()
    draw_menu()
    if mode =='main':
        main_array = [known_territory, territory, food, water, Scouts, Fisher]
        #draw_territory(known_territory, territory)
        #draw_food(food)
        #draw_water(water)
        draw_main_screen(main_array)
    elif mode =='stock':
        main_array = [known_territory, territory, food, water, Scouts, Fisher]
        draw_main_screen(main_array)
        draw_inventory()
    elif mode =='work':
        draw_main_screen()
    elif mode =='map':
        draw_main_screen()
    elif mode =='wiki':
        draw_main_screen()
    else:
        draw_main_screen()
    return

def nextday():
    global day
    global food
    global water
    day = day + 1  # День закончился
    scout2()    # Скауты отрабатывают день до конца
    fisher2()   # Рыбаки отрабатывают день до конца
    food = food - population
    water = water - population
    return


#mainscreen.fill(background)          #  Заливаем окно фоновым цветом
#draw_territory(known_territory, territory)
#pygame.display.update()

run = True
while run:          #  Основной Цикл игры
    mainscreen.fill(background)          #  Заливаем окно фоновым цветом
    for event in pygame.event.get():    #  Смотрим все события
        if event.type == pygame.QUIT:   #  Если есть событие Закрыть приложение
            run = False
            pygame.quit()
            sys.exit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit()
                sys.exit()
                break
            if event.key == pygame.K_1:
                mode = 'main'
            if event.key == pygame.K_2:
                mode = 'stock'
            if event.key == pygame.K_3:
                mode = 'work'
            if event.key == pygame.K_4:
                mode = 'map'
            if event.key == pygame.K_5:
                mode = 'wiki'
            if event.key == pygame.K_7:
                draw_inventory()
            if event.key == pygame.K_SPACE:
                nextday()
            if event.key == pygame.K_q:
                if free_human > 0:
                    free_human = free_human - 1
                    Scouts = Scouts + 1
            if event.key == pygame.K_a:
                if Scouts > 0:
                    free_human = free_human + 1
                    Scouts = Scouts - 1
            if event.key == pygame.K_w:
                if free_human > 0:
                    free_human = free_human - 1
                    Fisher = Fisher + 1
            if event.key == pygame.K_s:
                if Fisher > 0:
                    free_human = free_human + 1
                    Fisher = Fisher - 1
    #free_human = population
    #pygame.draw.rect(mainscreen, Red, (10, 300, quater, 30), 5)
    Line1()
    Line2()

    pygame.display.update()
    fpsClock.tick(FPS)


#    Иван - руководство и строительство
#   Влад - раззведка и медицина
#   Мирослав - добыча ресурсов
#   Бобдан - добыча  продуктов
#   Димон - производство и переработка

