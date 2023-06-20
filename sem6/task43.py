# Задача №43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.

def get_data(x):
    list = []
    for i in range(x):
        list.append(int(input(f"Введите {i+1} элемент: ")))
    return list


def get_count(list):
    count = 0
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if list[i] == list[j]:
                count += 1
    return count

n = int(input("Введите размер массива N: "))
nList = get_data(n)

print(get_count(nList))
