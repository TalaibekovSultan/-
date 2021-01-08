woman = []
man = []
i = 0
while i < 5:
    name = input("Введите имя: ")
    sex = input("Введите пол: ")
    if sex == "женский":
        woman.append(name)
    if sex == "мужской":
        man.append(name)
    i = i + 1
print("женские имена: ", woman)
print("мужские имена: ", man)
