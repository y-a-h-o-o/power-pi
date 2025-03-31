from components.INA228 import get_values
from components.LCD import LCD 
from data_logging.filewriter import write_to_file
import RPi.GPIO as GPIO
import datetime
import time

#LCD setup
# first parameter should always be 2. Use i2cdetect -y 0 to find I2C address. last param is for backlight 
lcd = LCD(2, 0x3F, True)

#GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN);
# GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN); 
# GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN); 

def loop(): 
    
    # check for button inputs for actions and then do something
    # here will be an infinite loop until something happens, but during it we will
    # read and output the current voltage and current and time 
    # write the data onto a file
    # sleep for an unspecified amount of time
    
    button_state1 = GPIO.input(10)
    # button_state2 = GPIO.input(9)
    # button_state3 = GPIO.input(8)

    if button_state1 == True: 
        return  #skip reading and writing values while this button is held
    
    values = get_values() # gets the values from the INA
    
    lcd.message("Current: " + values[0], 1)
    lcd.message("Voltage: " + values[1], 2)
    
    print("Displaying data on LCD Display")
        
    voltage = values[0]
    current = values[1] 
    
    data = str(datetime.datetime.now()) +  " " + str(voltage) + " " + str(current)
    write_to_file(data);
   
    time.sleep(1)

if __name__ == "__main__":
    try:
        while(True):
            loop()
    except KeyboardInterrupt:
        print("Exiting...")
        GPIO.cleanup()
