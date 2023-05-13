from PIL import Image, ImageFilter

def zad_1():
    img = Image.open('1.png')

    img.show()
    print(img.size)
    print(img.mode)
    print(img.format)

def zad_2():
    img = Image.open('1.png')

    img = img.reduce(3)
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img.save('1_2.png')

def zad_3():
    for i in range(2, 6):
        i = str(i)
        img = Image.open(i + '.jpg')
        img = img.filter(ImageFilter.EMBOSS)
        img.save('C:/Users/difiv/PycharmProjects/pythonProject/lab 7/pics/' + i + '.png')

zad_3()


