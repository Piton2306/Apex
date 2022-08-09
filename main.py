from multiprocessing import Process
from setting import Local_start, sleep
from locators import *


class Loc1:
    def __call__(self):
        Local_start(loc_1)


class Loc2:
    def __call__(self):
        Local_start(loc_2)


class Loc3:
    def __call__(self):
        Local_start(loc_3)


class Loc4:
    def __call__(self):
        Local_start(loc_4)


class Loc5:
    def __call__(self):
        Local_start(loc_5)



class Mirage:
    def __call__(self):
        Local_start(mirage)


if __name__ == '__main__':
    l1 = Loc1()
    l2 = Loc2()
    l3 = Loc3()
    l4 = Loc4()
    l5 = Loc5()
    m = Mirage()
    p1 = Process(target=l1)
    p2 = Process(target=l2)
    p3 = Process(target=l3)
    p4 = Process(target=l4)
    p5 = Process(target=l5)
    pm = Process(target=m)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    pm.start()
