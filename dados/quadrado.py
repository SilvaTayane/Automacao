import pyautogui
import time

def esperar(tempo) :
    time.sleep(tempo)

pyautogui.press('win')
pyautogui.write('paint', interval=0.2)
pyautogui.press('enter')
esperar(2)
pyautogui.moveTo(150, 350, duration= 1)
pyautogui.dragTo(350, 350, duration= 1)
pyautogui.dragTo(350, 450, duration= 1)
pyautogui.dragTo(150, 450, duration= 1)
pyautogui.dragTo(150, 350, duration= 1)