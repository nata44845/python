# Задача №45. Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 10^5. Программа должна вывести все пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает).
import datetime


def sum_delit(n):
    sum = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            sum += i
    return sum


def find(k):
    list = []
    for num1 in range(2, k):
        num2 = sum_delit(num1)
        if sum_delit(num2) == num1 and num1<num2:
           list.append((num1,num2))
    return list

def dict_friendly(k):
    dict = {}
    for i in range(2, k+1):
        sum = 0
        for j in range(1, i//2+1):
            if i % j == 0:
                sum += j
        dict[i] = sum

    list = []
    for i in range(2, len(dict)-1):
        for j in range(i+1, len(dict)):
            if i == dict.get(j) and j == dict.get(i) and i < j:
                list.append((i,j))
    return list


number = int(input('Enter a number K: '))

start = datetime.datetime.now()
print(dict_friendly(number))
stop = datetime.datetime.now()
print(stop-start)

start = datetime.datetime.now()
print(find(number))
stop = datetime.datetime.now()
print(stop-start)