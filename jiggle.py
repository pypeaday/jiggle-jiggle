import argparse
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--keys",
        nargs="+",
        default=["F15"],
        help="comma separated list of which keys to press, executed in order",
    )
    parser.add_argument(
        "--sleep", type=int, help="seconds to sleep between key presses", default=60
    )

    args = parser.parse_args()

    for k in args.keys:
        if k not in VK_CODE.keys():
            print(f"{k} not registered key!")

    while True:
        keys = [k for k in args.keys]
        print(f"pressing {keys}")
        press(*keys)
        time.sleep(args.sleep)
