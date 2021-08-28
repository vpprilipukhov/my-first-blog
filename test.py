import time
import random


def death(arr):
    for bact in arr:
        if bact.food <= 0:
            arr.remove(bact)


def life(arr):
    for bact in arr:
        bact.division_true()
        if bact.division_bool == True:
            arr.remove(bact)
            arr.append(Bacterium())
            arr.append(Bacterium())


class Bacterium():
    def __init__(self):
        self.food = 0.5
        self.division = 0.5
        self.division_threshold = 0.6
        self.find_food = 0.5
        self.division_bool = False

    def feeding(self):
        x = random.random()
        if self.find_food > x:
            self.food += 0.1001
            if self.food > 1:
                self.food = 1

    def fasting(self):
        self.food -= 0.05

    def division_true(self):
        if self.food > self.division_threshold:
            x = random.random()
            if self.division >= x:
                self.division_bool = True

arr = [Bacterium()]




fps = 10
skipticks = 1/(fps*1.0)


while True:
    for i in arr:
        i.fasting()
    for j in arr:
        j.feeding()
    death(arr)
    life(arr)


    print(arr[0].food, len(arr))
    time.sleep(skipticks )
