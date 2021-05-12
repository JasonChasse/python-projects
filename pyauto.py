import time
import pyautogui

pyautogui.hotkey('win', 'r')

time.sleep(1)

pyautogui.write('notepad.exe')

time.sleep(1)

pyautogui.press('enter')

time.sleep(1)

pyautogui.write('This is a test of whether or not I can run commands on here')

pyautogui.moveTo(1000, 500, duration=2)

pyautogui.moveTo(500, 1000, duration=2)

pyautogui.moveTo(1000, 500, duration=2)

pyautogui.moveTo(500, 1000, duration=2)

pyautogui.moveTo(800, 1800, duration=2)

pyautogui.moveTo(500, 1000, duration=2)

pyautogui.moveTo(50, 1000, duration=2)
