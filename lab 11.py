def zad_1():
    class Restaurant:
       def __init__(self,name,cuisine):
           self.name = name
           self.cuisine = cuisine

       def describe_restaurant(self):
            print("Name: ", self.name)
            print("Cuisine: ", self.cuisine)

       def open_restaurant(self):
            print("Restaurant is open")

    r1 = Restaurant
    r1.name = "Nya"
    r1.cuisine ="Nam"
    Restaurant.describe_restaurant(r1)
    Restaurant.open_restaurant(r1)

def zad_2():
    class Restaurant:
       rating = 4

       def __init__(self,name,cuisine):
           self.name = name
           self.cuisine = cuisine

       def describe_restaurant(self):
            print("Name: ", self.name)
            print("Cuisine: ", self.cuisine)

       def open_restaurant(self):
            print("Restaurant is open")
    r1=Restaurant
    r1.name = input("Name 1st restaurant")
    r1.cuisine = input("Cuisine 1st restaurant")
    r1.describe_restaurant(r1)

    r = input("Rating")
    Restaurant.rating = r
    print("Rating: ", Restaurant.rating)

    r2=Restaurant
    r2.name = input("Name 2nd restaurant")
    r2.cuisine = input("Cuisine 2nd restaurant")
    r2.describe_restaurant(r2)

    r3 = Restaurant
    r3.name = input("Name 3rd restaurant")
    r3.cuisine = input("Cuisine 3rd restaurant")
    r3.describe_restaurant(r3)


zad_2()