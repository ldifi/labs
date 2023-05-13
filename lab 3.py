def p1():
    print("Вводите слова, чтобы остановиться напишите stop")
    s = []
    while True:
        a = str(input())
        if a == "stop":
            break
        else:
            s.append(a)
    print(" ".join(s))

def p2():
    print("Введите редкое слово, чтобы остановиться напишите stop")
    s = []
    while True:
        a = str(input())
        if a == "stop":
            break
        else:
            if "ф" in a or "Ф" in a:
                print("Wow! It's rare word!")
            else:
                print("Oh! It's not rare word...")
            s.append(a)
    print(" ".join(s))

def p3():
    from random import randint
    no = 0
    po = 0
    print("Для завершения игры введите слово stop")
    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f"{a} + {b} = ", end="")
        otvet = input()
        while not otvet.isdigit() and otvet != "stop":
            print("Вы ввели что-то не то, попробуйте ввести снова: ", end="")
            otvet = input()
        if otvet == "stop":
            break
        otvet = int(otvet)
        if a + b == otvet:
            print("Правильный ответ!")
            po += 1
        else:
            print("Неправильный ответ...")
            no += 1
        if no == 3:
            print("Вы проиграли! Правильных ответов: ", po)
            break
p3()