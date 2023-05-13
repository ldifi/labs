def slova:
    s = ""
    while True:
        a = input()
        if a == "стоп":
            break
        else:
            s = s + a + " "
        continue
    print(s)

def colour():
    c1 = input()
    c2 = input()

    if c1 == "Красный":
        if c2 == "Синий":
            print("Фиолетовый")
        if c2 == "Желтый":
            print("Оранжевый")
    if c1 == "Синий":
        if c2 == "Желтый":
            print("Зеленый")
    if c1 == "Желтый":
        if c2 == "Синий":
            print("Зеленый")
        if c2 == "Красный":
            print("Оранжевый")

def god():
    god = input()
    god = int(god)
    if god % 4 == 0 and god % 100 != 0 or god % 400 == 0:
        print("Visokosniy")
    else:
        print("Nevisokosniy")

def password():
    p = input()
    p_low = False
    p_up = False
    p_sim = False
    p_ch = False
    for char in p:
        if char.isnumeric():
            p_ch = True
        if char.islower():
            p_low = True
        if char.isupper():
            p_up = True
        if char in '&?@*^%!.,№:;':
            p_sim = True

    if p_low and p_up and p_sim and p_ch is True:
        print("Надежный пароль")
    elif p_low is False:
        print("Добавьте буквы нижнего регистра")
    elif p_up is False:
        print("Добавьте буквы верхнего регистра")
    elif p_ch is False:
        print("Добавьте цифры")
    elif p_sim is False:
        print("Добавьте специальные символы")
    else:
        print("Вы не ввели пароль!")

def vagon():
    mesto = input()
    mesto = int(mesto)
    if mesto > 0:
        if mesto // 2 == 1:
            if 1 >= mesto <= 36:
                print("Купе, верхняя полка")
            elif 37 >= mesto <= 54:
                print("Боковая койка, верхняя полка")
        else:
            if 1 >= mesto <= 36:
                print("Купе, нижняя полка")
            elif 37 >= mesto <= 54:
                print("Боковая койка, нижняя полка")
