import pyautogui as pg
import time
from pynput.keyboard import Key, Controller


for i in range(5,0,-1):
	print(str(i)+' seconds... ')
	time.sleep(1)

print('here we go !!')

keyboard = Controller()

for i in range(100):
	pg.write("fcuk you... you cheating")
	time.sleep(0.5)
	# pg.press("Ctrl")
	# pg.press("Enter")
	keyboard.press(Key.ctrl)
	pg.press("Enter")
	# keyboard.release('enter')
	# keyboard.release(Key.ctrl)


fcuk you... you cheating

