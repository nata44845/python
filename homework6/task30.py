# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first = int(input("Введит первый элемент: "))
raz = int(input("Введит разность: "))
count = int(input("Введит количество элементов: "))

list = []

for i in range(count):
    list.append(first+i*raz)

print(*list)
