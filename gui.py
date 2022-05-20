import tkinter as tk
from tkinter import messagebox
messagebox.showinfo("hello","welcome to picam controller")

gui = tk.Tk()
gui.configure(background="light blue")
gui.title("picam controller")
gui.geometry("640x480")
gui.mainloop()