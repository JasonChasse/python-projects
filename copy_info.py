# Working with inputs

import os
import pyautogui
import time

p=pyautogui
t=time.sleep

var1=input("What day is it? ")

var2=input("What is your name? ")

var3=input("What is your age? ")

print(var1, file=open("log.txt", "a"))

print(var2, file=open("log.txt", "a"))

print(var3, file=open("log.txt", "a"))

p.hotkey('win' , 'r')
t(.5)

p.write("powershell.exe")
t(.5)

p.press('enter')
t(1)

p.write("cd $env:userprofile\Desktop")
p.press('enter')
t(.5)

p.write("copy log.txt D:\\")
t(.5)
p.press('enter')

    
    
        
