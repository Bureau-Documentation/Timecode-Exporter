import tkinter as tk
from tkinter import messagebox
import os
import pyperclip
from tkinterdnd2 import DND_FILES, TkinterDnD


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # PyInstaller creates a temp folder and stores path in _MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    

def process_file(file_path):
    if not os.path.isfile(file_path):
        messagebox.showerror("Error", f"File not found: {file_path}")
        return

    time_ranges = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                columns = line.split()
                # Check if the first column is a number and lines have enough columns
                if len(columns) > 7 and columns[0].isdigit():  # Checking for at least 8 columns
                    # Extract time from column 7 and column 8
                    start_time = columns[6]  # Column 7 is at index 6
                    end_time = columns[7]    # Column 8 is at index 7
                    
                    # Get the first 8 characters for both start_time and end_time
                    start_time_formatted = start_time[:8]  # First 8 characters
                    end_time_formatted = end_time[:8]      # First 8 characters
                    
                    time_ranges.append(f"{start_time_formatted} to {end_time_formatted}")

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

# Set the icon correctly using the resource path
icon_path = resource_path('timecode_exporter.ico')  # Get the absolute path to the icon
root.iconbitmap(icon_path)  # Use the resource path here

frame = tk.Frame(root, width=400, height=200)
frame.pack_propagate(False)
frame.pack()

lb = tk.Label(frame, text="Drag and drop the .edl file here", padx=10, pady=10)
lb.pack(expand=True)

# Register drop target using TkinterDnD
frame.drop_target_register(DND_FILES)
frame.dnd_bind('<<Drop>>', drop)

root.mainloop()