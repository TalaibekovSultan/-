import random
complex_dict = []
i = 0
v = 1
while i < 6:
    n = random.randrange(1, 1000)
    print(n)
    if n % 2 == 0:
        s = 'ЛЮБИТ'
        complex_dict.append(str(v) and s)
    else:
        s2 = 'НЕЛЮБИТ'
        complex_dict.append(str(v) and s2)
    v = v + 1
    i = i + 1
def romoshko():
    print(complex_dict)
    return complex_dict
