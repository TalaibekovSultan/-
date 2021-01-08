# Код для выигрыша не написал, но теоретически знаю как

a = [0, 1, 2]
b = [0, 1, 2]
c = [0, 1, 2]

print('a:', a)
print('b:', b)
print('c:', c)
i = 0
while i < 4:
    print('ХОД "X"')
    d = input("Выберите строку: ")
    x = int(input("Куда поставить Х: "))
    if d == 'a':
        a.pop(x) and a.insert(x, "x")
        if x == 0:
            a.insert(x, "x")
        print('a:', a)
        print('b:', b)
        print('c:', c)
    elif d == 'b':
        b.pop(x) and b.insert(x, "x")
        if x == 0:
            b.insert(x, "x")
        print('a:', a)
        print('b:', b)
        print('c:', c)
    elif d == 'c':
        c.pop(x) and c.insert(x, "x")
        if x == 0:
            c.insert(x, "x")
        print('a:', a)
        print('b:', b)
        print('c:', c)
    elif x > 2 or d != 'a' or d != 'b' or d != 'c':
        print('Что-то пошло не так')
    else:
        print('Что-то пошло не так')

    print('ХОД "O"')
    d = input("Выберите строку: ")
    o = int(input("Куда поставить 0: "))
    if d == 'a':
        a.pop(o) and a.insert(o, "o")
        if o == 0:
            a.insert(o, "o")
        print('a:', a)
        print('b:', b)
        print('c:', c)
    elif d == 'b':
        b.pop(o) and b.insert(o, "o")
        if o == 0:
            b.insert(o, "o")
        print('a:', a)
        print('b:', b)
        print('c:', c)
    elif d == 'c':
        c.pop(o) and c.insert(o, "o")
        if o == 0:
            c.insert(o, "o")
        print('a:', a)
        print('b:', b)
        print('c:', c)
    elif o > 2 or d != 'a' or d != 'b' or d != 'c':
        print('Что-то пошло не так')
    else:
        print('Что-то пошло не так')
    i = i + 1
print('КОНЕЦ ИГРЫ')
