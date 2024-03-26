from random import random
import ctypes  # для вывода в консоль на windows


kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


class Field:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        # Создание основного поля
        self.field = ()
        for _ in range(self.m):
            line = ()
            for _ in range(self.n):
                line += (self.first_era(), )
            self.field += (line, )
        # Создание нового поле
        self.new_field = []
        for _ in range(self.m):
            line = []
            for _ in range(self.n):
                line += ['0']
            self.new_field += [line]

    def __next__(self):
        # Итерация по основному полю
        for line_id, line in enumerate(self.field):
            for el_id, el in enumerate(line):
                self.new_field[line_id][el_id] = el.fate(self.neighbors(line_id, el_id))
        # Перенос значений из нового поля в основное
        self.field = ()
        for line in self.new_field:
            self.field += (tuple(line),)

    def neighbors(self, y, x):
        n = []
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if (i == y and j == x) or i < 0 or j < 0:
                    continue
                try:
                    n.append(str(self.field[i][j]))
                except IndexError:
                    pass
        return n

    def first_era(self):
        prob = random()
        if prob < 0.50:
            return Cell()  # Пустая
        elif prob < 0.75:
            return Civilian()  # Жизнь
        elif prob < 0.85:
            return Maniac()  # Маньяк
        else:
            return Frank()  # Виктор Франкенштейн

    def __str__(self):  # Вывод поля
        def pr(a):
            for line in a:
                for elem in line:
                    yield str(elem) + ' '
                yield '\n'
        out = ''
        for i in pr(self.field):
            i = str(i)
            if i == 'М ':
                i = f"\033[31m{'М '}"
            elif i == 'Ф ':
                i = f"\033[34m{'Ф '}"
            elif i == '* ':
                i = f"\033[32m{'* '}"
            elif i == '# ':
                i = f"\033[37m{'# '}"
            out += i
        return out


class Cell:
    def __init__(self):
        self.cage = '#'

    def birth(self):
        prob = random()
        if prob < 0.75:
            return Civilian()
        elif prob < 0.85:
            return Maniac()
        else:
            return Frank()

    def fate(self, n):
        if n.count('Ф') + n.count('М') + n.count('*') == 3:
            return self.birth()
        elif 'Ф' in n and random() < 0.20:
            return self.birth()
        else:
            return Cell()

    def __str__(self):
        return self.cage


class Civilian(Cell):
    def __init__(self):
        super().__init__()
        self.cage = '*'

    def fate(self, n):
        if n.count('Ф') + n.count('М') + n.count('*') == 3 or n.count('Ф') + n.count('М') + n.count('*') == 2:
            if 'М' in n and random() < 0.25:
                return Cell()
            else:
                return Civilian()
        else:
            return Cell()

    def __str__(self):
        return self.cage


class Maniac(Cell):
    def __init__(self):
        super().__init__()
        self.cage = 'М'

    def fate(self, n):
        if n.count('#') == len(n):
            return Cell()
        elif 'М' in n and random() < 0.25:
            return Cell()
        else:
            return Maniac()

    def __str__(self):
        return self.cage


class Frank(Cell):
    def __init__(self):
        super().__init__()
        self.cage = 'Ф'

    def fate(self, n):
        if '#' not in n:
            return Cell()
        elif 'М' in n and random() < 0.25:
            return Cell()
        else:
            return Frank()

    def __str__(self):
        return self.cage


N, M = map(int, input('Введите размеры поля (Ш В): ').split())
field = Field(N, M)
era = 0
while True:
    era += 1
    print(f'\nЭпоха № {era}\n')
    print(field, f"\033[0m{''}")
    inp = input('Нажмите \033[4mEnter\033[0m для перехода на следующую эпоху. '
                'Зажмите его для быстрого движения по эпохам. '
                'Ведите \033[4mВЫХОД\033[0m, если хотите выйти: ')
    if inp == '':
        next(field)
    elif inp == 'ВЫХОД':
        print("\n\033[35mВЫ ВЫШЛИ ИЗ ИГРЫ\n\033[0m")
        break
