# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
import random

n = int(input("Введите число монеток: "))

list_1 = []
sumzero = 0

for i in range(n):
    list_1.append(random.randint(0, 1))
    if list_1[i] == 0:
        sumzero += 1

if sumzero < n/2:
    print(*list_1, f" -> {sumzero}")
else:
    print(*list_1, f" -> {n-sumzero}")