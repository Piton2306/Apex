from locators import *


class IconStart:
    def __call__(self, sleep_time=10, sleep_time_ok=1):
        while True:
            icon = "Apex Legends" not in pg.getAllTitles()
            if icon:
                pg.moveTo(loc_icon)
                pg.doubleClick()
                pg.sleep(sleep_time)
            loc_ok_steam = loc_ok_steam_error
            if loc_ok_steam:
                pg.moveTo(loc_ok_steam_error)
                pg.click()
                pg.sleep(sleep_time_ok)
            break


def start(sleep_time=10, sleep_time_ok=1):
    while True:
        icon = "Apex Legends" not in pg.getAllTitles()
        if icon:
            pg.moveTo(loc_icon)
            pg.doubleClick()
            pg.sleep(sleep_time)
        if loc_ok_steam_error:
            pg.moveTo(loc_ok_steam_error)
            pg.click()
            pg.sleep(sleep_time_ok)
        pg.sleep(sleep_time_ok)



def next1():
    while True:
        loc = pg.locateOnScreen('screenshot\\next1.png', confidence=0.8)
        if loc:
            pg.moveTo(loc)
            pg.click()
            return True
        pg.sleep(0.2)


def close():
    while True:
        loc = pg.locateOnScreen('screenshot\\close.png', confidence=0.8)
        if loc:
            pg.moveTo(loc)
            pg.click()
            return True
        pg.sleep(0.2)


def run():
    while True:
        loc = pg.locateOnScreen('screenshot\\run.png', confidence=0.8)
        if loc:
            pg.moveTo(loc)
            pg.click()
            return True
        pg.sleep(0.2)


def raif():
    while True:
        loc1 = pg.locateOnScreen('screenshot\\yes.png', confidence=0.8)
        if loc1:
            loc = pg.locateOnScreen('screenshot\\raif.png', confidence=0.8)
            if loc:
                pg.moveTo(loc)
                pg.click()
                return True
        pg.sleep(0.2)
