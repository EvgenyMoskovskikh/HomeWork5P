from time import sleep
from game import*

# Задача 1
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
print("ЗАДАЧА 1")
my_text = 'У лукоморья дуб зелёный; Златая цепь на дубе том: И днём и ночью кот учёный Всё ходит по цепи кругом;'
print(f'Исходный текст:  {my_text}')


def del_some_char(txt):
    my_text_list = list(
        filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, txt.split()))
    return my_text_list


print(f'Результат:  {del_some_char(my_text)}')

# Задача 2
# Создайте программу для игры в ""Крестики-нолики""
sleep(1)
print("ЗАДАЧА 2")
game_over = False
human = True
rules()

while not game_over:
    print_maps()
    if human:
        symbol = "X"
        sleep(1)
        step = int(input("\nТвой ход: "))
    else:
        print("\nКомпьютер делает ход: ")
        sleep(1)
        symbol = "O"
        step = choice_move()

    if step != "":
        move_maps(step, symbol)
        win = get_result()
        if win != "":
            game_over = True
        else:
            game_over = False
    else:
        sleep(1)
        print("Все поля заполнены!")
        game_over = True
        win = "Достойная игра!)"
    human = not human
print_maps()
print(win)

# Задача 3
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
sleep(1)
print("ЗАДАЧА 3")


def compress(path):
    count = 1
    txt = ''
    for i in range(len(path) - 1):
        if path[i] == path[i + 1]:
            count += 1
        else:
            txt = txt + str(count) + path[i]
            count = 1
    if count > 1 or (path[len(path) - 2] != path[-1]):
        txt = txt + str(count) + path[-1]
    return txt


def decompress(path):
    number = ''
    txt = ''
    for i in range(len(path)):
        if not path[i].isalpha():
            number += path[i]
        else:
            txt = txt + path[i] * int(number)
            number = ''
    return txt


def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)
    print('Данные успешно записаны в файл!')


my_text = 'AAAABBBCPPPPWWWWWWWWWWWWWWKKKKKK'
comp_my_text = compress(my_text)
print(f'Сжатые данные: {comp_my_text}')
write_file('compress.txt', comp_my_text)
decomp_my_text = decompress(comp_my_text)
print(f'Восстановленные данные: {decomp_my_text}')
write_file('decompress.txt', decomp_my_text)
