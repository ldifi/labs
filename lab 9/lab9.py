def zad_1():
    import os
    from PIL import Image

    i = 'C:/Users/difiv/PycharmProjects/pythonProject/лаба/lab/pics'

    if not os.path.exists('C:/Users/difiv/PycharmProjects/pythonProject/лаба/lab/картинки'):
        os.mkdir('C:/Users/difiv/PycharmProjects/pythonProject/лаба/lab/картинки')

    for f in os.listdir(i):
        if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'):
            img = Image.open(os.path.join(i,f))
            img = img.resize((500, 500))
            img.save(os.path.join('C:/Users/difiv/PycharmProjects/pythonProject/лаба/lab/картинки', f))

def zad_3():
    import csv
    itog=0
    print('Нужно купить:')
    with open('data.csv') as file:
        file = csv.reader(file)
        for i in file:
            name=i[0]
            kolvo=int(i[1])
            cn=int(i[2])
            itog+=kolvo*cn
            print(name,'-',kolvo, ' шт. за',cn,' руб.')
    print("Итоговая сумма: ", itog)

zad_1()