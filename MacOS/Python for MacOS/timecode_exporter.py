import tkinter as tk
from tkinter import messagebox
import os
import pyperclip
from tkinterdnd2 import DND_FILES, TkinterDnD
import sys

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def init_icon():
    # Only set the icon once the window is fully initialized
    icon_path = resource_path('timecode_exporter.icns')
    root.iconbitmap(icon_path)

def process_file(file_path):
    if not os.path.isfile(file_path):
        messagebox.showerror("Error", f"File not found: {file_path}")
        return

    time_ranges = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                columns = line.split()
                if len(columns) > 5 and columns[0].isdigit():  # Check if the first column is a number
                    start_time = columns[4][:8]  # Extract start time from column 5
                    end_time = columns[5][:8]    # Extract end time from column 6
                    time_ranges.append(f"{start_time} to {end_time}")

        if time_ranges:
            formatted_time_ranges = "\n\n".join(time_ranges)
            pyperclip.copy(formatted_time_ranges)  # Copy to clipboard
            messagebox.showinfo("Timecodes", f"Timecodes:\n\n{formatted_time_ranges}\n\nThe timecodes are copied to your clipboard!")
        else:
            messagebox.showwarning("No Timecodes", "No valid timecodes found in the file.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while processing the file:\n{e}")

def drop(event):
    file_path = event.data.strip().strip('{}')  # Remove any enclosing curly braces and trim spaces
    print(f"Dropped file path: {file_path}")  # Debugging line
    process_file(file_path)

root = TkinterDnD.Tk()  # Use TkinterDnD instead of regular Tk
root.title("Timecode Exporter")
root.geometry("400x200")

# Initialize icon after main loop starts
root.after(100, init_icon)

frame = tk.Frame(root, width=400, height=200)
frame.pack_propagate(False)
frame.pack()

lb = tk.Label(frame, text="Drag and drop the .edl file here", padx=10, pady=10)
lb.pack(expand=True)

# Register drop target using TkinterDnD
frame.drop_target_register(DND_FILES)
frame.dnd_bind('<<Drop>>', drop)

root.mainloop()