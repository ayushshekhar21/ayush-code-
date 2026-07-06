import tkinter as tk
from datetime import datetime


def update_time():
    now = datetime.now()
    time_string = now.strftime('%I:%M:%S %p')
    date_string = now.strftime('%d-%m-%Y')
    clock_label.config(text=time_string)
    date_label.config(text=date_string)
    root.after(1000, update_time)


root = tk.Tk()
root.title('Digital Clock')
root.geometry('400x220')
root.configure(bg='black')

clock_label = tk.Label(
    root,
    text='00:00:00',
    font=('Arial', 48, 'bold'),
    fg='lightgreen',
    bg='black'
)
clock_label.pack(expand=True)

date_label = tk.Label(
    root,
    text='00-00-0000',
    font=('Arial', 20),
    fg='white',
    bg='black'
)
date_label.pack(pady=10)

update_time()
root.mainloop()
