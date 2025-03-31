import random

hardware = True

# code needed to test functionality without hardware
try:
    import board
    import adafruit_ina228 
except ImportError: 
    hardware = False

# if on hardware, use hardware specifc class via adafruit libraries 
if hardware:
    i2c = board.I2C() 
    ina228 = adafruit_ina228.INA228(i2c)

# method to read values from INA228; gives random values otherwise
def get_values(): 
    if hardware:
       return [ina228.voltage(), ina228.current()]
    return [random.uniform(12.0, 48.0), random.uniform(5.0, 10.0)] 
