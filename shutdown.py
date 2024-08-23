import os
import time
import tkinter
import tkinter as tk
from tkinter import messagebox

def schedule_shutdown(hours):
    timetowait = hours * 3600
    messagebox.showinfo("Agendado", f"o computador será desligado em {hours} horas")
    root.destroy()
    time.sleep(timetowait)
    os.system('shutdown /s /f /t 0')


root = tk.Tk()
root.title("agendar desligamento")

tk.Label(root, text="Escolha o tempo para desligar:").pack(pady=10)
tk.Button(root, text="1 hora", command=lambda: schedule_shutdown(1)).pack(pady=5)
tk.Button(root, text="2 horas", command=lambda: schedule_shutdown(2)).pack(pady=5)
tk.Button(root, text="3 horas", command=lambda: schedule_shutdown(3)).pack(pady=5)

root.mainloop()