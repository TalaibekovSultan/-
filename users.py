import os
name = input("Введите свое имя: ")
file_name = name + ".txt"
user_data = input('Введите свои данные: ')
with open(file_name, 'w') as f:
    f.write(user_data)
i = 0
while i == 0:
    print("Здраствуйте", name)
    print("1) Посмотореть свои данные:")
    print("2) Изменить свои данные:")
    print("3) Вывод файлов с пользователями:")
    print("4) Закрыть программу:")
    read = input("Выберите: ")
    if read == '1':
        print('Вот ваши данные: ', user_data)
        a = input("Желаете изменить свои данные?: ")
        if a == 'да':
            user_data = input('Введите свои данные: ')
            read = '2'
    elif read == '2':
        user_data = input('Введите свои данные: ')
        with open(file_name, 'w') as f:
            f.write(user_data)
    elif read == '3':
        directory = os.listdir()

        for index, file in enumerate(directory):
            print(index, ':', file)
        x = input('Хотите-ли посмотреть содержимое какого либо файла?: ')
        if x == 'да':
            y = int(input('Введите номер файла: '))
            with open(directory[y], 'r') as f:
                print('readline: ', f.readlines())
    elif read == '4':
        i = i + 1
    else:
        print("Что-то пошло не так")
print('Программа закрыта')
