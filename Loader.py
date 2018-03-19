class Animals:
    weight = 0 #kg
    eyes = 2
    name = None

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def name_animall (self, name):
        self.name = name

    def weight_animal(self, amount):
        self.weight += amount

class Mammals(Animals):
    hooves = 4

    def Toilet(self):
        self.weight -= 5

class Birds(Animals):
    wings = 2
    flying = False

    def fly(self, boolean):
        self.flying = boolean

class Cows(Mammals):

    def voice_cow(self):
        print("moooooow")

class Goats(Mammals):

    def voice_goat(self):
        print("BBBeeeeeee")

class Sheeps(Mammals):
    
    def voice_sheep(self):
        print("BBBeeeebbbbee")


class Pigs(Mammals):

    def voice_pig(self):
        print("hrruuuuu")

class Ducks(Birds):

    def voice_duck(self):
        print("kkkkkrrrrreeeeeee")

class Chikens(Birds):

    def voice_chiken(self):
        print("cccooooddddccccooodaaaaa")

class Geese(Birds):

    def voice_gees(self):
        print("ggooooogggoooooo")

pig1 = Pigs('pig1', 100)
print("вес свиньи:", pig1.weight)
pig1.weight_animal(100)
print("вес свиньи:", pig1.weight)
pig1.voice_pig()
pig1.Toilet()
print("вес свиньи:", pig1.weight)

goat1 = Goats('goat!', 10)
print("вес козла:", goat1.weight)
print("Сколько копыт у козла", Goats.hooves, "А сколько глаз у козла?", Goats.eyes)
goat1.weight_animal(20)
print("вес козла:" ,goat1.weight)
goat1.voice_goat()

gees1 = Geese('gees1' ,5)
gees1.voice_gees()
print("Гусь в небе?" ,gees1.flying)
gees1.fly(True)
print("Гусь в небе?", gees1.flying, "Сколько глаз у гуся?", gees1.eyes)
gees1.weight_animal(10)
print("Сколько гусь весит?", gees1.weight)

chiken1 = Chikens('chiken1', 14)
chiken1.voice_chiken()
print("Курица в небе?", chiken1.flying)
chiken1.fly(True)
print("Курица в небе?", chiken1.flying)
print("Сколько у курицы крыльев?", chiken1.wings)

pig2 = Pigs('pig2', 120)
print('Имя свиньи', pig2.name, 'и ее вес', pig2.weight)