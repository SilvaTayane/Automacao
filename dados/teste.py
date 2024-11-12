import pyautogui
import time

pyautogui.size
time.sleep(5)
x, y = pyautogui.position()
print(x, y)
pyautogui.alert(f'As coordenadas são: {x}, {y}')