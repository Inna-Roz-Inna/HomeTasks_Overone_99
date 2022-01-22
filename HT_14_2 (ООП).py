# HT_14_1
# Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
# Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
# Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.
#
# class Dog:
#
#     def __init__(self, height, weight, name, age):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#
#     def jump(self):
#         print(f'The Dog jumps high.')
#
#     def run(self):
#         print(f'The Dog runs fast.')
#
#     def bark(self):
#         print(f'The Dog barks loudly.')
#
#
# if __name__ == '__main__':
#     d = Dog(30, 9, 'Bim', 5)
#     print(f'Высота собаки {d.height} см. '
#           f'Вес собаки {d.weight} кг. '
#           f'Кличка собаки {d.name}. '
#           f'Возраст собаки {d.age} лет.')
#     d.jump()
#     d.run()
#     d.bark()


# HT_14_2
# Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут имени у объекта.
# Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.
#
# class Dog:
#
#     def __init__(self, height, weight, name, age):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#
#     def jump(self):
#         print(f'The Dog jumps high.')
#
#     def run(self):
#         print(f'The Dog runs fast.')
#
#     def bark(self):
#         print(f'The Dog barks loudly.')
#
#     @staticmethod
#     def change_name(new_name):
#         print(f"The new Dog's name is {new_name}.")
#
#
# if __name__ == '__main__':
#     d = Dog(30, 9, 'Bim', 5)
#     print(f'Dog name is {d.name}.')
#     d.change_name('Lord')


# 14.7 Создайте многоэтажный дом. Атрибуты: количество квартир. Методы: нанять вахтершу.
#
# class MultistoryHouse:
#
#     def __init__(self, rooms):
#         self.rooms = rooms
#
#     def watchman(self):
#         print(f'There is a watchman in this house.')
#
#
# if __name__ == '__main__':
#     mh = MultistoryHouse(858)
#     print(f'There are {mh.rooms} rooms in multistory house.')
#     mh.watchman()


# 14.8 Создайте класс для салона красоты, чтобы можно было создавать дома с салоном красоты.
# Методы: маникюр, стрижка. Методы прописывать не надо, просто поставить заглушку.
#
# class SalonMixin:
#
#     def manicure(self):
#         pass
#
#     def haircut(self):
#         pass

# 14.9 Добавьте в салон красоты метод salon_opening_hours, который сообщает салон открыт или закрыт.
# Создайте дом с салоном красоты. Атрибуты: час открытия салона, час закрытия салона.
# Посмотрите работает ли салон в 13 часов, а в 23?
#
# class MultistoryHouse:
#
#     def __init__(self, rooms):
#         self.rooms = rooms
#
#     def watchman(self):
#         print(f'There is a watchman in this house.')
#
#
# class SalonMixin:
#
#     def manicure(self):
#         pass
#
#     def haircut(self):
#         pass
#
#     def salon_opening_hours(self, now_time):
#         if now_time < self.open_time or now_time > self.close_time:
#             print(f'The Salon is closed')
#         else:
#              print(f'The Salon is open')
#
#
# class HouseWithSalon(MultistoryHouse, SalonMixin):
#
#     def __init__(self, open_time, close_time):
#         self.open_time = open_time
#         self.close_time = close_time
#
#
# if __name__ == '__main__':
#     mhs = HouseWithSalon(10, 22)
#     mhs.salon_opening_hours(13)
#     mhs.salon_opening_hours(23)