# Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# my_list="a a a b c a a d c d d".split()

my_list = "шла шла собака по роялю шла".split()

new_list = []

dict_1 = {}


# for i in range(len(my_list)):
#     n=my_list[0:i].count(my_list[i])
#     if n>0:
#         new_list.append(f"{my_list[i]}_{n}")
#     else:
#         new_list.append(my_list[i])

# print(*new_list)

for i in my_list:
    if i in dict_1:
        new_list.append(f"{i}_{dict_1[i]}")
        dict_1[i] += 1
    else:
        new_list.append(i)
        dict_1[i] = 1

print(*new_list)