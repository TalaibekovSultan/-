import random

complex_dict = {}
i = 0
v = 1
while i < 6:
    n = random.randrange(1, 1000)
    if n % 2 == 0:
        s = 'love'
        complex_dict[v] = s
    else:
        s2 = "don't love"
        complex_dict[v] = s2
    v = v + 1
    i = i + 1

