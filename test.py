import pyautogui as pg
from multiprocessing import Process
from time import sleep

loc_8 = 'screenshot\\loc_8.png'
loc_9 = 'screenshot\\loc_9.png'


#
#         if loc_1 or loc_2 or loc_5 or loc_6 or loc_7:
#             pg.moveTo(loc_1)
#             pg.moveTo(loc_2)
#             pg.moveTo(loc_5)
#             pg.moveTo(loc_6)
#             pg.moveTo(loc_7)
#             pg.click()
#         if loc_3_1 or loc_3_2 or loc_3_3:
#             loc_4 = pg.locateOnScreen('screenshot\\loc_4.png', confidence=0.8)
#             pg.moveTo(loc_4)
#             pg.click()


def Local_start(locator='', confiden=0.9):
    while True:
        loc = pg.locateOnScreen(locator, confidence=confiden)
        if loc:
            pg.moveTo(loc)
            sleep(0.3)
        sleep(0.3)


class A:
    def __call__(self):
        Local_start(loc_8)


class B:
    def __call__(self):
        Local_start(loc_9)


if __name__ == '__main__':
    a = A()
    b = B()
    p1 = Process(target=a)
    p2 = Process(target=b)
    p1.start()
    p2.start()
