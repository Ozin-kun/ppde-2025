import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np

# Membuat jendela utama
root = tk.Tk()
root.title("Data Visualizer")
root.geometry("800x600")
root.configure(bg="lightgray")

# Membuat Figure matplotlib
fig = Figure(figsize=(8, 6), dpi=100)
ax = fig.add_subplot(111)

# Plot data sederhana
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y)
ax.set_title("Grafik Sinus")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Embed plot ke dalam Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

root.mainloop()

# Membuat toolbar navigasi
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

