import tkinter as tk
import time
import os
import sys
from os import times
from tkinter import font

root = tk.Tk()
root.title("Schmoney Tracker")


HEIGHT = 200
WIDTH = 400


def run_buy_xed_history():
    os.system('python "C:/Users/radli/code/documentation/txt/buy_xed.py"')


def run_buy_rbc_history():
    os.system('python "C:/Users/radli/code/documentation/txt/buy_rbc.py"')


def run_sell_xed_history():
    os.system('python "C:/Users/radli/code/documentation/txt/sell_xed.py"')


def run_sell_rbc_history():
    os.system('python "C:/Users/radli/code/documentation/txt/sell_rbc.py"')


def run_buy_xed_plot():
    os.system('python "C:/Users/radli/code/documentation/plt/buy_xed.py"')


def run_buy_rbc_plot():
    os.system('python "C:/Users/radli/code/documentation/plt/buy_rbc.py"')


def run_sell_rbc_plot():
    os.system('python "C:/Users/radli/code/documentation/plt/sell_rbc.py"')


def run_sell_xed_plot():
    os.system('python "C:/Users/radli/code/documentation/plt/sell_xed.py"')


# Set screen size
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


frame = tk.Frame(root, bg="black")
frame.place(relwidth=1, relheight=1)  # relx =0,1 rely=0.1

button_buy_xed = tk.Button(
    frame,
    text="XED history",
    bg="#5cdb5c",
    fg="black",
    command=run_buy_xed_history,
    font=("Ariel", 12),
)
button_buy_xed.place(relx=0, rely=0, relwidth=0.25, relheight=0.5)

button_buy_xed_plot = tk.Button(
    frame,
    text="XED plot",
    bg="#5cdb5c",
    fg="black",
    command=run_buy_xed_plot,
    font=("Ariel", 12),
)
button_buy_xed_plot.place(relx=0.25, rely=0, relwidth=0.25, relheight=0.5)


button_buy_rbc = tk.Button(
    frame,
    text="RBC history",
    bg="#5cdb5c",
    fg="black",
    command=run_buy_rbc_history,
    font=("Ariel", 12),
)
button_buy_rbc.place(relx=0, rely=0.5, relwidth=0.25, relheight=0.5)
button_buy_rbc_plot = tk.Button(
    frame,
    text="RBC plot",
    bg="#5cdb5c",
    fg="black",
    command=run_buy_rbc_plot,
    font=("Ariel", 12),
)
button_buy_rbc_plot.place(relx=0.25, rely=0.5, relwidth=0.25, relheight=0.5)


button_sell_xed = tk.Button(
    frame,
    text="XED history",
    bg="#ff0021",
    fg="black",
    command=run_sell_xed_history,
    font=("Ariel", 12),
)
button_sell_xed.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.5)
button_sell_xed_plot = tk.Button(
    frame,
    text="XED plot",
    bg="#ff0021",
    fg="black",
    command=run_sell_xed_plot,
    font=("Ariel", 12),
)
button_sell_xed_plot.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.5)


button_sell_rbc = tk.Button(
    frame,
    text="RBC history",
    bg="#ff0021",
    fg="black",
    command=run_sell_rbc_history,
    font=("Ariel", 12),
)
button_sell_rbc.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.5)
button_sell_rbc_plot = tk.Button(
    frame,
    text="RBC plot",
    bg="#ff0021",
    fg="black",
    command=run_sell_rbc_plot,
    font=("Ariel", 12),
)
button_sell_rbc_plot.place(relx=0.75, rely=0.5, relwidth=0.25, relheight=0.5)


root.mainloop()
