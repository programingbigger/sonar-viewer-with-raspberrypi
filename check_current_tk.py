# ~ import os

# ~ display_name = os.environ.get('DISPLAY', ':0')
# ~ print(f"Current DISPLAY: {display_name}")

import tkinter as tk

root = tk.Tk()
screen_name = root.winfo_screen()
print(f"Current screen: {screen_name}")
