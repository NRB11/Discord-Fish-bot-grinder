import psutil
import pyautogui
import time

# Step 1: Detect if Discord is running
def is_discord_running():
    # Iterate through the running processes and check for Discord
    for process in psutil.process_iter(['name']):
        if 'discord' in process.info['name'].lower():
            return True
    return False

# Step 2: Simulate opening Discord and navigating to a specific chat
def locate_chat(chat_name):
    if is_discord_running():
        print("Discord is open!")

        # Simulate the keyboard shortcut to open channel search
        pyautogui.hotkey('ctrl', 'k')  # Ctrl+K opens the channel search
        time.sleep(1)  # Wait for the search bar to open

        # Type the name of the chat/channel
        pyautogui.write(chat_name)
        time.sleep(1)  # Wait for the search to process

        # Press 'Enter' to select the chat
        pyautogui.press('enter')
        print(f"Attempting to navigate to the chat: {chat_name}")
    else:
        print("Discord is not running!")

# Main Function
if __name__ == "__main__":
    # Specify the chat/channel name to search for
    locate_chat("fishing")  # Replace "general" with the name of the chat you're looking for
ishing