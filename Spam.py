import pyautogui
import webbrowser as web
from time import sleep
web.open("Link from whatsapp")
sleep(10)
with open(r"path from beescript.txt") as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")

