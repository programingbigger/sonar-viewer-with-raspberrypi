import tkinter as tk

# setup window
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
RADIUS = min(CENTER_X, CENTER_Y) * 0.9

# setup color
GREEN = "#00FF00"
RED = "#FF0000"

# setup tkinter
root = tk.Tk()
root.title("潜水艦ソナー")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

root.mainloop()
