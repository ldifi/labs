from PIL import Image, ImageDraw, ImageFont

file = str(input("Введите название праздника"))

def zad_1(name):

     file = Image.open(str(name) + ".jpg")
     cropped =file.crop((20,20,440,440))
     cropped.save('file.jpg')

def zad_2(name):
     prazdnik ={'новый год': 'новый год.jpg', '23 февраля' : '23 февраля.jpg', '8 марта' : '8 марта.jpg', 'день рождение' : 'день рождение.jpg'}
     img = Image.open(prazdnik[name])

     name = input("Введите имя того, кого хотите поздравить") + ", поздравляю!!!"
     font = ImageFont.truetype('arial.ttf', size=25)
     draw_text = ImageDraw.Draw(img)
     draw_text.text(
          (400, 200),
          name,font = font,
          fill=('#99dee8')
     )
     img.show()
     img.save("img.png")

zad_2(file)

