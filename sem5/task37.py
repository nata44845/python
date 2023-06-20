# Задача №37. Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def rev_input(n):
#     num = input()
#     if n == 1:
#         return num
    
#     return rev_input(n - 1) + ' ' + num
    
    
# print(rev_input(4))


def rev(list):
    if len(list)==1: 
        return list
    num0=list.pop(0)
    return(rev(list).append(num0))


print(rev([3,4]))