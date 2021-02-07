from tkinter import *
from tkinter import messagebox
import time
import pyautogui
import random
import os

os.system("pip install pyautogui")

for i in range(10):
    print("\nTo stop spamming press CTRL+C in console or just close the application!")

root = Tk()
root.title("Message Spammer")
root.geometry("380x190")
root.iconbitmap('./spam.ico')
root.attributes('-topmost', True)
authorLabel = Label(root, text="Message Spammer By Parmo#1619")
authorLabel.pack()

modeLabel = Label(root, text="What mode do you wanna use?")
modeLabel.pack()

delayEntry = Scale(root, from_=0, to=10, orient=HORIZONTAL)

files = []

clicked = StringVar()
clicked.set("Select Mode")

modeDrop = OptionMenu(root, clicked, "Preset", "Custom")
modeDrop.pack()

def spamStart():
    global msg
    startedLabel = Label(root, text=f"Spamming started with {delayEntry.get()} second(s) delay! Close Application to stop spamming")
    for file in os.listdir("./MESSAGEFILES"):
        if file.endswith(".txt"):
            files.append(f'./MESSAGEFILES/{file}')

    if clicked.get() == "Preset":
        msg = open(random.choice(files), 'r')
    elif clicked.get() == "Custom":
        msg = open("custom.txt", 'r')
    else:
        return messagebox.showerror(title="Attention!", message="Please select a mode!")

    time.sleep(5)
    startedLabel.pack()

    for word in msg:
        pyautogui.typewrite(word)
        time.sleep(delayEntry.get())
        pyautogui.press("enter")


startBtn = Button(root, text="Start Spamming", command=spamStart)

delayLabel = Label(root, text="How much delay do you want between each message?")

delayLabel.pack()
delayEntry.pack()
startBtn.pack()

root.mainloop()
