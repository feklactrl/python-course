# примеры из урока

# for i in range(5):
#     print("Привет!")
#
# for i in range(1, 6):
#     print("Номер", i)

# x = 0
# while x < 3:
#     print("повторение ", x)
#     x+=1

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)



# ДОМАШНЕЕ ЗАДАНИЕ 1

# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     print(i)

# ДОМАШНЕЕ ЗАДАНИЕ 2

n = int(input("введите число: "))
total = 0
for i in range(1, n + 1):
    total += i

print(f'сумма чисел от 1 до {n} равна {total}')
