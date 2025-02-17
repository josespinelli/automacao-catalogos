import pyautogui as pa
from module import *
from time import sleep
pa.PAUSE = 0.1

sleep(2)
listar_marca = os.path.abspath('./img/listar_marca.png')

dropdown_marca = list(pa.locateAllOnScreen(listar_marca))

for value in dropdown_marca:
    left = value.left + 20
    top = value.top + 20
    print(f"Left: {left}, Top: {top}")

pa.click(left, top)
sleep(2)