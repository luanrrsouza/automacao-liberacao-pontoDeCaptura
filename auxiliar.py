import pyautogui
import time

# Usado para coletar a posição do mouse para usar no método pyautogui.click.

time.sleep(5) 
# Está configurado para coletar a posição após 5 segundos, para dar tempo do operador arrastar o mouse onde deve ser clicado.
print(pyautogui.position())
pyautogui.position()

# Usado, caso seja necessário rolar a tela para cima, basta copiar e colar na main.
pyautogui.scroll(1000)