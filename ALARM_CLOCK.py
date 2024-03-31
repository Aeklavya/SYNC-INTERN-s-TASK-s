import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading
from playsound import playsound
def play_alarm_sound():
    playsound("fairytale.mp3")

def set_alarm(alarm_time, snooze_time=0):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        if current_time >= alarm_time:
            response = messagebox.askyesno("Alarm Clock", "Wake Up! Do you want to snooze?")
            if response:
                snooze_alarm(alarm_time, snooze_time)
            else:
                play_alarm_sound()
                time.sleep(300)
                break
            break

def snooze_alarm(alarm_time, snooze_time):
    snooze_duration = datetime.timedelta(minutes=snooze_time)
    new_alarm_time = alarm_time + snooze_duration
    messagebox.showinfo("Alarm Clock", f"The alarm is snoozed and will ring again in  {new_alarm_time.strftime('%H:%M:%S')}.")
    set_alarm(new_alarm_time, snooze_time)

def threading_set_alarm(hour, minute, second, snooze_time):
    alarm_time = datetime.datetime.now().replace(hour=int(hour.get()), minute=int(minute.get()), second=int(second.get()))
    time_left = alarm_time - datetime.datetime.now()
    messagebox.showinfo("Alarm Clock", f"Alarm is set and will ringq in {time_left}.")
    threading.Thread(target=set_alarm, args=(alarm_time, snooze_time)).start()

def create_gui():
    root = tk.Tk()
    root.title("Responsive Alarm Clock")

    frame = tk.Frame(root)
    frame.pack(expand=True, fill='both')

    tk.Label(frame, text="Set Alarm Time (HH:MM:SS)").pack()
    tk.Label(frame, text="Hour").pack(side='left')
    tk.Label(frame, text="Minute").pack(side='left')
    tk.Label(frame, text="Second").pack(side='left')

    hour = tk.StringVar()
    minute = tk.StringVar()
    second = tk.StringVar()

    hour.set("00")
    minute.set("00")
    second.set("00")

    hour_entry = tk.Entry(frame, textvariable=hour, width=5).pack(side='left')
    minute_entry = tk.Entry(frame, textvariable=minute, width=5).pack(side='left')
    second_entry = tk.Entry(frame, textvariable=second, width=5).pack(side='left')

    tk.Button(frame, text="Set Alarm", command=lambda: threading_set_alarm(hour, minute, second, 5)).pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
