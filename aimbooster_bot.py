# pip install pyautogui
# pip install keyboard
# pip install win32api

# Automatically gets you the best score in aimbooster http://www.aimbooster.com/ by doing everything for you

from pyautogui import *
import time 
import keyboard
import win32api, win32con
import pyautogui

time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# color: 255, 219, 195


while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(590, 430, 740, 500))
    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r, g, b = pic.getpixel((x, y))
            if b == 195:
                click(x+590, y+430)
                time.sleep(0.05)
                break 