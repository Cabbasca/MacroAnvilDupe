import pyautogui
from pynput import keyboard
from time import sleep

print("-- Forked by Visivel, Made by Glorman. --")
print("-- Hope you enjoy dupe your trash lol --")

COMBINATIONS = [
    {keyboard.KeyCode(char=']')}
]

current = set()


def execute():
    print("Bot duped your shit")
    pyautogui.moveTo(854, 495)
    sleep(0.3)
    pyautogui.click()
    sleep(0.3)
    pyautogui.press("space")
    sleep(0.3)
    pyautogui.moveTo(1069, 496)
    sleep(0.3)
    pyautogui.click()
    sleep(0.3)


def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO)for COMBO in COMBINATIONS):
            execute()


def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
