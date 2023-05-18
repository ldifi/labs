import json

def zad_1():
    with open('10.json', 'r', encoding='utf8') as f:
        s = json.load(f)
    print(s)
    for i in range(len(s.get('products'))):
        k = s.get('products')[i]
        print('Название: ' + str(k.get('name')))
        print('Цена: ' + str(k.get('price')))
        print('Вес: ' + str(k.get('weight')))
        if str(k.get('name')):
            print('В наличии')
        else:
            print('Нет в наличии!', '\n')

def zad_2():
    with open('10.json', 'r', encoding='utf8') as f:
        s = json.load(f)
    print(s)

    for i in range(len(s.get('products'))):
        k = s.get('products')[i]
        print('Название: ' + str(k.get('name')))
        print('Цена: ' + str(k.get('price')))
        print('Вес: ' + str(k.get('weight')))
        if str(k.get('name')):
            print('В наличии')
        else:
            print('Нет в наличии!', '\n')
        print('')

    dop = {}
    dop['name'] = input('Название: ')
    dop['price'] = input('Цена: ')
    dop['available'] = input('В наличии? (True/False) ')
    dop['weight'] = input('Вес: ')

    s['products'].append(dop)

    with open('10.json', 'w', encoding='utf8') as f:
        json.dump(s, f, indent=4, ensure_ascii=False)

def zad_3():
    e = open('en-ru.txt ', 'r', encoding='utf8').read().split('\n')
    s = {}
    for i in range(len(e)):
        e[i] = e[i].split(' - ')
        s[e[i][0]] = e[i][1:]
    print(s)

    s1 = {}
    for i in s:
        for k in s[i]:
            k = k.split(', ')
            for j in k:
                if j not in s1:
                    s1[j] = i

    s1 = dict(sorted(s1.items()))
    print(s1)

    s2 = ''
    for i in s1:
        s2 += i + ' - ' + s1[i] + '\n'

    x = open('ru-en.txt', 'w+', encoding='utf8')
    x.write(s2)
    
zad_3()