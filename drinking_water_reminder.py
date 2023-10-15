import winsound
import threading
from tkinter import messagebox
import time
import plyer
frequency = 2600  # Set Frequency To 2600 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
while True:
    winsound.Beep(frequency,duration)
    response = messagebox.showinfo(title='Reminder',message='Please drink water')
    if response == 'ok':
        plyer.notification.notify(title='Reminder',message='Please drink water',timeout=6)
    time.sleep(10)