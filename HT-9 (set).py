# HT_9_1 На вход программа принимает две строки и выводит их общие символы.
#
# a = set(input())
# b = set(input())
# set_1 = a ^ b
# print(set_1)

# HT_9_2 На вход программа принимает две строки и выводит все символы из второй строки, которых нет в первой.

# a = set(input())
# b = set(input())
# set_1 = b.difference(a)
# print(set_1)

# HT_9_3 Написать задачу со множеством. Представление: условия и решение.
# Вход строка: пословица: «рожь две недели зеленеет, две недели колосится, две недели отцветает,
# две недели наливает, две недели подсыхает». Вывести количество уникальных букв в пословице.
#
# proverb = '''рожь две недели зеленеет,
# две недели колосится,
# две недели отцветает,
# две недели наливает,
# две недели подсыхает'''
#
# proverb_1 = set(proverb)
# proverb_1.remove(' ')
# proverb_1.remove(',')
# proverb_1.remove('\n')
# print(len(proverb_1))
# print(proverb_1)

