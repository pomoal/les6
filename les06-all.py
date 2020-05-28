# Практическое задание
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.
#
# import time
#
#
# class TrafficLight(object):
#     def __init__(self):
#         self.color = "Red"
#
#     def running(self):
#         Color = ["Red", "Yellow", "Green"]
#         TrafficDelay = [7, 2, 4]
#         temp_index = Color.index(self.color)
#         print(f"Цвет светофора:{self.color}, будет гореть {str(TrafficDelay[temp_index])}с")
#         time.sleep(TrafficDelay[temp_index])
#
#         if temp_index == 2: self.color = "Red"
#         else:
#             temp_index += 1
#             self.color = Color[temp_index]
#
# Traffic = TrafficLight()
# print(Traffic.color)
# while True:
#     # if input('Выход - Q, \nЛюбая клавиша - продолжить: ').upper() == 'Q':
#     #     break
#     Traffic.running()


#
# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т
#
#

# class road:
#     def __init__(self, length, width, thickness=0.05, layer_weight=25):
#         self._lenght = length
#         self._width = width
#         self._Thickness = thickness
#         self.layer_weight = layer_weight
#
#     def calcweight(self):
#         self.weight = self._width * self._lenght * self._Thickness * self.layer_weight
#         print(f"Масса полотна:{self._width}м*{self._lenght}м*{self._Thickness}м*{self.layer_weight}кг={self.weight}кг")
#
# road = road(20,5000)
# road.calcweight()



# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
#
#
# class Worker:
#     def __init__(self, Name = None, Surname = None, position = None):
#         self.Name =  Name
#         self.Surname = Surname
#         self.position = position
#         self._wage = 12750
#         self._bonus = 5000
#         self.__income = {"wage": self._wage, "bonus": self._bonus}
#     def get_worker_info(self):
#         print(f"Фамилия:{self.Surname}\nИмя:{self.Name}\n")
#
# class Position(Worker):
#     def get_total_income(self):
#         set_temp = self._Worker__income
#         return int(set_temp.get("wage"))+int(set_temp.get("bonus"))
#     def get_full_name(self):
#         print(f"Имя:{self.Name}\nФамилия:{self.Surname}")
#
# new_worker = Position("Anton", "Tarasov")
# new_worker.get_full_name()
# income = new_worker.get_total_income()
# income_two = new_worker.get_total_income()
# print(f"Зарплата:{income}")

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
# name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
#
# class Car:
#     def __init__(self, name=None, speed=None, color=None, is_police=False):
#         self.name = name
#         self.speed = speed
#         self.color = color
#         self.is_police = is_police
#
#     def go(self):
#         print(f"Автомобиль {self.name} поехал.")
#
#     def stop(self):
#         print(f"Автомобиль {self.name} остановился.")
#
#     def turn(self):
#         rotation = {
#             "A":"Налево",
#             "D":"Направо",
#             "X":"Разворот"
#         }
#         key_pressed = input('A - Налево, Направо - D \nЛюбая другая клавиша - прямо: ').upper()
#         et_rot = rotation.get(key_pressed)
#         print(et_rot)
#         if et_rot == None:
#             print("Едем прямо!")
#         else:
#             print(f"Автомобиль {self.name} повернул {et_rot}.")
#
#     def show_speed(self):
#         print(f"Скорость автомобиля {self.name} - {self.speed}км/ч")
#
# class TownCar(Car):
#     def show_speed(self):
#         print(f"Скорость автомобиля {self.name} - {self.speed}км/ч")
#         if int(self.speed) > 60: print(f"Автомобиль {self.name} едет с превышением!")
#
# class WorkCar(Car):
#     def show_speed(self):
#         print(f"Скорость автомобиля {self.name} - {self.speed}км/ч")
#         if int(self.speed) > 40: print(f"Автомобиль {self.name} едет с превышением!")
#
# class SportCar(Car):
#     def show_speed(self):
#         print(f"Скорость автомобиля {self.name} - {self.speed}км/ч")
#         if int(self.speed) > 40: print(f"Автомобиль {self.name} едет с превышением!")
#
# class PoliceCar(Car):
#     def __init__(self, name=None, speed=None, color=None, is_police=True):
#         self.name = name
#         self.speed = speed
#         self.color = color
#         self.is_police = is_police
#     def show_speed(self):
#         if int(self.speed) > 90: print(f"Автомобиль полиции {self.name} цвета - {self.color} едет с превышением!")
#
# new_car = Car("жЫп","130","Red")
# new_car.turn()
# new_car.show_speed()
# police_car = PoliceCar("гранта", "120", "голубая")
#


#5.  Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title = None):
        self.title = title

    def draw(self):
        print(f"Рисуем, используя {self.title}.")

class Pen(Stationery):
    def __init__(self, title = "Ручка"):
        super().__init__(title)

    def draw(self):
        print(f"Рисуем, используя инструмент - шариковая {self.title}.")

class Pencil(Stationery):
    def __init__(self, title = "карандаш"):
        super().__init__(title)
    def draw(self):
        print(f"Рисуем, используя инструмент - твердый {self.title}.")

class Handle(Stationery):
    def __init__(self, title="маркер"):
        super().__init__(title)
    def draw(self):
        print(f"Рисуем, используя инструмент - перманентный {self.title}.")


first_pen = Pen()
first_pencil = Pencil()
first_handle = Handle()

first_pen.draw()
first_pencil.draw()
first_handle.draw()
