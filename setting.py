import os
import mouseinfo
import pyautogui as pg
from time import sleep


def Local_start(locator='', confiden=0.8):
    while True:
        loc = pg.locateOnScreen(locator, confidence=confiden)
        if loc:
            pg.moveTo(loc)
            pg.click()
            sleep(1)
        sleep(1)


def screenshot():
    path = 'screenshot'
    files_last = []
    for firs, folder, files in os.walk(path):
        for i in files:
            name = i.split('.')[0]
            files_last.append(f'{name} = "screenshot\\\\{i}"')
            # loc_1 = pg.locateOnScreen(f'screenshot/loc_1.png', confidence=0.8)
    return '\n'.join(files_last)


def mouse_Info():
    mouseinfo.mouseInfo()


