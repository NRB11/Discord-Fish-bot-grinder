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
def locate_chat(server_name, chat_name):
    if is_discord_running():
        print("Discord is open!")

        # Simulate the keyboard shortcut to open the server search
        pyautogui.hotkey('ctrl', 'k')  # Ctrl+K opens the channel search
        time.sleep(1)  # Wait for the search bar to open

        # Type the server name first (to locate the server)
        pyautogui.write(server_name)
        time.sleep(1)  # Wait for the search to process
        
        pyautogui.press('enter')  # Select the server
        time.sleep(2)  # Wait for the server to load

        # Now locate the specific chat within the server
        locate_chat_in_server(chat_name)
    else:
        print("Discord is not running!")

# Step 3: Locate a chat within a server (channel search)
def locate_chat_in_server(chat_name):
    print(f"Looking for chat: {chat_name}...")
    
    # Simulate searching for the chat name within the server
    pyautogui.hotkey('ctrl', 'k')  # Again open the search bar (within the server context)
    time.sleep(1)  # Wait for the search bar to open

    pyautogui.write(chat_name)  # Type the name of the chat/channel
    time.sleep(1)  # Wait for the search to process

    pyautogui.press('enter')  # Press 'Enter' to select the chat
    print(f"Attempting to navigate to the chat: {chat_name} in the server.")

# Step 4: Check if the chat is in DM or Server Channel
def is_dm(chat_name):
    # Direct messages are typically in the form of a user's name.
    # Server channels will usually have a channel name format (e.g., #general, #bot-commands)
    
    if chat_name[0] != '#':  # Assuming chats that start with "#" are channels
        return True  # Likely a Direct MaaaAAAaaa essage (since it’s a user name)
    return False  # It's likely a server channel (since it starts with '#')

# Main Function
if __name__ == "__main__":
    # Specify the server and chat/channel name to search for
    server = "AaaaAAAaaa"  # Replace with your server name
    chat = "empty"  # Replace with the chat/channel name you want to search for

    locate_chat(server, chat)  # Call the function to locate the chat in the server
