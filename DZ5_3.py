from random import randint

def PrintMas(mas):
    for i in range(0, len(mas)):
        print()
        for l in range(0, len(mas[i])):
            print(mas[i][l], end = ' ')

def Game1(mas):
        count = 1
        player1 = input("Введите имя первого игрока: ")
        player2 = input("Введите имя второго игрока: ")
        while count <= int(9):
            if count%2 == 0:
                player = player2
            else: player = player1
            pos1 = int(input("\nВведите позицию в столбце: "))
            pos2 = int(input("\nВведите позицию в строке: "))
            if mas[pos1-1][pos2] != "___|" :
                print("Ячейка зянята!")
                count -= 1
            else:
                if player == player1:
                    mas[pos1-1][pos2] = "_X_|"
                else: mas[pos1-1][pos2] = "_O_|"
                PrintMas(mas)
            if (((mas[0][1] == "_X_|") and (mas[0][2] == "_X_|") and (mas[0][3]== "_X_|")) or ((mas[0][1] == "_O_|") and (mas[0][2] == "_O_|") and (mas[0][3]== "_O_|")) or
                ((mas[1][1] == "_X_|") and (mas[1][2] == "_X_|") and (mas[1][3]== "_X_|")) or ((mas[1][1] == "_O_|") and (mas[1][2] == "_O_|") and (mas[1][3]== "_O_|")) or
                ((mas[2][1] == "_X_|") and (mas[2][2] == "_X_|") and (mas[2][3]== "_X_|")) or ((mas[2][1] == "_O_|") and (mas[2][2] == "_O_|") and (mas[2][3]== "_O_|")) or
                ((mas[0][1] == "_X_|") and (mas[1][1] == "_X_|") and (mas[2][1]== "_X_|")) or ((mas[0][1] == "_O_|") and (mas[1][1] == "_O_|") and (mas[2][1]== "_O_|")) or
                ((mas[0][2] == "_X_|") and (mas[1][2] == "_X_|") and (mas[2][2]== "_X_|")) or ((mas[0][2] == "_O_|") and (mas[1][2] == "_O_|") and (mas[2][2]== "_O_|")) or
                ((mas[0][3] == "_X_|") and (mas[1][3] == "_X_|") and (mas[2][3]== "_X_|")) or ((mas[0][3] == "_O_|") and (mas[1][3] == "_O_|") and (mas[2][3]== "_O_|")) or
                ((mas[0][1] == "_X_|") and (mas[1][2] == "_X_|") and (mas[2][3]== "_X_|")) or ((mas[0][1] == "_O_|") and (mas[1][2] == "_O_|") and (mas[2][3]== "_O_|")) or
                ((mas[0][3] == "_X_|") and (mas[1][2] == "_X_|") and (mas[2][1]== "_X_|")) or ((mas[0][3] == "_O_|") and (mas[1][2] == "_O_|") and (mas[2][1]== "_O_|"))):
                print(f"\n{player} win!!!")
                break
            count += 1

def Game2(mas):
    count = 1
    countP = 1
    player1 = input("Введите имя игрока: ")
    player2 = 'Bot'
    while count <= int(9):
        if count%2 == 0:
            player = player2
        else: player = player1
        if player == player1:
            pos1 = int(input("\nВведите позицию в столбце: "))
            pos2 = int(input("\nВведите позицию в строке: "))
            if mas[pos1-1][pos2] != "___|" :
                print("Ячейка зянята!")
                count -= 1
            else:
                mas[pos1-1][pos2] = "_X_|"
                PrintMas(mas)
        else: 
            pos1 = randint(0, 2)
            pos2 = randint(1, 3)
            if mas[pos1-1][pos2] != "___|" :
                count -= 1
            else:
                mas[pos1-1][pos2] = "_O_|"
                print("\n")
                PrintMas(mas)
        if (((mas[0][1] == "_X_|") and (mas[0][2] == "_X_|") and (mas[0][3]== "_X_|")) or ((mas[0][1] == "_O_|") and (mas[0][2] == "_O_|") and (mas[0][3]== "_O_|")) or
                ((mas[1][1] == "_X_|") and (mas[1][2] == "_X_|") and (mas[1][3]== "_X_|")) or ((mas[1][1] == "_O_|") and (mas[1][2] == "_O_|") and (mas[1][3]== "_O_|")) or
                ((mas[2][1] == "_X_|") and (mas[2][2] == "_X_|") and (mas[2][3]== "_X_|")) or ((mas[2][1] == "_O_|") and (mas[2][2] == "_O_|") and (mas[2][3]== "_O_|")) or
                ((mas[0][1] == "_X_|") and (mas[1][1] == "_X_|") and (mas[2][1]== "_X_|")) or ((mas[0][1] == "_O_|") and (mas[1][1] == "_O_|") and (mas[2][1]== "_O_|")) or
                ((mas[0][2] == "_X_|") and (mas[1][2] == "_X_|") and (mas[2][2]== "_X_|")) or ((mas[0][2] == "_O_|") and (mas[1][2] == "_O_|") and (mas[2][2]== "_O_|")) or
                ((mas[0][3] == "_X_|") and (mas[1][3] == "_X_|") and (mas[2][3]== "_X_|")) or ((mas[0][3] == "_O_|") and (mas[1][3] == "_O_|") and (mas[2][3]== "_O_|")) or
                ((mas[0][1] == "_X_|") and (mas[1][2] == "_X_|") and (mas[2][3]== "_X_|")) or ((mas[0][1] == "_O_|") and (mas[1][2] == "_O_|") and (mas[2][3]== "_O_|")) or
                ((mas[0][3] == "_X_|") and (mas[1][2] == "_X_|") and (mas[2][1]== "_X_|")) or ((mas[0][3] == "_O_|") and (mas[1][2] == "_O_|") and (mas[2][1]== "_O_|"))):
                print(f"\n{player} win!!!")
                break
        count += 1

mas = [["|", "___|", "___|", "___|"], ["|", "___|", "___|", "___|"], ["|", "___|", "___|", "___|"]]
PrintMas(mas)
choice = int(input("\nДля игры вдвоем нажмите 1 \nДля игры с ботом нажмите 2 \nВведите значение: "))
if choice == 1: Game1(mas)
else: Game2(mas)