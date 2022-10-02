import pyautogui
import time

time.sleep(5)
for line in open("typingData.txt", "r"):
    pyautogui.typewrite(line)
