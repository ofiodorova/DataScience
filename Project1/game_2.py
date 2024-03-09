
"""Игра угадай число.
Компьютер сам загадывает и угадывает число 
"""

import numpy as np

def random_predict(number:int=1) -> int:
    count = 0
    while True:
        count +=1
        predict_number = np.random.randint(1, 101)
        if predict_number == number:
           #  print (f"Your number {predict_number} is correct. Number of attempts = {count}")
            break
    return count

def score_game(random_predict) -> int:
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)



score_game(random_predict)
        

