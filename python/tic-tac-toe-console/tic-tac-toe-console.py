# флаг окончания игры и выхода из цикла
game_end = False
fields = []
move_sign = 'x' # x/0
move_count = 0
# рисуем таблицу
def drawing_table():
    print('  1 2 3')
    for r in range(len(fields)):
        print_row = str(r+1)
        for val in fields[r]:
            print_row = print_row +' ' + val
        print(print_row)
# очищаем таблицу
def clear_table():
    global fields, game_end
    game_end = False
    # инициировали массив
    fields =  [['-'] * 3 for i in range(3) ]
    move_count = 0
    drawing_table()
# переключаем символ игрока
def switch_sign():
    global move_sign
    if move_sign == 'x':
        move_sign = '0'
    else:
        move_sign = 'x'
# устанавливаем значение массива
def set_table(x_val, y_val ):
    global fields, move_sign, move_count
    if fields[x_val][y_val]== '-':
        fields[x_val][y_val] = move_sign
        move_count = move_count + 1
    else:
        print("!!! Клетка уже заполнена !!!")
        raise Exception("Значение заполнено")
# запрашиваем ввод данных
def input_data():
    global move_sign
    try:# тут можно переписать без try  но пусть пока так
        if move_sign == 'x':
            x_val, y_val = input("Введите координаты ходит КРЕСТИК: ").split()
        else:
            x_val, y_val = input("Введите координаты ходит НОЛИКИ: ").split()
        if x_val in (1,2,3) and y_val in (1,2,3):
            set_table(int(x_val)-1,int(y_val)-1)
        else:
            raise Exception("Значение заполнено")
    except Exception:
        print('Вы ввели неверные координаты')
        switch_sign()
# проверяем на победу
def winner_check():
    global fields, move_sign, move_count
    #горизонтали
    #вертикали
    #диагонали
    if fields[0][0] == fields[0][1] == fields[0][2] != '-' \
        or fields[1][0] == fields[1][1] == fields[1][2] != '-'\
        or fields[2][0] == fields[2][1] == fields[2][2] != '-'\
        or fields[0][0] == fields[1][0] == fields[2][0] != '-' \
        or fields[0][1] == fields[1][1] == fields[2][1] != '-' \
        or fields[0][2] == fields[1][2] == fields[2][2] != '-' \
        or fields[0][0] == fields[1][1] == fields[2][2] != '-'\
        or fields[0][2] == fields[1][1] == fields[2][0] != '-'\
        or move_count == 9:
        if move_count == 9:
            print("НИЧЬЯ")
            return True
        else:
            # тут инверсия, т.к. мы анализируем предыдущий ход
            if  move_sign == '0' :
                print("Победил Крестик")
            else:
                print("Победил Нолик")
            return True
# приветствие
print("-------------------")
print("  Приветсвуем вас  ")
print("      в игре       ")
print("  крестики-нолики  ")
print("-------------------")
print(" формат ввода: x y ")
print(" x - номер строки  ")
print(" y - номер столбца ")
# создаём пустую таблицу
clear_table()
#основной цикл программы
while (not game_end):
    input_data()
    drawing_table()
    game_end = winner_check()
    if game_end:
        if input("Сыграем ещё раз Y/N?  (Y-ещё раз/N-выйти)") == 'Y':
            clear_table()
        else:
            break
            print('Спасибо за игру')