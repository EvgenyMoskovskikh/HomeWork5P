# Игровое поле
map_game = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Варианты победы
victory_options = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def rules():
    print("Добро пожаловать в игру 'крестики-нолики' \nТы сражаешься с компьютером. Ты - X, компьютер - O."
          "\nЧтобы сделать ход, введи число от 1 до 9. Числа соотвествуют полям, как показано ниже:")


def print_maps():
    """Печать игрового поля"""
    print(f"\t {map_game[0]} | {map_game[1]} | {map_game[2]}")
    print(f"\t {map_game[3]} | {map_game[4]} | {map_game[5]}")
    print(f"\t {map_game[6]} | {map_game[7]} | {map_game[8]}")


def move_maps(move, num):
    """Делаем ход"""
    ind = map_game.index(move)
    map_game[ind] = num


def get_result():
    """Результат игры"""
    win = ""
    for i in victory_options:
        if map_game[i[0]] == "X" and map_game[i[1]] == "X" and map_game[i[2]] == "X":
            win = "Ты выиграл!"
        if map_game[i[0]] == "O" and map_game[i[1]] == "O" and map_game[i[2]] == "O":
            win = "Выиграл компьютер)"
    return win


def check_line(sum_o, sum_x):
    """Ищем все X и 0 на линии победы"""
    step = ""
    for line in victory_options:
        o = 0
        x = 0
        for i in range(0, 3):
            if map_game[line[i]] == "O":
                o += 1
            if map_game[line[i]] == "X":
                x += 1
        if o == sum_o and x == sum_x:
            for j in range(0, 3):
                if map_game[line[j]] != "O" and map_game[line[j]] != "X":
                    step = map_game[line[j]]
    return step


def choice_move():
    """Выбор хода"""
    step = check_line(2, 0)
    if step == "":
        step = check_line(0, 2)
    if step == "":
        step = check_line(1, 0)
    if step == "":
        if map_game[4] != "X" and map_game[4] != "O":
            step = 5
    if step == "":
        if map_game[0] != "X" and map_game[0] != "O":
            step = 1
    return step