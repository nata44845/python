def sum_numbers(n, y=0):
    sum = 0
    for i in range(1, n+1):
        sum += i
    print(sum)


def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res

sum_numbers(5)

print(sum_str('1','4','6','7'))

import modul1

print(modul1.max(5,9))

from modul1 import max

print(max(5,9))