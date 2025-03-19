import LCD1602
import time 

class LCD(self):
    def __init__(self):
        LCD1602.init(0x27, 1); # whatever slave adress we need, and we need a background light probabaly 
        LCD1602.write(0, 0, 'Starting')
        LCD1602.write(1, 0, 'Display.....')
        time.sleep(2)
    
    def write_to_lcd(row, col, text): # writes a string to the LCD display based on the specified row and column
            LCD1602.write(row, col, test)

