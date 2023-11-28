import cv2
import pyautogui
import numpy as np
import time

# Function to capture screen
def capture_screen():
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return frame

# Main loop
while True:
    frame = capture_screen()

    # Perform actions based on captured frame (Add your object detection logic here)

    # For demonstration purposes, let's simulate pressing 'W' every 1 second
    pyautogui.press('w')
    time.sleep(1)
