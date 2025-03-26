from INA226 import get_values
from LCD import LCD 
import filewriter
import datetime

def setup():
    lcd = LCD()

def loop(): 
    
    # check for button inputs for actions and then do something
    # here will be an infinite loop until something happens, but during it we will
    # read and output the current voltage and current and time 
    # write the data onto a file
    # sleep for an unspecified amount of time

    values = get_values() # gets the values from the INA
    lcd.write_to_lcd(0, 0, values[0] + "V") # writes values to LCD display
    lcd.write_to_lcd(1, 0, values[1] + "mA");
    data = datetime.datetime.now() +  " " + values[0] + " " + values[1]
    filewriter.write_to_file(data);

if __name__ == "__main__":
    try:
        setup() 
        while(True):
            loop()
    except KeyboardInterrupt:
        destroy()
