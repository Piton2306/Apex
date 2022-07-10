from locators import *
print(icon)
im = pg.screenshot('my_screenshot.png',region=(6, 1205, 32, 33))
print(list(pg.locateOnScreen(f'screenshot\\1.png', confidence=0.8)))