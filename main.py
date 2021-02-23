from tkinter import *
from tkinter import ttk
from datetime import datetime


class DisappearingText():
    def __init__(self, window):

        self.window = window
        self.countingsecs = 0
        self.start_time = 0
        self.time_used = 0

        window.title(string='Disappearing Text App')
        window.config(padx=5, pady=5)

        frame = ttk.Frame(window)
        frame.grid(column=0, row=0, sticky="N W E S")

        label_time_afk = ttk.Label(frame, text="Time Not Recieved Key (in sec):", width=38, font=("Arial", 14, "normal"))
        label_time_afk.grid(row=1, column=1, sticky='W')
        self.time_used = StringVar()
        label_time_used = ttk.Label(frame, textvariable=self.time_used, width=4, font=("Arial", 14, "normal"))
        label_time_used.grid(row=1, column=2, sticky="W")

        self.text = Text(frame, width=75, height=5, background="#d3e0dc", font=("Arial", 18, "normal"), wrap="word")
        self.text.focus()
        self.text.config(spacing1=10, spacing2=10, spacing3=10)
        self.text.grid(row=3, column=1, columnspan=2, sticky='W E')
        self.text.bind('<KeyPress>', self.start)

    def start(self):
        self.start_time = datetime.now()
        self.counting()

    def counting(self):
        self.time_used_secs = datetime.now() - self.start_time
        self.time_used.set(int(self.time_used_secs.seconds))
        self.countingsecs = self.window.after(1000, self.counting)
        self.delete()

    def delete(self):
        if self.time_used_secs.seconds > 5:
            self.text.delete(1.0, 'end')
            self.window.after_cancel(self.countingsecs)


window = Tk()
app=DisappearingText(window)
window.mainloop()