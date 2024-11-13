import pyautogui
import moviepy.editor as mpy
import numpy as np
import time
import keyboard

# Set the duration for the recording (in seconds)
duration = 3600  # 1 hour

# Get the screen size
screen_size = pyautogui.size()

# List to store frames
frames = []
key_press_count = 0
key_press_time = []


def check_key_presses():
    global key_press_count, key_press_time
    current_time = time.time()
    key_press_time = [t for t in key_press_time if current_time - t < 2]
    if len(key_press_time) >= 7:
        return True
    return False


# Record the screen
start_time = time.time()
while True:
    # Capture the screen
    img = pyautogui.screenshot()

    # Convert the image to a numpy array
    frame = np.array(img)

    # Append the frame to the list
    frames.append(frame)

    # Check if the duration has been reached
    if time.time() - start_time > duration:
        break

    # Check for key presses
    if keyboard.is_pressed('esc'):
        key_press_time.append(time.time())
        if check_key_presses():
            break

# Create a video clip from the frames
clip = mpy.ImageSequenceClip(frames, fps=20)

# Write the video file
clip.write_videofile("screen_recording.mp4", codec="libx264")

print("Recording complete!")
