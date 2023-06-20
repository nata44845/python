# Задача №35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


def simple(x):
    for i in range(2,(x//2)+1):
        if x%i==0:
            return "no"
    return "yes"


print(simple(6))