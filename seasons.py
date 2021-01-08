month = int(input("Введите номер месяца: "))
my_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
if month in my_list[0:3]:
    print("Время года: Зима")
elif month in my_list[3:6]:
    print("Время года: Весна")
elif month in my_list[6:9]:
    print("Время года: Лето")
elif month in my_list[9:12]:
    print("Время года: Осень")
else:
    print("Вы ввели не правильный номер месяца")
