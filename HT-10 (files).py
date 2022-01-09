# 10.1 Создать список из 10 случайных чисел. Записать в файл:
# 1. Количество элементов в списке; 2. Все элементы списка в одну строку.
# Т.е. в файле должно быть 2 строки.
#
# import random
#
# ls = []
# for i in range(10):
#     r = random.randint(1, 101)
#     ls.append(r)
#     i += 1
# print(ls)
#
# with open('HT_10_file_1.txt', 'w') as f:
#     f.write(f'{len(ls)}\n')
#     for i in ls:
#         f.write(str(i) + ' ')

# 10.2 Прочитать из файла числа, сформировать список и напечатать его.
#
# with open('HT_10_file_1.txt', 'r') as f:
#     line = f.read()
# ls = [int(i) for i in line.split()]
# print(ls)

# 10.3 Дан словарь: days = {1:'Sun', 2:'Mon', 3:'Tue', 4:'Wed', 5:'Thu', 6:'Fri', 7:'Sat'}
# Записать его в файл построчно.
#
# days = {1: 'Sun', 2: 'Mon', 3: 'Tue', 4: 'Wed', 5: 'Thu', 6: 'Fri', 7: 'Sat'}
#
# with open('HT_10_file_2.txt', 'w') as f:
#     for k, v in days.items():
#         f.write(f'{k}: {v} \n')

# 10.4 Прочитать предыдущий файл, сформировать из него словать, распечатать его.
#
# with open('HT_10_file_2.txt', 'r') as f:
#     lines = f.read().splitlines()
# dic = {}
# for line in lines:
#     k, v = line.split(': ')
#     dic.update({int(k): v})
# print(dic)

# 10.5 Создать множество отрицательных и положительных чисел. Записать его в файл построчно.
#
# ls = set(int(i) for i in input('введите целые числа: ').split())
# print(ls)
# with open('HT_10_file_3.txt', 'w') as f:
#     for i in ls:
#         f.write(str(i) + '\n')

# 10.6 Прочитать предыдущий файл, сформировать из него множество, распечатать его.
# with open('HT_10_file_3.txt', 'r') as f:
#     line = f.read()
#     ls = set([int(i) for i in line.split()])
#     print(ls)

# 10.7 Пользователь вводит слова. Записать их в файл: каждое слово на отдельной строке.
#
# ls = input('введите несколько слов: ').split()
# print(ls)
# with open('HT_10_file_4.txt', 'w') as f:
#     for i in ls:
#         f.write(i + '\n')

# 10.8 Дан список [5, True, 'abc']. Записать его в файл.
#
# ls = [5, True, 'abc']
# with open('HT_10_file_5.txt', 'w') as f:
#     for i in ls:
#         f.write(str(i) + '\n')

# 10.9 Создать список чисел. Записать каждое нечетное число в файл.
#
# ls = [int(i) for i in input('введите список чисел: ').split()]
# print(ls)
# with open('HT_10_file_6.txt', 'w') as f:
#     for i in ls:
#         if i % 2 != 0:
#             f.write(str(i) + '\n')

