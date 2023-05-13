def zad_1():
    a=int(input('введите число'))
    if a%3==0:
        print('число делится на 3')
    else:
        print('число не делится на 3')

def zad_2():
    try:
        a=int(input('ведите число'))
        b=100/a
    except ZeroDivisionError:
        print('Введен 0')
    except ValueError:
        print('Введено не число')
    else:
        print('Результат деления на введеное число', b)

def zad_3():
    d = input('введите дату')
    d = d.split('.')
    if int(d[0]) * int(d[1]) == int(d[2][2:4]):
        print('Дата магическая')
    else:
        print('Дата не магическая')

def zad_4():
    x=0
    y=0
    c = input('Введите номер ')
    if len(c)%2 == 0:
        for k in c[0:int(len(c)/2)]:
            x+= int(k)
        for k in c[int(len(c)/2): int(len(c))+1]:
            y+= int(k)
        if x==y:
            print('Билет счастливый')
        else:
            print('Билет не счастливый ')
    else:
        print('Количество цифр нечетное!')