import os
import time
import pyautogui

cmd1 = 'powershell'

os.startfile(cmd1)
time.sleep(2)
pyautogui.write('notepad.exe')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('hello')
