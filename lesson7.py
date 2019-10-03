import random

class Card:
    def __init__(self, max):
        self._point = 0  # счётчик, количество набранных очков (зачёркнутых цифр)
        self._l_number = []
        if max > 15:
            self._max = max # максимальное количество бочонков
        else:
            self._max = 15
        self._l_number = self._init_l_number() # список цифр карты

    @property
    def l_number(self):
        return l_number

    def check_digit(self, digit): # проверка принадлежности бачонка с цифрй к карте
        if digit in self._l_number:
            self._l_number[self._l_number.index(digit)] = '-'
            return True

    def add_point(self): # метод инкриментрующий счётчик подсчёта заччёркнутых цифр
        self._point += 1

    @property
    def point(self): # метод, возвращающий количество зачёркнутых цифр
        return self._point

    def check_point(self): # метод, проверяющий, все ли цифры вычеркнуты из карты
        return self._point == 15

    def _init_l_number(self): # инициализация карты
        list = []
        for _ in range(3): # цикл по строкам
            l_index_excluded = []
            for _ in range(4): # генерируем индексы 4ёх исключений для строки
                while True:
                    e = random.randint(0, 8)
                    if e not in l_index_excluded:
                        break
                l_index_excluded.append(e)
            for j in range(9): # цикл по столбцам
                if j in l_index_excluded:
                    n = ' '
                else:
                    while True:
                        n = random.randint(1, self._max)
                        if n not in list:
                            break
                list.append(n)
        return list

    def show(self): # вывод текущего состояния карты на экран
        print(f'{self.name}'.center(26, '-'))
        for i, d in enumerate(self._l_number):
            print(str(d).rjust(2, ' '), end = ' ')
            if (i + 1) % 9  == 0:
                print()
        print('--------------------------')

class PlayerCard(Card):
    def __init__(self, max):
        super().__init__(max)
        self.name = 'Карточка игрока'

class ComputerCard(Card):
    def __init__(self, max):
        super().__init__(max)
        self.name = 'Карточка компьютера'

class Game:
    def __init__(self, max = 90):
        if max > 15:
            self._max = max # максимальное количество бочонков
        else:
            self._max = 15
        self._ost = max # счётчик оставшхся бочонков
        self._out_num = [] # список бочонков, которые уже в игре

    def _gen_key(self): # генератор следующего бочонка
        while True:
            i = random.randint(1, self._max)
            if i not in self._out_num:
                self._out_num.append(i)
                self._ost -= 1
                return i

    def start(self): # старт игры
        p_card = PlayerCard(self._max)
        c_card = ComputerCard(self._max)

        while True:
            print(f'Счёт {p_card.point}:{c_card.point}')
            key = self._gen_key()
            print(f'Новый бочонок: {key} (осталось {self._ost})')
            p_card.show()
            c_card.show()

            while True:
                inp = input('Зачеркнуть цифру? (y/n)')
                if inp in ['n', 'y']:
                    break
                else:
                    print('Ошшибка ввода')
                    continue

            if inp == 'y':
                 if p_card.check_digit(key):
                     p_card.add_point()
                 else:
                     print('Вы ошиблись, игра закончена')
                     break
            elif inp == 'n':
                 if p_card.check_digit(key):
                     print('Вы ошиблись, игра закончена')
                     break

            if c_card.check_digit(key):
                c_card.add_point()

            p_cp = p_card.check_point()
            c_cp = c_card.check_point()

            if p_cp and c_cp:
                print('Ничья')
                break
            elif p_cp:
                print('Игрок выиграл')
                break
            elif c_cp:
                print('Компьютер выиграл')
                break

game = Game()
game.start()