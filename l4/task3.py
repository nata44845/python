data = '1 2 3 5 8 15 23 38'.split()
print(data)

res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)