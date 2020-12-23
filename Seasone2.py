month = int(input("Введите номер месяца: "))
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
if month == my_list[-1:2]:
    print("Время года: Зима")
elif month == my_list[3:5]:
    print("Время года: Весна")
elif month == my_list[5:8]:
    print("Время года: Лето")
elif month == my_list[8:12]:
    print("Время года: Осень")
