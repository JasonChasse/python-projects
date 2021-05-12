import time
import pyautogui
import os

pyautogui.hotkey('win', 'r')

time.sleep(.5)

pyautogui.write('notepad.exe')

time.sleep(.5)

pyautogui.press('enter')

time.sleep(.5)

pyautogui.write('Going to try to make a folder ok? So please watch.', interval=.25)

pyautogui.moveTo(1000, 500, duration=2)

pyautogui.rightClick()

time.sleep(.5)

pyautogui.press('right')

time.sleep(.5)

pyautogui.press('down')

time.sleep(.5)

pyautogui.press('down')

time.sleep(.5)

pyautogui.press('down')

time.sleep(.5)

pyautogui.press('down')

time.sleep(.5)

pyautogui.press('down')

time.sleep(.5)

pyautogui.press('down')

time.sleep(.5)

pyautogui.press('down')

time.sleep(.5)

pyautogui.press('right')

time.sleep(.5)

pyautogui.press('enter')

pyautogui.write('Python Folder')

time.sleep(.5)

pyautogui.press('enter')





