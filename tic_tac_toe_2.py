def greet():                      # Создаём функцию для приветствия игрока
    print("-------------------")
    print("  Добро пожаловать ")
    print("      в игру       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def show():                       # Создаём функцию для отображения поля игры
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def ask():                        # Создаём функцию для ввода со стороны
    while True:                   # игрока и для проверки введённых данных
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:       # Проверяем на наличие обеих координат,
            print(" Введите 2 координаты! ")  # введённых игроком
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):  # Проверяем на наличие ввода от игрока
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:        # Устанавливаем диапазон для введённых данных
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":                      # Проверяем клетку на занятость
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():                  # Создаём функцию для проверки выигрышных комбинаций
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


greet()
field = [[" "] * 3 for i in range(3)]  # Создаём пустое игровое поле
count = 0
while True:
    count += 1                         # С помощью счётчика определяем, чей ход
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()                       # Запрашиваем у функции ввода переменные x/y

    if count % 2 == 1:                 # С помощью счётчика определяем, чем заполняется ячейка
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():                    # Проверяем на выигрышные комбинации
        break

    if count == 9:                     # Проверяем на ничью
        print(" Ничья!")
        break
