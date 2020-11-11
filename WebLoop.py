
# Import Libraries

from time import sleep # Necessary to make the code wait
import webbrowser # Necessary to manage web interactions with Python

import os # Necessary to kill the process

# Settings

print("Choose the URL to access:")
url = input()

print("Choose the time it will take to loop:")
time = int(input())

# Loop Script

while(True):
    browser = webbrowser.get("c:\\program files\\internet explorer\\iexplore.exe")
    browser.open_new(url)
    sleep(time)
    os.system("taskkill /f /im iexplore.exe")
    os.system("taskkill /f /im msedge.exe")