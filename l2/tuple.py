t = () # создание пустого кортежа
print(type(t)) # class <'tuple'>
t = (1,)
print(type(t))
t = (1,2)
print(type(t))
t = (28, 9, 1990)
print(type(t))

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

print(t[0])

for i in t:
	print(i)
for i in range(len(t)):
	print(t[i])