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
    predict_number = 50  # предположение, что загаданное число равно половине диапазона угадываемых чисел
    divider = 50   # переменная для уменьшения диапазона массива чисел содержащего загаданного число
    
    while True:
        count += 1        
        if number == predict_number:  
            break  # выход из цикла если угадали
        
        if number > predict_number:
            if divider % 2 == 0:
                predict_number += divider / 2                 
                divider /= 2
            else:
                predict_number += (divider + 1)/2
                divider = (divider + 1)/2
              
        elif number < predict_number:
            if divider % 2 == 0:
                predict_number -= divider / 2               
                divider /=2                
            else:
                predict_number -= (divider + 1)/2       
                divider = (divider + 1)/2
              
       
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
