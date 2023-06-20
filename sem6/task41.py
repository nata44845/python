# Задача №41. Дан массив, состоящий из целых чисел. Напишитепрограмму, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

def get_data(x):
    list = []
    for i in range(x):
        list.append(int(input(f"Введите {i+1} элемент: ")))
    return list


def get_count(list):
    count = 0
    for i in range(1, len(list)-1):
        if list[i] > list[i-1] and list[i] > list[i+1]:
            count += 1
    return count


n = int(input("Введите размер массива N: "))
nList = get_data(n)

print(get_count(nList))
