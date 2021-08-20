import time
import random

fps = 50
time_delta = 1./fps


class Cat():
    def __init__(self, name, ves):
        self.name = name
        self.age = 1
        self.ves = ves
        self.hungry = 10
        self.eat = 2

    def myu(self):
        print("Кошка", self.name, "кричит мяяяяяу!")

    def grow(self):
        self.age = self.age + 1
        print("Поздравляем с днем рождения! Кошечке", self.name, "исполнилось", self.age, "лет")

    def food(self,a):
        self.hungry += a

    def hunger(self):
        self.hungry -= 0.05



class Feeder():
    def __init__(self,name,m):
        self.name = name
        self.m = m
    def feeding(self,a):
        self.m-=a


catty = Cat("Симочка",4)
feederr = Feeder("Чаппи",100)




i = 0
while True:
    catty.hunger()

    if catty.hungry <= 10:
        a = random.randint(3,15)
        catty.food(a)
        feederr.feeding(a)
        print("Кошка покушала, ее сытость =",catty.hungry)


    if i >= 356:
        catty.grow()
        i = 0

    i+=1
    time.sleep(time_delta)