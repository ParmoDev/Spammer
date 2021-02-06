"""

I (Parmo#1619) am not responsible for anything that happens to you with use of this program. (Such as bans on discord
etc.)
By using this program you agree to the terms. (the above)

"""
import os
import time
import random
import math

print("Spammer by Parmo#1619\n\n")

print("Installing required dependencies...")
os.system("pip install pyautogui")
print("Finished installing dependencies\n\n")

import pyautogui


def spam():
    delay = input("Do you want a 'random' delay between 0 and 1 or a 'fixed' delay?: ")
    delay = delay.lower()
    delayTime = input("Ok! How much delay do you want? (in seconds. Also notice a delay under 2 for discord is not reccomended.): ")

    files = []

    for file in os.listdir("./MESSAGEFILES"):
        if file.endswith(".txt"):
            files.append(f'./MESSAGEFILES/{file}')
    print("Files listed.")

    mode = input("Do you want to use a random 'preset' file from MESSAGEFILES or a 'custom' file?: ")
    mode = mode.lower()

    if mode == "preset":
        msg = open(random.choice(files), 'r')
        print(msg)
    elif mode == "custom":
        msg = open("custom.txt", 'r')

    log = input("OK ONE LAST THING! Do you want logs in the console when you send a message? yes/no: ")
    log = log.lower()

    print(
        """
        ================================================================================================================

        Please get ready for spamming in the application you want to spam in.
        Initializing, please wait...

        ================================================================================================================
        """
    )

    time.sleep(5)
    print("Spamming started...")

    if delay == 'fixed' and log == 'yes':
        for word in msg:
            pyautogui.typewrite(word)
            time.sleep(float(delayTime))
            pyautogui.press("enter")
            print(f'Message sent: {word}')
    elif delay == 'fixed' and log == 'no':
        for word in msg:
            pyautogui.typewrite(word)
            time.sleep(float(delayTime))
            pyautogui.press("enter")
            print(f'Message sent: {word}')
    elif delay == 'random' and log == 'yes':
        for word in msg:
            delayTime = random.random()
            pyautogui.typewrite(word)
            time.sleep(delayTime)
            pyautogui.press("enter")
            print(f'Message sent: {word}')
    elif delay == 'random' and log == 'no':
        for word in msg:
            delayTime = random.random()
            pyautogui.typewrite(word)
            time.sleep(delayTime)
            pyautogui.press("enter")

    print("Finished spamming.")


spam()
