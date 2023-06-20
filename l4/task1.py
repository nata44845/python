# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).

mas = [1,2,3,5,8,15,23,38]

# for i in mas:
#     if i%2==0:
#         mas_new.append((i,i*i))

# print(*mas_new)

def select(f,col):
    return [f(x) for x in col]

def where(f,col):
    return [x for x in col if f(x)]

res = where(lambda x:x%2==0,mas)
print(res)
res = select(lambda x:(x,x*x),res)
print(res)
