# 14.4 Добавьте в класс Person метод, который считает и выводит в каком году родился человек.
# Как параметр Вам понадобится текущий год. Создайте Васю и вызовите этот метод. Считается, что Васи
# уже был день рождения в этом году.
#
# class Person:
#
#     def __init__(self, name, lastname, age, sex):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.sex = sex
#
#     def year_born(self, current_year):
#         return current_year - self.age
#
#
# if __name__ == '__main__':
#     Vasya = Person("Вася", "Иванов", 47, "мужской")
#     print(Vasya.year_born(2022))


# 14.5 Добавьте в класс Porsche метод, который считает пробег, а также выводит пробег и сколько за сегодня проехал порш.
# Создайте 1 порш и 2 раза вызовите метод.
#
# class Porsche:
#     model = 'Panamera'
#
#     def __init__(self, power, engine):
#         self.power = power
#         self.engine = engine
#         self.mileage = 0
#
#     def count_mileage(self, km):
#         '''
#         считает пробег
#         :param km: километры
#         :return:
#         '''
#         self.mileage += km
#
#     def get_mileage(self):
#         '''
#         возвращает (печатает) пробег
#         :return:
#         '''
#         return self.mileage
#
# if __name__ == '__main__':
#     p1 = Porsche(400, 1.6)
#     p1.count_mileage(120)
#     p1.count_mileage(120)
#     print(p1.get_mileage())


# 14.6 Расширьте в классе Person метод, который считает год рождения: добавьте вывод, что человек пойдет в армию
# в таком-то году, если это мужчина допризывного возраста. Считается, что в армию забирают с 18 лет.
# Соз дайте Васю допризывного возраста и Катю. Вызовите для каждого объекта этот метод.
#
# class Person:
#
#     def __init__(self, name, lastname, age=1, sex='male'):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.sex = sex
#
#     def year_born(self, current_year):
#         return current_year - self.age
#
#     def army(self, current_year):
#         if self.sex == 'male' and self.age < 18:
#             return f'Пойдет в армию в {current_year - self.age + 18} году'
#         else:
#             return f'Не пойдет в армию'
#
#
# if __name__ == '__main__':
#     Kate = Person('Kate', 'Borisova', 25, 'woman')
#     Vasya = Person("Vasya", "Ivanov", 16)
#     print(Kate.army(2022))
#     print(Vasya.army(2022))
