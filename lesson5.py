# a = [1, 2, 3]
# b = a.copy()
# b.append(4)
#
# print(a)
# print(b)

# fruits = ["яблоко", "банан", "вишня"]
# print("исходный список: ", fruits)
#
# fruits.append("киви")
# fruits.insert(1, "манго")
# print("после обновления: ", fruits)
#
# fruits.remove("банан")
# print("после удаления: ", fruits)
#
# fruits.sort()
# print("отсортированный список: ", fruits)


# дз 1

animals = ['кошка', 'собака', 'крыса', 'ящерица', 'рыбка']
print('исходный список: ', animals)

animals.append('хомяк')
animals.insert(2, 'курица')
print('после добавления: ', animals)

animals.remove('рыбка')
print('после удаления: ', animals)

animals.sort()
print('отсортированный список: ', animals)

result = animals.sort()
print('вот мой обновленный список', result)



