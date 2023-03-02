import pyautogui
from pynput import keyboard
from time import sleep

print("-- Forked by Visivel, Made by Glorman. --")
print("-- Hope you enjoy dupe your trash lol --")

COMBINATIONS = [
    {keyboard.KeyCode(char=']')} # Change the keybind here, just change "]" to your keybind
]

# Configuration area for self use

delay = 0.2 #>> Set the delay of the bot right here!
anvilslot1 = 854,495 #>> Set where is the anvil slot to insert the item
anvilslot2 = 1069,496 #>> Set where is the second slot to get the renamed item
current = set() 


def execute():
    print("Bot duped your shit")
    pyautogui.moveTo(anvilslot1)
    sleep(delay)
    pyautogui.click()
    sleep(delay)
    pyautogui.press("space")
    sleep(delay)
    pyautogui.moveTo(anvilslot2)
    sleep(delay)
    pyautogui.click()
    sleep(delay)
    pyautogui.moveTo(anvilslot1)
    sleep(delay)
    pyautogui.click()
    sleep(delay)
    pyautogui.press("backspace")
    sleep(delay)
    pyautogui.moveTo(anvilslot2)
    sleep(delay)
    pyautogui.click()
    sleep(delay)


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
