# Combining Powershell with Python to make a directory and download a picture to it
# then open picture

import time
import pyautogui
import os

p = pyautogui
t = time.sleep

p.hotkey('win', 'r')
t(.25)
p.write('powershell.exe -WindowStyle Hidden')
t(.25)
p.press('enter')
t(.25)
p.write('cd $env:userprofile\Desktop')
t(.25)
p.press('enter')
t(.25)
p.write('md "Batman Was Here"')
t(.25)
p.press('enter')
t(.25)
p.write('cd "Batman Was Here"')
t(.25)
p.press('enter')
t(.25)
p.write("Invoke-WebRequest -Uri https://hdwallpapers.move.pk/wp-content/uploads/2015/08/batman-style.jpg -OutFile batman.jpg")
t(.25)
p.press('enter')
t(.25)
p.write('start batman.jpg -WindowStyle maximized')
t(.25)
p.press('enter')
t(.25)
p.write('exit')
t(.5)
p.press('enter')
