import pyscreenrec
import keyboard
import tkinter as tk
from tkinter import filedialog
from screeninfo import get_monitors

import time

f_path="default.mp4"
def browse_file():
    # Open a file dialog and set the file path in the entry widget
    file_path = filedialog.askdirectory()
    entry_var.set(file_path)

def print_file_path():
    # Get the file path from the entry widget and print it to the console
    global f_path
    file_path = entry_var.get()
    f_path=file_path+"/"+str(time.time())+".mp4"
    print(f"Selected file path: {file_path}")
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("File Path Selector")

# Create a StringVar to hold the file path
entry_var = tk.StringVar()

# Create an entry widget to accept the file path
entry = tk.Entry(root, textvariable=entry_var, width=50)
entry.pack(pady=10)

# Create a button to open the file dialog
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=5)


# Create a button to print the file path
ok_button = tk.Button(root, text="OK", command=print_file_path)
ok_button.pack(pady=5)

# Run the application
root.mainloop()


# Create a ScreenRecorder object
recorder = pyscreenrec.ScreenRecorder()

# Start recording (output file name, frames per second)
recorder.start_recording(f_path, 20)
def check_key_presses():
    global key_press_count, key_press_time
    current_time = time.time()
    key_press_time = [t for t in key_press_time if current_time - t < 2]
    print(key_press_time)
    if len(key_press_time) >= 5:
        return True
    return False


key_press_time=[]
while True:
    if keyboard.is_pressed('esc'):
        key_press_time.append(time.time())
        if check_key_presses():
            break
        time.sleep(0.1)


# Stop recording
recorder.stop_recording()

print("Recording complete!")