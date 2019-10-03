# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name):
        self.name = name
    # Функция для подсчета урона
    def _calculate_damage(self, armor):
        return self.damage // armor
    # Функция атаки, принимает на вход 2 структуры
    def attack(self, defend):
        damage = self._calculate_damage(defend.armor)
        defend.health -= damage
        print('{} нанес {} урона {}, у того осталось {} жизней.'.format(self.name, defend.name, damage, defend.health))

class Player(Person):
    def __init__ (self, name):
        super().__init__(name)
        self.health = 100
        self.damage = 50
        self.armor = 0.7
class Enemy(Person):
    def __init__ (self, name):
        super().__init__(name)
        self.health = 100
        self.damage = 50
        self.armor = 0.7


# Функция старта игры, никаких аргументов не принимает.
def start_game():
    # получаем наши структуры, через вышеописанную функцию
    player = Player('Player')
    enemy = Enemy('Enemy')

    # Запоминаем кто последний атаковал
    last_attacker = player
    while player.health > 0 and enemy.health > 0:
        if last_attacker == player:
            enemy.attack(player)
            last_attacker = enemy
        else:
            player.attack(enemy)
            last_attacker = player

    if player.health > 0:
        print('Игрок победил!')
    else:
        print('Враг победил!')

start_game()
