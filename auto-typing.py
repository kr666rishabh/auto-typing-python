import pyautogui
import time

time.sleep(30)
for line in open("typingData.txt", "r"):
    pyautogui.typewrite(line)
    pyautogui.press("enter")
