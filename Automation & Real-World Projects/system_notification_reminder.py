# This program reminds the user to drink water at regular intervals.
# It uses system notifications and GUI popups to alert the user.
# Different implementations demonstrate various notification methods.


   #This code shows a popup with an "OK" button and waits until the user clicks it before continuing:
import tkinter as tk
from tkinter import messagebox
import time

interval = 5400   # 90 minutes

while True:
    root = tk.Tk()
    root.withdraw()  # Hide main window

    messagebox.showinfo("Drink Water Reminder!!", "Hey Anushka, It's time to drink a glass of water")
    
    root.destroy()  # Close the window

    time.sleep(interval)




   #This code waits for the user to press Enter before waiting for the next reminder:
import time
from plyer import notification

interval = 5400  # 90 minutes
while True:
    notification.notify(
        title="Drink Water Reminder!!",
        message="Hey Anushka, It's time to drink a glass of water",
        timeout=10
    )

    input("Press Enter after you've had your water... 💧")

    time.sleep(interval)
