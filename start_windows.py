import pyautogui as pi

def icon():
    while True:
        loc = pi.locateOnScreen('screenshot\\icon.png', confidence=0.8)
        if loc:
            loc = pi.locateOnScreen('screenshot\\icon.png', confidence=0.8)
            pi.moveTo(loc)
            pi.doubleClick()
            return True
        pi.sleep(0.2)


def next1():
    while True:
        loc = pi.locateOnScreen('screenshot\\next1.png', confidence=0.8)
        if loc:
            pi.moveTo(loc)
            pi.click()
            return True
        pi.sleep(0.2)


def close():
    while True:
        loc = pi.locateOnScreen('screenshot\\close.png', confidence=0.8)
        if loc:
            pi.moveTo(loc)
            pi.click()
            return True
        pi.sleep(0.2)


def run():
    while True:
        loc = pi.locateOnScreen('screenshot\\run.png', confidence=0.8)
        if loc:
            pi.moveTo(loc)
            pi.click()
            return True
        pi.sleep(0.2)


def raif():
    while True:
        loc1 = pi.locateOnScreen('screenshot\\yes.png', confidence=0.8)
        if loc1:
            loc = pi.locateOnScreen('screenshot\\raif.png', confidence=0.8)
            if loc:
                pi.moveTo(loc)
                pi.click()
                return True
        pi.sleep(0.2)
