# print('Задача 1.4:')
# print('Введите сумму $, имеющихся у Пола: ')
# sum = float(input())
# print('Введите цену одной бутылки вина, $: ')
# price = float(input())
# print('Пол может купить не больше', int(sum // price), 'бутылок вина.')

# print('Задача 1.5:')
# print('Введите сумму $, которая имеется в наличии у Пола: ')
# sum = float(input())
# print('Введите цену одной бутылки вина, $: ')
# price = float(input())
# print('Пол может купить не больше', int(sum // price), 'бутылок вина, т.к. у него останется', float(sum % price), '$')

# print('Задача 1.6:')
# print('Введите сумму $, которая имеется у Пола в наличии: ')
# sum = float(input())
# print('Введите цену одной бутылки вина, $: ')
# price = float(input())
# print('Пол может купить не больше', int(sum // price), 'бутылок вина.')
# print('Введите количество бутылок вина, которое купил Пол: ')
# numbers = int(input())
# print('Пол потратил', price * numbers, '$, у него еще осталось в наличии', round((sum - price * numbers),2), '$.')

# print('Задача НТ_1_1:')
# print('Введите длину ребра куба:')
# a = float(input())
# b = (a**3)
# c = (a**2*4)
# print('Объем куба равен: ', b)
# print("Площадь боковой поверхноти куба равна: ", c)

# print('Задача НТ_1_2:')
# print('Введите число 1: ')
# number_1 = float(input())
# print('Введите число 2: ')
# number_2 = float(input())
# print('Сумма чисел равна: ', number_1 + number_2)
# print('Разность чисел равна: ', number_1 - number_2)
# print('Произведение чисел равно: ', number_1 * number_2)
# print('Частное от деления чисел равно: ', number_1 / number_2)
# print('Введите степень числа: ')
# number_3 = float(input())
# print('Число 1 в степени равно: ', number_1 ** number_3)
# print('Число 2 в степени равно: ', number_2 ** number_3)
# print('Результат целочисленного деления чисел равен: ', number_1 // number_2)
# print('Остаток от деления чисел равен: ', number_1 % number_2)

# print('Задача НТ_1_3:')
# print('Введите сколько яблок было у Анны: ')
# a = int(input())
# print('Введите сколько яблок съел Пол: ')
# b = int(input())
# print('Остаток яблок составил', a - b, 'шт.')

# print('Задача НТ_1_4:')
# S = 200
# V1 = 50
# V2 = 50
# V3 = 75
# t = (S / (V1 + V2))
# print("До встречи поездов муха пролетит расстояние в", V3 * t, 'км.')

# print('Задача НТ_1_5:')
# S = 20
# S_first_day = 2
# S_other_days = 2 - 1
# print('Улитка доберется до вершины на', int((S - S_first_day) / S_other_days + 1), 'день.')

# print('Задача 2.2 (вариант 1):')
# g = '*****'
# print(' ', g[3])
# print('', g[1], g[4])
# print(g[0], ' ', g[4:])
# print(g)

# print('Задача 2.2 (вариант 2):')
# g = '*'
# print(' ', g)
# print('', g, g, sep=' ')
# print(g, ' ', g)
# print(g * 5)

# print('Задача 2.7 (вариант 1):')
# str_1 = 'program'
# print('количетво букв "r" в слове "program": ', str_1.count('r', 0, 8))
# print('индексы буквы "r" в слове "program": ', str_1.find('r'), str_1.rfind('r'))

# print('Задача 2.7 (вариант 2):')
# str_1 = 'program'
# print(str_1.find('r'), str_1.rfind('r'))

# print('Задача 2.8 (вариант 1):')
# str_1 = 'love'
# str_2 = 'python'
# print(str_1.index('o') + str_2.index('o'))

# print('Задача 2.8 (вариант 2):')
# str_1 = 'love'
# str_2 = 'python'
# print(str_1.rindex('o') + str_2.rindex('o'))

# print('Задача 2.9:')
# str_1 = '1'
# str_2 = '123'
# print(str_1 in str_2)
# print(str_2 in str_1)

# print('Задача 2.10 (вариант 1):')
# str_1 = 'Today is Monday'
# str_2 = 'Tomorrow is Friday'
# print(str_1.replace('Monday', 'Friday'))
# print(str_2.replace('Friday', 'Monday'))

# print('Задача 2.10 (вариант 2):')
# str_1 = 'Today is Monday'
# str_2 = 'Tomorrow is Friday'
# print(str_1.replace('Monday', 'Friday'), '\n', str_2.replace('Friday', 'Monday'))

# print('Задача 2.11:')
# str_1 = 'Anna loves music! She plays the piano very well! Look!'
# str_2 = str_1.replace('! ', '!*', 2)
# print(str_2.split('*'))

# print('Задача 2.12:')
# print('Введите имя: ')
# name = input()
# print('Введите наименование товара: ')
# product = str(input())
# print('Введите количество товара, шт.: ')
# amount_product = int(input())
# print(f'{name}, я тебе купил {product}, {amount_product} штук.')

# print('Задача 2.13:')
# str_1 = str(input())
# str_2 = str_1[::-1]
# print(str_1 in str_2)

# print('Задача 2.14:')
# print('Введите адрес электронной почты: ')
# email = str(input())
# index = email.index('@')
# print(email[:index] + email[index + 1:])

# print('Задача 2.15:')
# str_1 = str(input())
# element = str(input())
# print(str_1.count(element))

# print('Задача НТ_2_1:')
# str_1 = 'rythm rough rush shake than'
# print(str_1.replace('a', ''))
# print(str_1.count('a'))

# print('Задача НТ_2_2:')
# str_1 = 'rythm (rough rush shake) than'
# print(str_1[:str_1.index('(')] + str_1[str_1.index(')')+2:])

# print('Задача НТ_2_3:')
# str_1 = 'rythm rough rush shake than'
# print(str_1.count('t'))

# print('Задача НТ_2_4:')
# str_1 = 'rythm rough rush shake than'
# index_1 = str_1.index('h')
# index_2 = str_1.rindex('h')
# str_2 = str_1[index_1 + 1 : index_2]
# print(str_2[::-1])

# print('Задача НТ_2_5:')               
# str_1 = 'rythm rough rush shake than'
# index_1 = str_1.index('h')
# index_2 = str_1.rindex('h')
# str_2 = str_1[index_1 + 1 : index_2]
# print(str_1[:index_1 + 1] + str_2.replace('h', 'H') + str_1[index_2:])
