# Задача 3.1: Вход: несолько цветов. Программа должна добавлять в начало списка еще несколько цветов.

# colors_1 = [input('Введите ваши любимые цвета: ')]
# colors_2 = input('введите еще несколько цветов: ')
# colors_1.insert(0, colors_2)
# print(colors_1)

# colors_1 = ['red', 'yellow', 'blue']
# colors_2 = ['green', 'gray']
# colors_1.insert(0, colors_2)
# print(colors_1)

# Задача 3.2: Вход: число 0. Программа создает список, заполненный нулями, кроме первого и последнего элементов.

# num_1 = '0'
# num_2 = int(input('введите количество элементов списка: '))
# ls = list(num_1 * num_2)
# ls[0] = ''
# ls[-1] = ''
# print(ls)

# 3.4 Вход: несколько цветов. Программа должна заменять 2-ой элемент на ‘yellow’.

# colors = [input('введите цвет 1: '), input('введите цвет 2: '), input('введите цвет 3: '), input('введите цвет 4: ')]
# colors[1] = 'yellow'
# print(colors)

# 3.6 Вход: список ['cat', 'rabbit', 'elephant’]. Программа делает из него 2 списка:
# 1.  Содержит животное и количество букв в его имени. 2. Содержит животных,где последняя буквы заглавная

# animals = ['cat', 'rabbit', 'elephant']
# animals_1 = animals.copy()
# animals_1.insert(1, len(animals_1[0]))
# animals_1.insert(3, len(animals_1[2]))
# animals_1.insert(5, len(animals_1[4]))
# print(animals_1)
# el1 = animals[0]
# el2 = animals[1]
# el3 = animals[2]
# el1 = (el1[::-1].capitalize())[::-1]
# el2 = (el2[::-1].capitalize())[::-1]
# el3 = (el3[::-1].capitalize())[::-1]
# print([el1, el2, el3])

# 3.7 Вход: список чисел и еще одна цифра. Программа проверяет есть ли введенная цифра в списке чисел.

# numbers_1 = input('Введите несколько чисел: ')
# list(numbers_1)
# number_2 = input('Введите любую цифру: ')
# print('Наличие цифры в числах: ', number_2 in numbers_1)

# 3.8 Вход: список ['dog', 'cat', 'rat', 'rabbit'].
# Программа делает из него список ['rat', 'rabbit', 'pig', 'dog', 'cat'].

# animals = ['dog', 'cat', 'rat', 'rabbit']
# animals[-1], animals[1] = animals[1], animals[-1]
# animals[-2], animals[0] = animals[0], animals[-2]
# animals.insert(2, 'pig')
# print(animals)

# animals = ['dog', 'cat', 'rat', 'rabbit']
# animals.insert(0, 'rat')
# animals.insert(1, 'rabbit')
# animals.insert(2, 'pig')
# del animals[5:]
# print(animals)

# 3.9 Вход: список [1, 2, 3, 4, 5]. Программа создает такой же список из этого,
# удаляет в нем все элементы со 2-го до последнего. Проверяет, что это разные списки.

# numbers = [1, 2, 3, 4, 5]
# numbers_1 = numbers
# del numbers_1[1:4]
# print(numbers in numbers_1)

# 3.11 Вход: [1, 2, 3, 4, 5]. Программа находит их сумму.

# numbers = [1, 2, 3, 4, 5]
# print(sum(numbers))

# 3.14 Создать 2 списка чисел до 100: 1. Делятся на 10. 2. Делятся на 3.

# list_1 = list(range(10, 101, 10))
# print(list_1)
# list_2 = list(range(3, 100, 3))
# print(list_2)

# 3.15 Создать 2 списка: 1. [30, 28, 26, 24, 22, 20, 18, 16, 14]. 2.  Из первого списка сделать список [14, 16, 18].

# list_1 = list(range(30, 13, -2))
# print(list_1)
# list_2 = (list_1[-3:])
# list_2 = list_2[::-1]
# print(list_2)

# HT_3_1 Вход: разные слова. Программа создает из них список и выводит его задом наперед.

# words = [input('Введите слово 1:'), input('Введите слово 2:'), input('Введите слово 3:'), input('Введите слово 4:')]
# print(words[::-1])

# HT_3_2 Создать список из чисел от 0 до 10. Программа создает новый список, состоящий из
# минимального, максимального элементов и суммы чисел первого списка.
# *Попробуйте сделать в 3 строки кода, включая print().

# numbers = list(range(0, 11))
# numbers_1 = [min(numbers), max(numbers), sum(numbers)]
# print(numbers_1)

# HT_3_3 Вход: беспорядочный набор символов, например: ade rg gt5 re u. Заменить пробелы на
# * и посчитать сколько получилось *.

# symbols = (input('Введите любой набор символов'))
# symbols_1 = symbols.replace(' ', '*')
# print(symbols_1.count('*'))

# HT_3_4 Придумать задачу для использования методов строк. Минимум 2 – 3 метода. Задача
# должна содержать условие и Ваше решение.

# Создать переменную ps (пословица): «Рожь две недели зеленеет, две недели колосится, две недели отцветает,
# две недели наливает, две недели подсыхает»
# Программа: 1. выводит длину строки; 2. заменяет слова «две» на цифру «2»;
# 3. считает количество букв «е» до замены слов и после замены; 4. выводит все слова строки с заглавной буквы.

# ps = 'Рожь две недели зеленеет, две недели колосится, две недели отцветает, две недели наливает, две недели подсыхает'
# print(len(ps))
# print(ps.count('е'))
# ps = ps.replace('две', '2', ps.count('две'))
# print(ps.count('е'))
# print(ps.title())

# HT_3_5 Придумать задачу для использования методов списка. Минимум 2-3 метода. Задача
# должна содержать условие и Ваше решение.

# Вход: строка и список. Программа преобразует строку в список и объединяет два списка в один.
# Полученный список программа дополняет элементом «УРА» и выводит список, в котором все элементы
# расположены в обратном порядке.

# str_1 = input()
# ls_1 = list(input().split())
# str_1 = str_1.split()
# ls = ls_1 + str_1
# ls.append('УРА')
# print(ls[::-1])
