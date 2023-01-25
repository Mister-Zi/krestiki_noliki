def hi():
    print('                        ')
    print('                        ')
    print('     Привет, друг!      ')
    print('Добро пожаловать в игру')
    print('   Крестики - нолики    ')
    print('                        ')
    print('                        ')

def pravila():
    door=input('Если хочешь ознакомится с правила игры, то нажми "y", если ты матерый проффесионал, то скипай и нажимай "n" '
                '\n"y" означает - да, а "n" означает нет.'
                "                                        "
                '\nВведите данные;')
    if door == "y":
        print('')
        print(
            'Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики).'
            '\nПервый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.\n'
            'Первый ход делает игрок, ставящий крестики.')
        input('Что бы пойти дальше нажми "Enter"')
        print('')
        print('')

def pravila2():
    print('')
    print('Что ОБЯЗАТЕЛЬНО нужно знать перед игрой:')
    print('x - номер строки')
    print('y - номер столбца')
    print('Формат ввода x y ')
    print('Пример: 1 1')
    print("        y   y   y  ")
    print('      | 0 | 1 | 2 | ')
    print('  ----------------')
    print('x | 0 |   |   |   |')
    print('  ----------------')
    print('x | 1 |   | X |   |')
    print('  ----------------')
    print('x | 2 |   |   |   |')

def previe():
        print("       ")
        print('   | 0 | 1 | 2 | ')
        print('  --------------')
        for i, row in enumerate(field):
            row_str=f" {i} | {' | '.join((row))} | "
            print(row_str)
            print('  --------------')
        print()

def game():
    while True:
        hod = input("          Ваш ход: ").split()
        if len(hod) !=2:
            print("Введите 2 координаты! ")
            continue

        x, y = hod
        if not(x.isdigit()) or not (y.isdigit()):
            print("Введите числа! ")
            continue

        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты введены неверно. Попробуй ещё раз!")
            continue

        if field[x][y] != " ":
            print("Клетка занята! Выберите другую клетку!")
            continue
        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True
    return False

hi()
propusk=input("Нажми 'Enter' для продолжения")
pravila()
pravila2()
input('Готов? жми на "Enter"')
field = [[" "]* 3 for i in range(3)]
num = 0
while True:
    num += 1
    previe()
    if num % 2 == 1:
        print(' Ходит крестик')
    else:
        print(' Ходит нолик')
    x, y = game()
    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if check_win():

        break
    if num == 9:
        print('Ничья!')
        break



