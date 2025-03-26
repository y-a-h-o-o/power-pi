import board
import adafruit_ina228

#replace with required values

i2c = board.I2C() 
ina228 = adafruit_ina228.INA228(i2c)

def get_values(): 
    return [ina228.voltage(), ina228.current(), ina228.power()]
