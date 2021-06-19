#This bot is made for mouseaccuracy.com
#SETTING: spacing=10 && target_color=(120,19,45)
# NOR = Normal - HAR = Hard - INS = Insane
# TI = Tiny - MEDI = Medium - LARG = Large
# durations = 15s - 30s - 90s
#Result table
# | # |   SETTINGS    | TG EFFICIENCY |  CL ACCURACY  | CLICK PER SEC |
# | - | ------------- | ------------- | ------------- | ------------- |
# | 1 | INS-TINY-30s  |     100%      |      97%      |      3.3      |
# | 2 | INS-TINY-90s  |     100%      |      86%      |      3.8      |
# | 3 | INS-TINY-15s  |     100%      |      92%      |      3.2      |
# | 4 | NOR-MEDI-30s  |     100%      |      82%      |      2.2      |
import win32api,win32con
import pyautogui
import time
import keyboard
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
print("started")

spacing=10
target_color=(120,19,45)
while keyboard.is_pressed('q')==False:
    pic = pyautogui.screenshot()
    width, height = pic.size
    for x in range(0, width, spacing):
        for y in range(0, height, spacing):
            r, g, b = pic.getpixel((x, y))
            if (r,g,b) == target_color:
                click(x, y)
                time.sleep(0.01)
                break

print("stopped")
    
    




