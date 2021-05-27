import pyautogui
import time
time.sleep(5)
f = open("Script.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("Enter")
