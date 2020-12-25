# дз 2
name = input("Введите имя")
sex = input("Введите пол")
woman = []
man = []
if sex == "женский":
    woman.append(name)
    print(woman)
elif sex == "мужской":
    man.append(name)
    print(man)

# дз 1
x = 1
while x < 100:
    print("x: ", x)
    x = x * 7
