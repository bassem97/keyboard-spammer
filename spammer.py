import pyautogui as pg
import time
import sys


for i in range(5,0,-1):
	print(str(i)+' seconds... ')
	time.sleep(1)

print('here we go !!')


for i in range(100):
	pg.write(str(sys.argv[1]))
	time.sleep(0.1)
	pg.press("Enter")




