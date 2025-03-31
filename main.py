from components.INA228 import get_values
from components.LCD import LCD
from data_logging.filewriter import *
from gpiozero import Button, Buzzer
import datetime
import time
import os

# LCD setup
# first parameter should always be 2. Use i2cdetect -y 0 to find I2C address. last param is for backlight 
lcd = LCD(2, 0x3F, True)

# button setup
# replace the numbers in brackets with which ever gpio pin the components are connected to
wait_btn = Button(2) 
alarm_btn = Button(3)
bz = Buzzer(4)

# trailing average list and variable declaration
counter = 1
avg_voltage = 0
avg_current = 0

def loop(): 
    # check for button inputs for actions and then do something
    # here will be an infinite loop until something happens, but during it we will
    # read and output the current voltage and current and time 
    # write the data onto a file
    # sleep for an unspecified amount of time

    # turn off alarm manually when this button is pressed
    if alarm_btn.is_pressed: 
        bz.off()
    
    values = get_values() # gets the values from the INA
    
    lcd.message("Current: " + str(values[0]), 1)
    lcd.message("Voltage: " + str(values[1]), 2)

    # updating current & voltage data and averages
    current = values[0] 
    current_average = current_total/counter
    
    voltage = values[1]
    voltage_average = voltage_total/counter

    # Moves file to USB if stick is inserted
    if not wait_btn.is_pressed:
        usb_path = check_usb()
        if usb_path:
            if os.path.exists("./data.txt"):
                lcd.message("USB INSERT", 1)
                lcd.message("WAIT....", 2)
                transfer_to_usb("./data.txt", usb_path) 
            lcd.message("FILE MOVED", 1)
            lcd.message("UNPLUG USB", 2)
        else:
            data = str(datetime.datetime.now()) +  " " + str(voltage) + " " + str(current)
            write_to_file(data);

    # Log data at 15 second intervals
    time.sleep(15)

if __name__ == "__main__":
    try:
        while(True):
            loop()
    except KeyboardInterrupt:
        print("Exiting...")
