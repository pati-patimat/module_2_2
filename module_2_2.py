number_1 = input('Введите число: ')
number_2 = input('Веедите число: ')
number_3 = input('Веедите число: ')
if number_1 == number_2 == number_3:
    print(3)
elif number_1 == number_2 or number_2 == number_3 or number_3 == number_1:
    print(2)
elif number_1 != number_2 != number_3:
    print(0)