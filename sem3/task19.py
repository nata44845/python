# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 2
# Output:  [4, 5, 1, 2, 3]


list_1 = [1, 2, 3, 4, 5]
k = int(input("Введите k: "))
k = k%len(list_1)
# k = len(list_1)-k

list_2 = []

for i in list_1[-k:]:
    list_2.append(i)

for i in list_1[:-k]:
    list_2.append(i)

print(list_2)


# for i in range(k):
#     list_1.insert(0,list_1.pop())

# print(list_1)