import pyautogui
import time
import os
import datetime

pyautogui.hotkey('winleft','r')
time.sleep(1)
pyautogui.typewrite('notepad.exe', interval=.1)
time.sleep(.25)
pyautogui.press('enter')
time.sleep(.25)
pyautogui.press('enter')
time.sleep(.25)
pyautogui.press('enter')
pyautogui.typewrite('Your PC has been taken over by a technomage')

