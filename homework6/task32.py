# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
if start > end:
    start, end = end, start

count = int(input("Введите количество элементов: "))

list = []
list_diap = []

for i in range(count):
    num = int(input(f"Введите {i+1} элемент: "))
    list.append(num)
    if num >= start and num <= end:
        list_diap.append(num)

print(*list)
print(start, end)
print(*list_diap)
