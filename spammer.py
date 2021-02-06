"""

I (Parmo#1619) am not responsible for anything that happens to you with use of this program. (Such as bans on discord
etc.)
By using this program you agree to the terms. (the above)

"""
import os
import time

print("Spammer by Parmo#1619\n\n")

print("Installing required dependencies...")
os.system("pip install pyautogui")
print("Finished installing dependencies\n\n")

import pyautogui


def spam():
    confirm = input(
        "Please change 'spamMsg.txt' to what you wish to spam. By default will spam the Bee-movie transcript. Press "
        "enter to continue ")

    if " " in confirm or confirm == "":

        delay = input("How much delay do you want between sending the messages? (in seconds): ")
        print(f'Delay has been set to {delay}')

        msg = open('spamMsg.txt', 'r')

        if msg == "":
            return print("Message file is empty. Please add content to message file to continue")

        print(
            """
            ================================================================================================================

            Please get ready for spamming in the application you want to spam in.
            Initializing, please wait...

            ================================================================================================================
            """
        )

        time.sleep(2)
        print("Spamming started...")

        for word in msg:
            pyautogui.typewrite(word)
            time.sleep(float(delay))
            pyautogui.press("enter")
            print(word + 'Has been sent. Press CTRL+C to stop the program')


spam()
print("Finished spamming.")
