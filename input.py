import pyautogui
import os
import time

file_index = 0

for i in range(30):
    time.sleep(5)
    os.system("scrot image" + str(file_index) + ".jpg")
    file_index += 1
