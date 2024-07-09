import pyautogui
import time        


pyautogui.PAUSE= 0.5

pyautogui.press("win")
pyautogui.write("Google Chrome")
pyautogui.press("enter")

pyautogui.write("https://web.ntkonline.com.br/#/container/home")
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=35, y=146)
pyautogui.click(x=100, y=290)
pyautogui.click(x=107, y=346)

time.sleep(2)
pyautogui.click(x=1203, y=291)
time.sleep(0.8)
pyautogui.hotkey("win", "v")
pyautogui.click(x=1253, y=475)
pyautogui.click(x=1370, y=327)

time.sleep(0.5)
pyautogui.click(x=1570, y=298)

time.sleep(3)
pyautogui.click(x=1602, y=426)
pyautogui.click(x=1559, y=510)
pyautogui.click(x=1034, y=195)

time.sleep(2)

pyautogui.click(x=1157, y=1062)

pyautogui.click(x=719, y=986)

pyautogui.write("Opa, Liberado para a instalacao!")