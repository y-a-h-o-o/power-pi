from INA226 import get_values
from LCD import LCD 

def setup():
    lcd = LCD()

def loop(): 
    
    # check for button inputs for actions and then do something
    # here will be an infinite loop until something happens, but during it we will
    # read and output the current voltage and current and time 
    # write the data onto a file
    # sleep for an unspecified amount of time

    values = get_values() # gets the values from the INA
    lcd.write_to_lcd(0, 0, "Halloo :3 !!!") # writes to LCD display
    

if __name__ == "__main__":
    try:
        setup() 
        while(True):
            loop()
    except KeyboardInterrupt:
        destroy()
