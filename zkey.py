import keyboard
import datetime

zpress = 0


def on_press_reaction(event):
    global zpress
    if event.name == 'z':
        zpress += 1
        print("z key pressed %d times"%zpress)
        f=open("Keypress.txt",'a')
        f.write ("Z Key was pressed" '\n')
        f.write(datetime.datetime.now().ctime())
        f.write('\n')
        f.write('\n')
        f.close

keyboard.on_press(on_press_reaction)

while True:
    pass
