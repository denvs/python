# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self):
        self.speed = 60
        self.color = 'green'
        self.name = 'TownCar'
        self.is_police = False
        print(self.name, self.color, self.speed, self.is_police)

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print(f'turn {direction}');

class SportCar:
    def __init__(self):
        self.speed = 100
        self.color = 'red'
        self.name = 'SportCar'
        self.is_police = False
        print(self.name, self.color, self.speed, self.is_police)

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print(f'turn {direction}');

class WorkCar:
    def __init__(self):
        self.speed = 60
        self.color = 'blue'
        self.name = 'WorkCar'
        self.is_police = False
        print(self.name, self.color, self.speed, self.is_police)

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print(f'turn {direction}');

class PoliceCar:
    def __init__(self):
        self.speed = 100
        self.color = 'white'
        self.name = 'PoliceCar'
        self.is_police = True
        print(self.name, self.color, self.speed, self.is_police)

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print(f'turn {direction}');

my_town_car = TownCar()
my_sport_car = SportCar()
my_work_car = WorkCar()
my_police_car = PoliceCar()

my_town_car.go()
my_town_car.turn('left')
my_town_car.stop()

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print(f'turn {direction}');

class TownCar(Car):
    def __init__(self):
        self.speed = 60
        self.color = 'green'
        self.name = 'TownCar'
        self.is_police = False
        print(self.name, self.color, self.speed, self.is_police)

class SportCar(Car):
    def __init__(self):
        self.speed = 100
        self.color = 'red'
        self.name = 'SportCar'
        self.is_police = False
        print(self.name, self.color, self.speed, self.is_police)

class WorkCar(Car):
    def __init__(self):
        self.speed = 60
        self.color = 'blue'
        self.name = 'WorkCar'
        self.is_police = False
        print(self.name, self.color, self.speed, self.is_police)

class PoliceCar(Car):
    def __init__(self):
        self.speed = 100
        self.color = 'white'
        self.name = 'PoliceCar'
        self.is_police = True
        print(self.name, self.color, self.speed, self.is_police)

my_town_car = TownCar()
my_sport_car = SportCar()
my_work_car = WorkCar()
my_police_car = PoliceCar()

my_town_car.go()
my_town_car.turn('left')
my_town_car.stop()