# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.
#
import time


class TrafficLight(object):
    def __init__(self):
        self.color = "Red"

    def running(self):
        Color = ["Red", "Yellow", "Green"]
        TrafficDelay = [7, 2, 4]
        temp_index = Color.index(self.color)
        print(f"Цвет светофора:{self.color}, будет гореть {str(TrafficDelay[temp_index])}с")
        time.sleep(TrafficDelay[temp_index])

        if temp_index == 2: self.color = "Red"
        else:
            temp_index += 1
            self.color = Color[temp_index]

Traffic = TrafficLight()
print(Traffic.color)
while True:
    # if input('Выход - Q, \nЛюбая клавиша - продолжить: ').upper() == 'Q':
    #     break
    Traffic.running()

