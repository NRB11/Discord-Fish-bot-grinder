import pyautogui
import threading
import tkinter as tk
import time

# Global flag to control the program
running = False

# Function to start the program
def start_program():
    global running
    running = True
    start_button.config(state="disabled")  # Disable the Start button
    stop_button.config(state="normal")    # Enable the Stop button
    threading.Thread(target=send_messages).start()  # Run in a separate thread

# Function to stop the program
def stop_program():
    global running
    running = False
    start_button.config(state="normal")   # Enable the Start button
    stop_button.config(state="disabled") # Disable the Stop button

# Function to send messages repeatedly
def send_messages():
    global running
    text_to_type = "/fish "
    while running:
        # Type the text and send it
        pyautogui.typewrite(text_to_type)
        pyautogui.press('enter')

        # Wait for 3 seconds before sending the next message
        time.sleep(3)

# Create the GUI window
window = tk.Tk()
window.title("Automated Chat Sender")

# Create buttons for starting and stopping the program
start_button = tk.Button(window, text="Start Program", command=start_program, width=20)
start_button.pack(pady=10)

stop_button = tk.Button(window, text="End Program", command=stop_program, state="disabled", width=20)
stop_button.pack(pady=10)

# Run the GUI event loop
window.mainloop()
