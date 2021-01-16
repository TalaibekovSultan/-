import json

json_filename = 'data.json'

from ramashka import complex_dict

with open(json_filename, 'w') as file:
    json.dump(complex_dict, file)
print(complex_dict)
b = int(input('Сколько значений вы хотите добавить?: '))
v = 0
z = 7
while v < b:
    a = int(input('Введите значение: '))
    if a % 2 == 0:
        s = 'love'
        complex_dict[z] = s
    elif a % 2 != 0:
        s2 = "don't love"
        complex_dict[z] = s2
    if b == str or a == str:
        print('Что-то пошло не так')
    z = z + 1
    v = v + 1
with open(json_filename, 'w') as file:
    json.dump(complex_dict, file)
print(complex_dict)
