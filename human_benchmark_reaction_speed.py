import pyautogui as pag
from PIL import ImageGrab
from ctypes import *  # 获取屏幕上某个坐标的颜色
import win32api
import win32con
import time


def get_color(x, y):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)  # 获取颜色值
    pixel = gdi32.GetPixel(hdc, x, y)  # 提取RGB值
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    return [r, g, b]


def click(x, y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def main():
    x, y = 300, 350
    while 1:
        # pic = ImageGrab.grab()
        # color = pic.getpixel(pix)
        if get_color(x, y) == [75, 219, 106]:
            pag.click(x, y)
            time.sleep(0.1)
            print("equal")


if __name__ == "__main__":
    main()