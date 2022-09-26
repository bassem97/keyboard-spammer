import pyautogui as pg
import time

for i in range(5,0,-1):
	print(str(i)+' seconds... ')
	time.sleep(1)

print('here we go !!')

for i in range(100):
	pg.write("spam text")
	time.sleep(0.5)
	pg.press("Enter")
