import time
import pyautogui
import os

pyautogui.hotkey('win', 'r')

time.sleep(.25)

pyautogui.write('powershell.exe')

time.sleep(.25)

pyautogui.press('enter')

time.sleep(.25)

pyautogui.write('cd $env:userprofile\Desktop')

time.sleep(.25)

pyautogui.press('enter')

time.sleep(.25)

pyautogui.write('md "Hacker Was Here"')

time.sleep(.25)

pyautogui.press('enter')

time.sleep(.25)

pyautogui.write('cd "Hacker Was Here"')

time.sleep(.25)

pyautogui.press('enter')

time.sleep(.25)

pyautogui.write("Invoke-WebRequest -Uri https://hdwallpapers.move.pk/wp-content/uploads/2015/08/batman-style.jpg -OutFile batman.jpg")

time.sleep(.25)

pyautogui.press('enter')

time.sleep(1)

pyautogui.write('exit')

time.sleep(.25)

pyautogui.press('enter')
