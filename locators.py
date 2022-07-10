import pyautogui as pg

close = pg.locateOnScreen(f'screenshot\\close.png', confidence=0.8)
icon = pg.locateOnScreen(f'screenshot\\icon.png', confidence=0.8)
next1 = pg.locateOnScreen(f'screenshot\\next1.png', confidence=0.8)
raif = pg.locateOnScreen(f'screenshot\\raif.png', confidence=0.8)
run = pg.locateOnScreen(f'screenshot\\run.png', confidence=0.8)
sleep = pg.locateOnScreen(f'screenshot\\sleep.png', confidence=0.8)
yes = pg.locateOnScreen(f'screenshot\\yes.png', confidence=0.8)
yes1 = pg.locateOnScreen(f'screenshot\\1.png', confidence=0.8)
a = 'kjd'


def test(*args):
    while icon:
        pg.moveTo(yes1)
        pg.moveTo(icon)
        pg.sleep(0)


def icon_start():
    while True:
        loc = pg.locateOnScreen('screenshot\\icon.png', confidence=0.8)
        if loc:
            loc = pg.locateOnScreen('screenshot\\icon.png', confidence=0.8)
            pg.moveTo(loc)
            pg.doubleClick()
            return True
        pg.sleep(0.2)
