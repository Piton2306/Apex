import os
import mouseinfo


def screenshot(*args):
    path = 'screenshot'
    files_last = []
    for firs, folder, files in os.walk(path):
        for i in files:
            name = i.split('.')[0]
            files_last.append(f"{name} = pi.locateOnScreen(f'screenshot\\\\{i}', confidence=0.8)")
    return '\n'.join(files_last)


def mouse_Info():
    mouseinfo.mouseInfo()

mouse_Info()