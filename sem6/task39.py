# Задача №39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива

def get_data(x):
    list = []
    for i in range(x):
        list.append(int(input(f"Введите {i+1} элемент: ")))
    return list    

def diff(list1: list[int],list2: list[int]) -> list[int]:
    result = []
    for i in list1:
        if i not in list2:
            result.append(i)
    return result


n = int(input("Введите размер N: "))
nList = get_data(n)

m = int(input("Введите размер M: "))
mList = get_data(m)

print(diff(nList, mList))


test_res = set(test_list1)-set(test_list2)
print(test_res)
[3, 1, 3, 4, 2, 4, 12]
{2, 3, 12}
for i in test_list1:
    if i in test_res:
        print(i)