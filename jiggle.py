import time

import win32api
import win32con

from vk_codes import VK_CODE


def press(*args):
    """
    one press, one release.
    accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
    """
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, 0, 0)
        time.sleep(0.05)
        win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)


def pressAndHold(*args):
    """
    press and hold. Do NOT release.
    accepts as many arguments as you want.
    e.g. pressAndHold('left_arrow', 'a','b').
    """
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, 0, 0)
        time.sleep(0.05)


def pressHoldRelease(*args):
    """
    press and hold passed in strings. Once held, release
    accepts as many arguments as you want.
    e.g. pressAndHold('left_arrow', 'a','b').

    this is useful for issuing shortcut command or shift commands.
    e.g. pressHoldRelease('ctrl', 'alt', 'del'), pressHoldRelease('shift','a')
    """
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, 0, 0)
        time.sleep(0.05)

    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.1)


def release(*args):
    """
    release depressed keys
    accepts as many arguments as you want.
    e.g. release('left_arrow', 'a','b').
    """
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)


if __name__ == "__main__":
    while True:
        press("F15")
        print("pressed F15")
        time.sleep(60)
