import numpy as np


def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return (count)  # выход из цикла, если угадали

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return(count) # выход из цикла, если угадали

def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1 # устанавливаем счетчик попыток; начинаем с 1-ой попытки
    predict = np.random.randint(1,101) # предполагаемое число; машина генерирует
    dlt = number - predict
    dd = abs(dlt)
    while number != predict:
        count+=1
        if number > predict:
            predict += dd
        elif number < predict:
            predict -= dd
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000)) # загадали число; машина генерирует массив случайных чисел
    for number in random_array: #для каждого компонента из массива случайных чисел
        count_ls.append(game_core(number)) #добавляем в список число попыток за которое было угадано загаданое число
    score = int(np.mean(count_ls)) #вычисляем среднее значение
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

#score_game(game_core_v1)
#score_game(game_core_v2)
score_game(game_core_v3)
