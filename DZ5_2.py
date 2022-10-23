from random import randint

def Game1(number):
    print('Welcome to "Candy and Pain" for two players!')
    count = randint(1, 3)
    player1 = input("Введите имя первого игрока: ")
    player2 = input("Введите имя второго игрока: ")
    while number > int(0):
        if count%2 == 0:
            player = player2
        else: player = player1
        if number < int(28):
            print(f'{player} win!')
            break
        number2 = int(input(f"{player}, enter your number (1-28): "))
        if number2 > 28 and number2 < 0:
            print("You stupid! Enter number from 1 to 28!")
            count -= 1
        else:
            number -= number2
            print(f"Current number - {number}")
        count += 1

def Game2(number):
    print('Welcome to "Candy and Pain" for players and bot!')
    count = randint(1, 3)
    player1 = input("Введите имя первого игрока: ")
    player2 = "Bot"
    while number > int(0):
        if count%2 == 0:
            player = player2
        else: player = player1
        if number < int(28):
            print(f'{player} win!')
            break
        if player == player1:
            number2 = int(input(f"{player}, enter your number (1-28): "))
            if number2 > 28 or number2 < 0:
                print("You stupid! Enter number from 1 to 28!")
                count -= 1
            else:
                number -= number2
                print(f"Current number - {number}")
        else:
            number2 = randint(1, 29)
            print(f"Bot enter number = {number2}")
            number -= number2
            print(f"Current number - {number}")
        count += 1

number = 2021

choice = int(input("\nДля игры вдвоем нажмите 1 \nДля игры с ботом нажмите 2 \nВведите значение: "))
if choice == 1: Game1(number)
else: Game2(number)