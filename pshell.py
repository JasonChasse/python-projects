import time
import pyautogui
import os

pyautogui.hotkey('win', 'r')

time.sleep(.5)

pyautogui.write('powershell.exe')

time.sleep(.5)

pyautogui.press('enter')

time.sleep(.5)

pyautogui.write('cd $env:userprofile\Desktop')

time.sleep(.5)

pyautogui.press('enter')

time.sleep(.5)

pyautogui.write('md "Hacker Was Here"')

time.sleep(.5)

pyautogui.press('enter')

time.sleep(.5)

pyautogui.write('exit')

time.sleep(.5)

pyautogui.press('enter')



