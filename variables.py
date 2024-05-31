# os - библиотека для работы с консолью
import os

# Зададим цвет шрифта консоли
os.system('COLOR B')

LEFT = 1  # LEFT - левая граница
RIGHT = 5  # RIGHT - правая граница

counter_complete_HV = 12
# counter_complete_HV - количество выполненных ДЗ
counter_expensive_hours = 1.5
# counter_expensive_hours - количество затраченных часов
title_course = 'Python' # title_course - название курса

time = counter_expensive_hours / counter_complete_HV
# time - выделенное время на прохождение
hours = 'час' if time == LEFT else 'часов'
hours = 'часа' if (time < LEFT or LEFT < time < RIGHT) else 'часов'
# hours - склонение слова 'час'

# Выведем информацию
print('\nИНФОРМАЦИЯ\n')

# Выведем информацию о прохождении курса
print('Курс: ', title_course, ', всего задач: ', counter_complete_HV,
      ', затрачено часов: ', counter_expensive_hours, ', ',
      'среднее время выполнения ', time, ' ', hours, '.\n', sep='')

# Зададим переменные
first_name = 'Vasya' # first_name - первое имя
apple_count = 10 # apple_count - количество яблок
second_name = 'Petya' # second_name - второе имя
orange_count = 15 # orange_count - количество апельсинов

# Выведем информацию о торговле
print(first_name, 'дал', second_name, apple_count, 'яблок и', orange_count, 'апельсинов.\n')

try:
    os.system('PAUSE') # Остановка работы программы
    os.system('CLS') # Очищение экрана консоли
except:
    os.system('CLS') # Очищение экрана консоли
