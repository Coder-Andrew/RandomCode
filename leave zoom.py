from pynput.mouse import Controller, Button
import time

mouse = Controller()

left = Button.left


timer = time.localtime()
while True:
    if (timer[3] >= 15 and timer[4] >= 30):
        for i in range(5):
            mouse.click(left)
        print("Left class. Click successful")
        break

    timer = time.localtime()
    time.sleep(5)
