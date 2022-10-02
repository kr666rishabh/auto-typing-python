import pyautogui
import time
import sys
import os

time.sleep(30)
# for line in open("typingData.txt", "r"):
for line in open(os.path.join(sys.path[0], 'typingData.txt')):
    pyautogui.typewrite(line)
    # pyautogui.press("enter")
