import os
import tkinter as tk

root = tk.Tk()
root.title("LOADING")

parentDirectory = os.path.dirname(os.path.abspath(__file__))

def start():
    os.startfile('dist\main\main.exe')
    root.destroy()
start()
root.mainloop()