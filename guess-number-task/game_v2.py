from numpy.core.numeric import count_nonzero
"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    # задаем нижнюю и верхнюю границу  
    lowerlim = 1
    upperlim = 101
    
    while True:
        count += 1
        #predict_number = np.random.randint(1, 101)  # предполагаемое число
        predict_number = np.random.randint(lowerlim, upperlim)  # предполагаемое число в изменяемых границах
        if number > predict_number:
            lowerlim = predict_number
        elif number < predict_number:
            upperlim = predict_number
        # выход из цикла если число угадано
        else:
            break
        
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(10)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    #print(random_array)

    for number in random_array:
        count_ls.append(random_predict(number))

    #print(count_ls)
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score




if __name__ == "__main__":
    # RUN
    score_game(random_predict)
