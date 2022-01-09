# H_13_1 Из полученного списка чисел создайте список с суммами этих чисел, отсортированными по возрастанию.
# In: 965 582 023 8 695210
# Out: [5, 8, 15, 20, 23]
#
# ls_1 = [int(i) for i in input().split()]
#
# def new_list_summ(ls):
#     '''
#     Функция из заданного списка создает новый список отсортированных по возрастанию сумм чисел заданного списка.
#     :param ls: список чисел.
#     :return: новый список чисел, отсортированных по возрастанию.
#     '''
#     ls_2 = []
#     for i in ls:
#         summ = 0
#         while i != 0:
#             last = i % 10
#             summ += last
#             i = i // 10
#         ls_2.append(summ)
#     return sorted(ls_2)
# print(new_list_summ(ls_1))

# H_13_2 Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
# f(x)=1-((x+2) в квадрате) при условии x меньше-равно "-2", f(x)=-(x/2) при условии x меньше-равно "2" и больше "-2",
# f(x)=((x+2) в квадрате)+1 при условии x больше "2".
# In: 4.5
# Out: 7.25
#
# a = float(input())
#
# def f(x):
#     '''
#     Функция возвращает результат решения уравнения при определенном условии.
#     :param x: любое число.
#     :return: возвращает результат в зависимости от того, какому условю отвечает введенное число.
#     '''
#     if x <= -2:
#         return 1 - (x + 2) ** 2
#     elif -2 < x <= 2:
#         return - x / 2
#     elif 2 < x:
#         return (x - 2) ** 2 + 1
#
# print(f(a))

# H_13_3 Напишите функцию, которая принимает на вход список целых чисел, удаляет из него все нечетные значения,
# а четные нацело делит на два.
# In: 852 85 784 58
# Out: [426, 392, 29]
#
# ls_1 = [int(i) for i in input().split()]
#
# def new_list_divide_two(ls):
#     '''
#     Функция из заданного списка создает новый список из четных чисел, деленных на два.
#     :param ls: список целых чисел.
#     :return: список четных чисел из заданного списка, деленных на два.
#     '''
#     ls_2 = []
#     for i in ls:
#         if i % 2 == 0:
#             ls_2.append(i // 2)
#     return ls_2
#
# print(new_list_divide_two(ls_1))