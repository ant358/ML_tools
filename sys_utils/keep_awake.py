"""
Prevent the system from shutting down if you have 
no admin control and need it to run for many hours
"""


import pyautogui
import time
import sys
from datetime import datetime

# quickly move the mouse to the upper left corner to exit
pyautogui.FAILSAFE=True

numMin = 3

run = True

while(run == True):
    x=0
    print('Keep Awake: move mouse quickly to top left to exit')
    # # in_put = input('Enter q to quit, anything else to continue: ')
    # if in_put == 'q':
    #     run == False 
    #     break
    # else:
    while(x < numMin):
        print(x)
        time.sleep(50)
        x += 1
    # for i in range(0,200, 10):
    #     pyautogui.moveTo(500,250 + i, 5) # x, y, over 5 seconds
    pyautogui.press('volumedown')
    time.sleep(5)
    pyautogui.press('volumeup')
    print('Volume up down at {}'.format(datetime.now().time()))
    time.sleep(5)
    # for i in range(0,3):
    pyautogui.press("shift")
    print('Key pressed at {}'.format(datetime.now().time()))

# used to keep the cmd window open when run on the desktop
input("Press enter to exit ;)")
