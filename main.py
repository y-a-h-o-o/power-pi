from components.INA228 import get_values
from components.LCD import LCD
from data_logging.filewriter import *
from gpiozero import Button, Buzzer, LED
import datetime
import time
import os

if os.path.exists("./data.txt"):
    os.remove("./data.txt")
# LCD setup
# Use i2cdetect -y 0 to find I2C address. last param is for backlight 
lcd = LCD(0x3F, True)

# LCD confirmation
lcd.message("POWER ON", 1)
lcd.message("SETUP...", 2)

# button setup
wait_btn = Button(4) 
alarm_btn = Button(17)
bz = Buzzer(27)
green_led = LED(22)
red_led = LED(18)

# Green LED to tell whether device is ON
green_led.on()

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
    
    global counter
    global avg_voltage
    global avg_current

    # turn off alarm manually when this button is pressed
    if alarm_btn.is_pressed: 
        bz.off()
        red_led.off()
   
    # gets the values from the INA
    values = get_values()     

    # display to LCD; if freezing screen, don't change the message on LCD
    if not wait_btn.is_pressed: 
        lcd.message("VOLTAGE: " + str(values[0]), 1)
        lcd.message("CURRENT: " + str(values[1]), 2)
 
    voltage = values[0]
    current = values[1]
    
    # alarm will sound if less than 12.0 volts; Outside expected range
    if voltage < 12.0: 
        bz.on()
        red_led.on()
    else:
        bz.off()
        red_led.off()

    # Moves file to USB if stick is inserted.    

    usb_path = check_usb()
    if usb_path:
        if os.path.exists("./data.txt"):
            lcd.message("USB INSERT", 1)
            lcd.message("WAIT....", 2)
            transfer_to_usb("./data.txt", usb_path) 
        lcd.message("FILE MOVED", 1)
        lcd.message("UNPLUG USB", 2)
    else
        # if 15 values are read, write the average of them to file 
        if counter % 16 == 0:  
            avg_voltage /= 15 
            avg_current /= 15 
            data = str(datetime.datetime.now()) +  " " + str(avg_voltage) + " " + str(avg_current)
            log_data(data);
            avg_voltage = 0
            avg_current = 0
        else:
            # increment cumulative voltage and current sum, and increment counter 
            counter += 1
            avg_voltage += voltage
            avg_current += current

    # run loop every second; current will display every second but, every 15 readings we log the average
    # this ensures that more accurate values are stored if power fluctuates
    
    time.sleep(1)

if __name__ == "__main__":
    try:
        while(True):
            loop()
    except KeyboardInterrupt:
        print("Exiting...")
