# name = "kit"
# age = 18
#
# if age >=18 :
#     print(f"{name}, ты можешь получить водительские права!")
# else:
#     print(f"{name}, пока рано за руль!")


# ЗАДАНИЕ 1
age = int(input("введите свой возраст: "))
if age <=7 :
    print("ты еще малыш!")
elif age <=17 :
    print("ты школьник")
elif age <=22 :
    print("ты студент")
else:
    print("ты взрослый человек")


# ЗАДАНИЕ 2

tempirature = int(input("напиши сколько сейчас градусов: "))
if tempirature <0 :
    print("очень холодно! надень шапку")
elif tempirature <10 :
    print("прохладно! возьми куртку")
elif tempirature <20 :
    print("тепло, но не жарко")
else:
    print("можешь одеть футболку")
