import board
import adafruit_ina228 

i2c = board.I2C() 
ina228 = adafruit_ina228.INA228(i2c)

# method to read values from INA228; 
def get_values(): 
    return [ina228.voltage(), ina228.current()]
