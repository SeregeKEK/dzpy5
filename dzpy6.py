def zadacha1():
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
    text = 'Корни обабвразования горькие, но плабводы сладкие. абв'
    my_list = list(filter(lambda x: 'абв' not in x , text.split()))
    print(' '.join(my_list))


def zadacha2():
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
    from random import randint

    def input_dat(name):
        number = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
        while number < 1 or number > 28:
            number = int(input(f"{name}, введите корректное количество конфет: "))
        return number


    def p_print(name, k, counter, value):
        print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

    playerOne = input("Введите имя первого игрока: ")
    playerTwo = input("Введите имя второго игрока: ")
    value = int(input("Введите количество конфет на столе: "))
    flag = randint(0,2)
    if flag:
        print(f"Первый ходит {playerOne}")
    else:
        print(f"Первый ходит {playerTwo}")

    counter1 = 0
    counter2 = 0
    while value > 28:
        if flag:
            candyCount = input_dat(playerOne)
            counter1 += candyCount
            value -= candyCount
            flag = False
            p_print(playerOne, candyCount, counter1, value)
        else:
            candyCount = input_dat(playerTwo)
            counter2 += candyCount
            value -= candyCount
            flag = True
            p_print(playerTwo, candyCount, counter2, value)

    if flag:
        print(f"Выиграл {playerOne}")
    else:
        print(f"Выиграл {playerTwo}")


def zadacha3():
# Создайте программу для игры в ""Крестики-нолики"".	
    print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

    board = list(range(1,10))

    def draw_board(board):
        print("-" * 13)
        for i in range(3):
            print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)

    def take_input(player_token):
        valid = False
        while not valid:
            player_answer = input("Куда поставим " + player_token+"? ")
            try:
                player_answer = int(player_answer)
            except:
                print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if(str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

    def check_win(board):
        win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
        for each in win_coord:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                return board[each[0]]
        return False

    def main(board):
        counter = 0
        win = False
        while not win:
            draw_board(board)
            if counter % 2 == 0:
                take_input("X")
            else:
                take_input("O")
            counter += 1
            if counter > 4:
                tmp = check_win(board)
                if tmp:
                    print(tmp, "выиграл!")
                win = True
                break
            if counter == 9:
                print("Ничья!")
            break
    draw_board(board)
    main(board)
    input("Нажмите Enter для выхода!")

def zadacha4():
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
    def unzip(compressed_string:str):
        new_string = ""
        digit = ""
        for i in range(len(compressed_string)):
            if compressed_string[i].isdigit():
                digit += compressed_string[i]
            else:
                new_string += compressed_string[i] * int(digit)
                digit = ""               
        return new_string

    def rle2(string: str):
        new_string = ""
        last_symmbol = string[0]
        count = 1        
        for i in range(1, len(string)):
            if string[i] == last_symmbol:
                count += 1
                continue
            else:
                new_string += f"{count}{last_symmbol}"
                last_symmbol = string[i]
                count = 1                
        new_string += f"{count}{last_symmbol}"        
        return new_string

    in_string = "qqqqqqqqqqqqqqeeeeWWWFssssssWwwwwwQQQQrrrrasdasd"
    print(f'Изначальный текст: {in_string}')
    compressed = rle2(in_string)
    print(f'Сжатый текст: {compressed}')
    unpack = unzip(compressed)
    print(f'Разжатый текст: {unpack}')

# zadacha1()
# zadacha2()
# zadacha3()
zadacha4()