# дз 1

# fruits = ['apple', 'banana', 'avocado', 'orange', 'grape']
# for fruit in fruits:
#     print(fruit)
#
#
# # дз 2
#
# numbers = [1,2,3,4,5,6,7,8,9,10]
#
# total = 0
#
# for number in numbers:
#     if number % 2 == 0:
#         print(number)
#
#     total += number
#
# print(f"сумма всех чисел: {total}")


# дополнительные задания

numbers = [1,5,7,6,8,9,3,4,2,6]
print("четные числа: ")

for number in numbers:
    if number % 2 == 0:
        print(number)

minimum = min(numbers)
maximum = max(numbers)
print(f"минимальное число: {minimum}, максимальное число: {maximum}")