list_1 = []
list_1 = list()
list_1 = [1,2,3,8]
print(*list_1)

list_1.append(6)

print(*list_1)

for i in range(5):
    list_1.append(i)

print(*list_1)

a=list_1.pop(0)

print(*list_1)

list_1.insert(100,45)

print(*list_1)

print(*list_1[5:])

for key,i in list_1:
    print(key)