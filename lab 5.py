def zad_1():
    number = int(input('Enter number: \n'))
    num = [1,2,3,4,5]
    if number in num:
        print("Win!")
    else:
        print('Lose!')

def zad_2():
    num = [1, 2, 3, 4, 4, 5, 6, 6, 6, 6, 6, 1, 2, 2, 2]
    num1 = []
    for x in num:
        if num.count(x) > 1:
            if x not in num1:
                num1.append(x)
    print(*num1)

def zad_3():
    days = ("Monday", 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    d = int(input('Enter your days off: \n'))
    print("Yours days off are: ", *days[-d:])
    print("Yours working days are: ", *days[:-d])


def zad_4():
    import random
    surname1 = ["Ivanov", "Smirnov", "Kucher", "Smit", "Vadimov", "Shishkin", "William", "Hampton", "Gryazev", "Hokkins"]
    surname2 = ["Ivanov", "Smirnov", "Kucher", "Smit", "Vadimov", "Shishkin", "William", "Hampton", "Gryazev", "Hokkins"]
    a1 = []
    a2 = []
    a = []
    a1.append(random.sample(surname1, 5))
    a2.append(random.sample(surname2, 5))
    a.extend(*a1)
    a.extend(*a2)
    a = tuple(a)
    print('a', *surname1)
    print('a', *surname2)
    print('a', *a)
    print('b', len(a))
    print('d', *sorted(a))
    print('e', 'Ivanov' in a)
    print('e', a.count('Ivanov'))


