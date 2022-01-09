# 7.1 На вход программа получает имя, фамилию и адрес электронной почты от двух пользователей.
# Пользователь может вводить данные в любом порядке. Необходимо создать кортеж из почты обоих пользователей.
#
# user_1 = input('Введите имя, фамилию, адрес электронной почты: ').split()
# user_2 = input('Введите имя, фамилию, адрес электронной почты: ').split()
#
# tpl_mails = []
# for i in user_1:
#     if '@' in i:
#         tpl_mails.append(i)
# for i in user_2:
#     if '@' in i:
#         tpl_mails.append(i)
# tpl_mails = tuple(tpl_mails)
# print(tpl_mails)

# 7.2 Анна регистрируется на сайте. Ей надо ввести имя, фамилию, возраст и почту. Она ввела только
# "Anna" и почту. Необходимо создать кортеж из имени и почты.
#
# name = input('Введите имя: ').capitalize()
# surname = input('Введите фамилию: ').capitalize()
# age = input('Введите возраст (полных лет): ')
# email = input('Введите почту: ')
#
# tpl_person = []
#
# if len(name) > 0:
#     tpl_person.append(name)
# if len(surname) > 0:
#     tpl_person.append(surname)
# if len(age) > 0:
#     if age.isdigit():
#         tpl_person.append(age)
#     else:
#         print('Возраст введен некорректно!')
# if len(email) > 0:
#     tpl_person.append(email)
# tpl_person_1 = tuple(tpl_person)
# print(tpl_person_1)

# 7.3 На вход программа получает несколько чисел. Создать кортеж из чисел, кратных трем.
#
# nums = input('Введите несколько чисел: ').split()
# nums_1 = []
#
# for i in nums:
#     i = int(i)
#     if i % 3 == 0:
#         nums_1.append(i)
# nums_1 = tuple(nums_1)
# print(nums_1)

# 7.4 Создайте кортеж с числами от 0 до 9 и посчитайте сумму элементов.
#
# tpl = tuple(range(0, 10))
# print(tpl)
# print(sum(tpl))

# 7.5 Создайте кортеж с буквами. Посчитайте сколько гласных и выведите на экран в формате: "Буква а в кортеже
# встречается 1 раз".
#
# tpl = tuple(input('Введите слово или набор букв: ').lower())
# vowels = 'eyuioa'
# tpl_count = 0
#
# for i in tpl:
#     if i in vowels:
#         tpl_count += 1
# print(f'Гласных букв в кортеже {tpl_count} шт.')
# a = input('Введите гласную букву: ').lower()
# if a in tpl:
#     print(f'Буква {a} в кортеже встречается {tpl.count(a)} раз.')

# 7.6 Программа на вход получает среднюю температуру за несколько дней. Посчитайте среднюю температуру.
#
# temp = input('Введите ежедневную среднюю температуру за несколько дней: ').split()
# temp = tuple(temp)
# summ = 0
#
# for i in temp:
#     i = float(i)
#     summ += i
# print(f'Средняя температура за {len(temp)} дня (дней) составила {(summ / len(temp)):.2f} градусов')

# H_7_1 Создайте 2 кортежа с 10 случайными числами от -5 до 0. Объедините их и посчитайте сколько раз в
# получившемся кортеже встретится 0.
#
# import random
#
# iter = 1
# tpl_1 = []
# tpl_2 = []
#
# while iter <= 10:
#     tpl1 = random.randint(-5, 0)
#     tpl2 = random.randint(-5, 0)
#     iter += 1
#     tpl_1.append(tpl1)
#     tpl_2.append(tpl2)
# tpl_1 = tuple(tpl_1)
# tpl_2 = tuple(tpl_2)
# print('Кортеж 1:', tpl_1)
# print('Кортеж 2:', tpl_2)
# print('Объединенный кортеж: ', tpl_1 + tpl_2)
# print(f'Цифра НОЛЬ в объединенном кортеже встречается {(tpl_1 + tpl_2).count(0)} раз(а).')

# H_7_2 Создайте кортеж из 5 случайных чисел от 1 до 10. Все числа, кроме первого и последнего, распаковать
# в один список. Для распаковки используйте *.
#
# import random
#
# iter = 1
# tpl_1 = []
#
# while iter <= 5:
#     tpl = random.randint(1, 10)
#     iter += 1
#     tpl_1.append(tpl)
# tpl_1 = tuple(tpl_1)
# print('Кортеж:', tpl_1)
# a, *b, e = tpl_1
# print('Распаковка кортежа:', a, b, e, sep=' ')

# H_7_3 На вход программе подаются числа. Создайте кортеж из чисел меньше 5.
#
# nums = input('Введите несколько чисел: ').split()
# nums1 = []
#
# for i in nums:
#     i = int(i)
#     if i < 5:
#         nums1.append(i)
# nums1 = tuple(nums1)
# print(nums1)

# H_7_4  У вас есть кортеж, который содержит список. Измените кортеж так, чтобы список был пустым.
#
# ls = list(input('Введите список: '))
# ls1 = input('Введите что угодно: ')
# ls2 = input('Введите что угодно: ')
# tpl = tuple([ls])
# tpl1 = tuple(ls1)
# tpl2 = tuple(ls2)
# tpl_all = tpl + tpl1 + tpl2
# print(tpl_all)
# tpl_all[0][0:] = ''
# print(tpl_all)

# H_7_5 Написать задачу с кортежем. Задача должна содержать условие и решение.
# Вход строка: пословица: «Рожь две недели зеленеет, две недели колосится, две недели отцветает,
# две недели наливает, две недели подсыхает»
# Создать кортеж из букв, вывести количество букв «е» и индекс первой буквы «е».
#
# proverb = '''Рожь две недели зеленеет,
# две недели колосится,
# две недели отцветает,
# две недели наливает,
# две недели подсыхает'''
#
# proverb = tuple(proverb)
# print(proverb.count('е'))
# print(proverb.index('е'))

