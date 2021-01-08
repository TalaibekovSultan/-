name = input("Введите свое имя: ")
file_name = name
user_data = input('Введите свои данные: ')
with open(file_name, 'w') as f:
    s = open(file_name, 'w')
    s.write(user_data)
    s.close()
i = 0
while i == 0:
    print("Здраствуйте", name)
    print("a) Посмотореть свои данные:")
    print("б) Изменить свои данные:")
    print("в) Вывод файлов с пользователями:")
    print("г) Закрыть программу:")
    read = input("Выберите: ")
    if read == 'а':
        print('Вот ваши данные: ', user_data)
        a = input("Желаете изменить свои данные?: ")
        if a == 'да':
            user_data = input('Введите свои данные: ')
            with open(file_name, 'w') as f:
                s = open(file_name, 'w')
                s.write(user_data)
                s.close()
    elif read == 'б':
        user_data = input('Введите свои данные: ')
        with open(file_name, 'w') as f:
            s = open(file_name, 'w')
            s.write(user_data)
            s.close()
    elif read == 'в':
        import os

        directory = os.listdir()
        for index, file in enumerate(directory):
            print(index, ':', file)
        x = input('Хотите-ли посмотреть содержимое какого либо файла?: ')
        if x == 'да':
            y = input('Введите номер файла: ')



    elif read == 'г':
        i = i + 1
    else:
        print("Что-то пошло не так")
print('Программа закрыта')
