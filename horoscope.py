name = input("Введите свое имя: ")
a = int(input("Введите день рождения: "))
b = int(input("Введите месяц рождения "))
if ((a >= 21) and (a <= 31) and (b == 3)) or ((a >= 1) and (a <= 20) and (b == 4)):
    print(name + " ваш знак задиака: ОВЕН")
if ((a >= 21) and (a <= 30) and (b == 4)) or ((a >= 1) and (a <= 20) and (b == 5)):
    print(name + " ваш знак задиака: ТЕЛЕЦ")
if ((a >= 21) and (a <= 31) and (b == 5)) or ((a >= 1) and (a <= 20) and (b == 6)):
    print(name + " ваш знак задиака: БЛИЗНЕЦЫ")
if ((a >= 22) and (a <= 30) and (b == 6)) or ((a >= 1) and (a <= 20) and (b == 7)):
    print(name + " ваш знак задиака: РАК")
if ((a >= 23) and (a <= 31) and (b == 7)) or ((a >= 1) and (a <= 20) and (b == 8)):
    print(name + " ваш знак задиака: ЛЕВ")
if ((a >= 24) and (a <= 31) and (b == 8)) or ((a >= 1) and (a <= 20) and (b == 9)):
    print(name + " ваш знак задиака: ДЕВА")
if ((a >= 24) and (a <= 30) and (b == 9)) or ((a >= 1) and (a <= 20) and (b == 10)):
    print(name + " ваш знак задиака: ВЕСЫ")
if ((a >= 24) and (a <= 31) and (b == 10)) or ((a >= 1) and (a <= 20) and (b == 11)):
    print(name + " ваш знак задиака: СКОРПИОН")
if ((a >= 23) and (a <= 30) and (b == 11)) or ((a >= 1) and (a <= 20) and (b == 12)):
    print(name + " ваш знак задиака: СТРЕЛЕЦ")
if ((a >= 22) and (a <= 31) and (b == 12)) or ((a >= 1) and (a <= 20) and (b == 1)):
    print(name + " ваш знак задиака: КОЗЕРОГ")
if ((a >= 21) and (a <= 31) and (b == 1)) or ((a >= 1) and (a <= 20) and (b == 2)):
    print(name + " ваш знак задиака: ВОДОЛЕЙ")
if ((a >= 21) and (a <= 29) and (b == 2)) or ((a >= 1) and (a <= 20) and (b == 3)):
    print(name + " ваш знак задиака: РЫБЫ")
elif a > 31:
    print(name, "вы ввели неправельный день рождения")
elif b > 12:
    print(name, "вы ввели неправельный месяц рождения")
