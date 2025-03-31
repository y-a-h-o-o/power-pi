import os
import time
import datetime
import shutil

def check_usb():

    # change this path based on user name of raspberry pi
    media_path = "/media/sajjadnaqvi/"

    # get all folders in this directory
    all_items = os.listdir(media_path)

    mounted_devices = []
    
    for item in all_items:
        item_path = os.path.join(media_path, item)
        if os.path.isdir(item_path): 
            mounted_devices.append(item)

    if mounted_devices:
        return mounted_devices[0]
    else:
        return None

# Function to transfer the log file to USB
def transfer_to_usb(log_file, usb_path):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    destination_file = os.path.join(usb_path, f"log_{timestamp}.txt")
    
    # Copy log file to USB
    shutil.copy(log_file, destination_file)
    
    # Delete old file after transferring
    os.remove(log_file)

def log_data(data):
    # creates and appends to a file called data.txt. Could name based on current time
    with open("data.txt", "a") as file: 
        file.write(data + "\n")
