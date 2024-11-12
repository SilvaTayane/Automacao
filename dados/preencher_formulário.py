import pyautogui
import time
import pandas as pd

def esperar(tempo):
    time.sleep(tempo)

dados = pd.read_csv('formulario.csv')
mun_linhas = dados.shape[0]

# url = "link do formulário"

pyautogui.press('win')
pyautogui.write('firefox')
esperar(0.5)
pyautogui.press('enter')
esperar(2)
pyautogui.write(url, interval=0.1)
pyautogui.press('enter')
esperar(5)


for index, row in dados.iterrows():

    pyautogui.moveTo(716, 376)
    pyautogui.click()

    pyautogui.write("1234", interval= 0.1)
    pyautogui.press('tab')

    pyautogui.write("name", interval=0.1)
    pyautogui.press('tab')

    pyautogui.write("lastname", interval=0.1)
    pyautogui.press('tab')

    pyautogui.write("sim", interval=0.1)
    pyautogui.press('tab')
    pyautogui.press('enter')
    esperar(3)
    pyautogui.moveTo(733,274)
    pyautogui.click()
    esperar(3)

    pyautogui.alert('Aacabou a Execução!')

    fechar = pyautogui.locateOnWindow("image.png")
    centro = pyautogui.center(fechar)
    centro = pyautogui.click()