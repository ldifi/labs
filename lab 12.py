import tkinter as tk

def zad_1():
    class Restaurant:
        def __init__(self, name, type):
            self.rname = name
            self.ctype = type

        def describe_restaurant(self):
            print(f'Название: {self.name} Тип кухни: {self.type}')

    class IceCreamStand(Restaurant):
        def __init__(self,name, type, flavors):
            super().__init__(name, type)
            self.flavors = flavors

        def iflavors(self):
            print('Виды мороженного:')
            print(*self.flavors, sep='\n')

    s = IceCreamStand("Крипипаста", 'обычная', ['клубничка', 'ванилька', 'шоколадик'])
    s.iflavors()

def zad_2():
    class Restaurant:
        def __init__(self, name, type):
            self.name = name
            self.type = type

        def describe_restaurant(self):
            print(f'Название: {self.name} Тип кухни: {self.type}')


    class IceCreamStand(Restaurant):
        def __init__(self, name, type, flavors, place, time):
            super().__init__(name, type)
            self.flavors = flavors
            self.place = place
            self.time = time

        def flavors_(self):
            print('Виды мороженного:')
            print(*self.flavors, sep='\n')

        def plus(self):
            self.flavors.append(input('Введите новое мороженое '))

        def minus(self):
            self.flavors.remove(input('Удалить мороженое '))

        def search(self):
            if input('Какой вкус хотите найти? ') in self.flavors:
                print('Eсть')
            else:
                print('Нет')

    class naPalochke(IceCreamStand):
        def __init__(self, name, type, flavors, place, time, material):
            super().__init__(name, type, flavors, place, time)
            self.material = material

        def palochka(self):
            print('Материал палочки: ', self.material)

    class vstakane(IceCreamStand):
        def __init__(self, name, type, flavors, place, time, sale):
            super().__init__(self, name, type, flavors, place, time)
            self.sale = sale

        def stakan(self):
            print('Размер стакана: ', self.sale)

    s = IceCreamStand("Крипипаста", 'обычная', ['клубничка', 'ванилька', 'шоколадик'], 'ул. Еда', '8:00-21:00')
    s.describe_restaurant()
    s.plus()
    s.flavors_()
    s.minus()
    s.flavors_()
    s.search()

    g = naPalochke("Крипипаста", 'обычная', ['клубничка', 'ванилька', 'шоколадик'], 'ул. Еда', '8:00-21:00', 'бамбук')
    g.palochka()

def zad_3():
    class IceCreamStand:
        def __init__(self):
            self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Coffee', 'Rocky Road']
            self.prices = [1.99, 2.99, 2.99, 3.99, 3.99, 4.99]

        def get_flavors(self):
            return self.flavors

        def get_prices(self):
            return self.prices

    class IceCreamStandGUI:
        def __init__(self, master):
            self.master = master
            master.title("IceCream")

            self.ice_cream_stand = IceCreamStand()

            self.flavors_label = tk.Label(master, text='Flavors', font='Helvetica 12 bold')

            self.flavors_listbox = tk.Listbox(master, font='Helvetica 12', height=len(self.ice_cream_stand.get_flavors()))

            for flavor in self.ice_cream_stand.get_flavors():
                self.flavors_listbox.insert(tk.END, flavor)

            self.prices_label = tk.Label(master, text='Prices', font='Helvetica 12 bold')

            self.prices_listbox = tk.Listbox(master, font='Helvetica 12', height=len(self.ice_cream_stand.get_prices()))

            for price in self.ice_cream_stand.get_prices():
                self.prices_listbox.insert(tk.END, price)

            self.flavors_label.grid(row=0, column=0)
            self.flavors_listbox.grid(row=1, column=0)
            self.prices_label.grid(row=0, column=1)
            self.prices_listbox.grid(row=1, column=1)

    root = tk.Tk()
    a = IceCreamStandGUI(root)
    root.mainloop()
