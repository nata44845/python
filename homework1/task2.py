# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

n = int(input("Введите трехзначное число: "))
sum = 0
sumText = ""
temp = n

for i in range(3):
    x = temp % 10
    sum += x
    sumText = (" + " if i < 2 else "") + str(x) + sumText
    temp //= 10

print(f"{n} -> {sum} ({sumText})")
