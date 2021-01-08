s = []


def my_function():
    brand = input("Введите марку авто: ")
    model = input("Введите модель авто: ")
    year = input("Введите год авто: ")
    dict = {'brand': brand, 'model': model, 'year': year}
    s.append(dict)


i = 0
while i < 3:
    my_function()
    i = i + 1
print(s)
