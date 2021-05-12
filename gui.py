import pyautogui
import time

pyautogui.size() # current screen resolution width and height 
(1366, 768)

while True :

    pyautogui.moveTo(900,600,2)

    pyautogui.scroll(-10)

    time.sleep(2)

    pyautogui.scroll(-10)

    time.sleep(2)

    pyautogui.scroll(-10)

    time.sleep(2)

    pyautogui.scroll(50)

#pyautogui.moveRel(50,500,2)

#pyautogui.moveRel(500,60,4)

#pyautogui.moveRel(10,325,1)

#pyautogui.moveRel(650,525,3)




